from dataclasses import dataclass
from typing import Dict, Any, Optional
from datetime import datetime

@dataclass
class Poliza:
    """Represents a complete poliza with its header and movements"""
    number: int  # The poliza number (used as key in the dictionary)
    raw_header: str = ""
    header_error: Optional[str] = None
    
    # Header fields
    id: str = "P"  # Always 'P' for poliza header
    fecha: Optional[str] = None  # Format: YYYYMMDD
    tipo_pol: Optional[str] = None
    folio: Optional[str] = None
    clase: Optional[str] = None
    id_diario: Optional[str] = None
    concepto: Optional[str] = None
    sist_orig: Optional[str] = None
    impresa: Optional[float] = None
    ajuste: Optional[float] = None
    guid: Optional[str] = None
    
    # Movements (parts)
    parts: Dict[int, Dict[str, Any]] = None  # Dictionary of movements indexed by number
    
    def __post_init__(self):
        if self.parts is None:
            self.parts = {}
    
    def add_movement(self, mov_num: int, movement_data: Dict[str, Any]):
        """Add a movement to this poliza
        
        Args:
            mov_num: The movement number (1-based)
            movement_data: Dictionary with the movement data
        """
        self.parts[mov_num] = movement_data
    
    @property
    def total_movements(self) -> int:
        """Get the total number of movements in this poliza"""
        return len(self.parts)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the poliza to a dictionary format matching the desired structure"""
        # Start with header fields
        result = {
            'id': self.id,
            'fecha': self.fecha,
            'tipo_pol': self.tipo_pol,
            'folio': self.folio,
            'clase': self.clase,
            'id_diario': self.id_diario,
            'concepto': self.concepto,
            'sist_orig': self.sist_orig,
            'impresa': self.impresa,
            'ajuste': self.ajuste,
            'guid': self.guid
        }
        
        # Clean header fields
        header = {k: v for k, v in result.items() if v is not None}
        
        # Clean movement fields
        parts = {}
        for num, mov in self.parts.items():
            cleaned_mov = {k: v for k, v in mov.items() if v is not None}
            if cleaned_mov:  # Only include if it has data
                parts[num] = cleaned_mov
        
        # Only include parts if we have any
        if parts:
            header['parts'] = parts
        
        return header
