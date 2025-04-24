from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from uuid import UUID


@dataclass
class PolizaHeader:
    fecha: str
    numero: str
    tipo: str
    descripcion: str
    uuid: str
    otros_campos: dict  # For any additional fields we might find

@dataclass
class PolizaLine:
    cuenta: str
    referencia: str  # e.g., FA94509978
    debe_haber: int  # 1 for debe, 0 for haber
    monto: float
    descripcion: str
    uuid: str
    fecha: str
    am_reference: Optional[str] = None  # For AM lines that follow
    otros_campos: dict = None  # For any additional fields

class Poliza:
    def __init__(self):
        """Initialize the Poliza model."""
        self.header: Optional[PolizaHeader] = None
        self.lines: List[PolizaLine] = []
        self.file_path: Optional[str] = None

    def _parse_header(self, line: str) -> PolizaHeader:
        """Parse a header line into structured data."""
        # Split the line into parts, keeping track of original positions
        parts = line.split()
        
        # Extract known fields based on their typical positions and patterns
        try:
            # Find UUID (it's typically a long string with hyphens)
            uuid = next((part for part in parts if '-' in part and len(part) > 30), '')
            
            # Find fecha (date in format YYYYMMDD)
            fecha = next((part for part in parts if len(part) == 8 and part.isdigit()), '')
            
            # Find numero (typically a short number after the date)
            numero_idx = parts.index(fecha) + 1 if fecha in parts else -1
            numero = parts[numero_idx] if numero_idx > -1 and numero_idx < len(parts) else ''
            
            # Get the description (typically the longest text part)
            descripcion = next((part for part in parts if len(part) > 20 and not '-' in part), '')
            
            # First part is typically the line type
            tipo = parts[0] if parts else ''
            
            # Store any other fields we found in otros_campos
            otros_campos = {
                'raw_line': line,
                'remaining_parts': [p for p in parts if p not in [uuid, fecha, numero, descripcion, tipo]]
            }
            
            return PolizaHeader(
                fecha=fecha,
                numero=numero,
                tipo=tipo,
                descripcion=descripcion,
                uuid=uuid,
                otros_campos=otros_campos
            )
        except Exception as e:
            print(f"Error parsing header: {e}")
            return None

    def _parse_line(self, line: str, prev_line: Optional[str] = None) -> PolizaLine:
        """Parse a detail line into structured data."""
        try:
            parts = line.split()
            
            # If this is an AM line (reference line), return None but update previous line
            if len(parts) == 2 and len(parts[1]) > 30 and '-' in parts[1]:
                if self.lines:  # If we have previous lines
                    self.lines[-1].am_reference = parts[1]
                return None
                
            # Regular line parsing
            cuenta = parts[1] if len(parts) > 1 else ''
            referencia = next((part for part in parts if part.startswith('FA')), '')
            
            # Find the numerical values (monto)
            montos = [float(p) for p in parts if p.replace('.', '').isdigit()]
            monto = montos[0] if montos else 0.0
            
            # debe_haber is typically right after the cuenta
            debe_haber = 1 if len(parts) > 2 and parts[2] == '1' else 0
            
            # UUID is typically a long string with hyphens
            uuid = next((part for part in parts if '-' in part and len(part) > 30), '')
            
            # fecha is typically YYYYMMDD format at the end
            fecha = next((part for part in parts if len(part) == 8 and part.isdigit()), '')
            
            # descripcion is typically the longest text part
            descripcion = next((part for part in parts if len(part) > 20 and not '-' in part), '')
            
            otros_campos = {
                'raw_line': line,
                'remaining_parts': [p for p in parts if p not in 
                    [cuenta, referencia, str(monto), uuid, fecha, descripcion]]
            }
            
            return PolizaLine(
                cuenta=cuenta,
                referencia=referencia,
                debe_haber=debe_haber,
                monto=monto,
                descripcion=descripcion,
                uuid=uuid,
                fecha=fecha,
                otros_campos=otros_campos
            )
        except Exception as e:
            print(f"Error parsing line: {e}")
            return None

    def load_from_file(self, file_path: str) -> bool:
        """
        Load poliza data from a text file.
        
        Args:
            file_path (str): Path to the text file to read
            
        Returns:
            bool: True if file was successfully loaded, False otherwise
        """
        self.file_path = file_path
        self.lines = []
        self.header = None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                prev_line = None
                for line in file:
                    clean_line = line.strip()
                    if not clean_line:
                        continue
                        
                    # If we don't have a header yet, try to parse as header
                    if not self.header:
                        header = self._parse_header(clean_line)
                        if header:
                            self.header = header
                            continue
                    
                    # Try to parse as detail line
                    detail_line = self._parse_line(clean_line, prev_line)
                    if detail_line:
                        self.lines.append(detail_line)
                    
                    prev_line = clean_line
                        
                return True
                
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found")
            return False
        except Exception as e:
            print(f"Error reading file: {e}")
            return False

    def get_line(self, index: int) -> Optional[PolizaLine]:
        """Get a specific line by index."""
        if 0 <= index < len(self.lines):
            return self.lines[index]
        return None

    def get_all_lines(self) -> List[PolizaLine]:
        """Get all detail lines."""
        return self.lines.copy()

    def line_count(self) -> int:
        """Get the total number of detail lines."""
        return len(self.lines)