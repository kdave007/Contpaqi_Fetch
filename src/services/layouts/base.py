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
        line_length = len(line)

        # Process fields in order
        for field in self.fields:
            # Handle fields with negative positions (counting from end)
            if field.start_pos < 0:
                if abs(field.start_pos) > line_length:
                    continue
                value = line[field.start_pos:field.start_pos + field.length].strip()
            # Handle fields with positive positions
            else:
                if field.start_pos + field.length > line_length:
                    continue
                value = line[field.start_pos:field.start_pos + field.length].strip()
            
            # Skip empty values
            if not value:
                continue

            # Convert numeric values
            if field.field_type in ('int', 'float'):
                try:
                    result[field.name] = float(value) if field.field_type == 'float' else int(value)
                except ValueError:
                    continue
            else:
                result[field.name] = value



        return result


class LayoutProvider(ABC):
    """Abstract base class for layout providers"""
    @abstractmethod
    def get_layout(self) -> LineLayout:
        """Return the layout configuration"""
        pass