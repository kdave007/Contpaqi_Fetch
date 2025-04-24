from typing import Iterator, Optional
from dataclasses import dataclass
from .layouts.registry import LayoutRegistry
from .layouts.base import LineLayout


@dataclass
class ParsedLine:
    """Represents a parsed line with its raw content"""
    raw_line: str
    clean_line: str
    layout: Optional[LineLayout] = None


class LineParser:
    """Simple line parser that reads lines directly from the file"""
    
    def __init__(self, registry: LayoutRegistry):
        self.registry = registry

    def read_lines(self, file_path: str) -> Iterator[ParsedLine]:
        """Read lines from file directly.
        
        Args:
            file_path: Path to the file to read
            
        Yields:
            ParsedLine objects containing the raw lines
        """
        with open(file_path, 'r', encoding='latin1') as f:
            for line in f:
                # Skip empty lines
                if not line.strip():
                    continue
                    
                # Get the layout for this line
                layout = self.registry.get_layout(line)
                
                # Create ParsedLine object with raw line
                parsed = ParsedLine(
                    raw_line=line,
                    clean_line=line.rstrip('\n'),  # Just remove newline
                    layout=layout
                )
                
                yield parsed
