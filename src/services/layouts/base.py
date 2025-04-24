from dataclasses import dataclass
from typing import List, Dict, Optional
from abc import ABC, abstractmethod


@dataclass
class FieldDefinition:
    """Defines a field's position and type in a line layout"""
    start_pos: int
    length: int
    field_type: str  # 'str', 'int', 'float', 'date', etc.
    name: str
    description: str = ""
    required: bool = True


@dataclass
class LineLayout:
    """Defines the layout for a specific line type (identified by first letter)"""
    identifier: str  # The letter that identifies this type of line
    description: str
    fields: List[FieldDefinition]
    
    def parse_line(self, line: str) -> Dict[str, any]:
        """Parse a line according to the defined layout"""
        result = {}
        for field in self.fields:
            if len(line) < field.start_pos + field.length:
                if field.required:
                    raise ValueError(f"Line too short for field {field.name}")
                continue
                
            value = line[field.start_pos:field.start_pos + field.length].strip()
            if not value and field.required:
                raise ValueError(f"Required field {field.name} is empty")
                
            if field.field_type == 'int':
                result[field.name] = int(value) if value else 0
            elif field.field_type == 'float':
                result[field.name] = float(value) if value else 0.0
            elif field.field_type == 'date':
                result[field.name] = value  # You might want to parse this into a date object
            else:
                result[field.name] = value
        return result


class LayoutProvider(ABC):
    """Abstract base class for layout providers"""
    @abstractmethod
    def get_layout(self) -> LineLayout:
        """Return the layout configuration"""
        pass