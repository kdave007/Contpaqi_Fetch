from typing import Dict, Optional
from .base import LineLayout


class LayoutRegistry:
    """Registry for all layout providers"""
    _instance = None
    _layouts: Dict[str, LineLayout] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def register_layout(cls, identifier: str, layout: LineLayout):
        """Register a new layout"""
        cls._layouts[identifier.upper()] = layout

    @classmethod
    def get_layout(cls, line: str) -> Optional[LineLayout]:
        """Get layout for a specific line based on its 2-space identifier"""
        if not line or len(line) < 2:
            return None
            
        # Get first two spaces (whether it's "P " or "M1")
        identifier = line[:2].rstrip().upper()
        return cls._layouts.get(identifier)