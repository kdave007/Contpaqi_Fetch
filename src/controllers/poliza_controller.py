from typing import Dict, Any
from pathlib import Path

from models.poliza import Poliza
from services.line_parser import LineParser
from services.layouts import registry

class PolizaController:
    def __init__(self):
        self.parser = LineParser(registry)
        self.polizas: Dict[int, Poliza] = {}
        self.current_poliza_num = 0
    
    def parse_file(self, file_path: str | Path) -> None:
        """Parse a file and store all polizas found in it"""
        current_poliza = None
        current_movement_num = 0
        
        for parsed_line in self.parser.read_lines(str(file_path)):
            # Skip empty lines
            if not parsed_line.clean_line:
                continue
                
            # If this is a new poliza header
            if parsed_line.clean_line.startswith('P '):
                # Save previous poliza if exists
                if current_poliza:
                    self.polizas[current_poliza.number] = current_poliza
                
                # Increment poliza number
                self.current_poliza_num += 1
                current_movement_num = 0
                
                # Try to parse the header
                try:
                    header_data = parsed_line.layout.parse_line(parsed_line.clean_line)
                    # Create new poliza with direct field mapping
                    current_poliza = Poliza(
                        number=self.current_poliza_num,
                        raw_header=parsed_line.raw_line,
                        fecha=header_data.get('fecha'),
                        tipo_pol=header_data.get('tipo_pol'),
                        folio=header_data.get('folio'),
                        clase=header_data.get('clase'),
                        id_diario=header_data.get('id_diario'),
                        concepto=header_data.get('concepto'),
                        sist_orig=header_data.get('sist_orig'),
                        impresa=header_data.get('impresa'),
                        ajuste=header_data.get('ajuste'),
                        guid=header_data.get('guid')
                    )
                except Exception as e:
                    # Create poliza with error
                    current_poliza = Poliza(
                        number=self.current_poliza_num,
                        raw_header=parsed_line.raw_line,
                        header_error=str(e)
                    )
            
            # If we have a current poliza and this is a movement
            elif current_poliza and parsed_line.clean_line.startswith('M'):
                try:
                    # Parse movement data
                    movement_data = parsed_line.layout.parse_line(parsed_line.clean_line)
                    
                    # Increment movement number
                    current_movement_num += 1
                    
                    # Add movement data directly
                    current_poliza.add_movement(current_movement_num, {
                        'id': 'M1',
                        'cuenta': movement_data.get('cuenta'),
                        'referencia': movement_data.get('referencia'),
                        'tipo_movto': movement_data.get('tipo_movto'),
                        'debe': movement_data.get('debe'),
                        'haber': movement_data.get('haber'),
                        'id_diario': movement_data.get('id_diario'),
                        'concepto': movement_data.get('concepto'),
                        'id_seg_neg': movement_data.get('id_seg_neg'),
                        'guid': movement_data.get('guid'),
                        'fecha_aplicacion': movement_data.get('fecha_aplicacion')
                    })
                except Exception as e:
                    # Add movement with error
                    current_poliza.add_movement(current_movement_num, {
                        'id': 'M1',
                        'error': str(e)
                    })
        
        # Don't forget to add the last poliza
        if current_poliza:
            self.polizas[current_poliza.number] = current_poliza
    
    def get_polizas(self) -> Dict[int, Poliza]:
        """Get all parsed polizas"""
        return self.polizas
    
    def clear(self) -> None:
        """Clear all stored polizas"""
        self.polizas.clear()
        self.current_poliza_num = 0
    
    def to_dict(self) -> Dict[int, Dict[str, Any]]:
        """Convert all polizas to dictionary format"""
        return {num: poliza.to_dict() for num, poliza in self.polizas.items()}
