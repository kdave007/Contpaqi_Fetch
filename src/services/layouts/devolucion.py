from .base import LayoutProvider, LineLayout, FieldDefinition


class DevolucionLayout(LayoutProvider):
    """Provider for the Devolucion (W) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='W',
            description='Devolución',
            fields=[
                FieldDefinition(0, 2, 'str', 'devolucion', 'Tipo de registro'),
                FieldDefinition(2, 20, 'float', 'ietu_deducible', 'IETU Deducible'),
                FieldDefinition(22, 1, 'float', 'ietu_modificado', 'IETU Modificado 1,0')
            ]
        )
