from .base import LayoutProvider, LineLayout, FieldDefinition


class Devolucion2Layout(LayoutProvider):
    """Provider for the Devolucion 2 (W2) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='W2',
            description='Devolución 2',
            fields=[
                FieldDefinition(0, 2, 'str', 'devolucion_2', 'Tipo de registro'),
                FieldDefinition(2, 20, 'float', 'ietu_deducible', 'IETU Deducible'),
                FieldDefinition(22, 20, 'float', 'ietu_acreditable', 'IETU Acreditable'),
                FieldDefinition(42, 1, 'float', 'ietu_modificado', 'IETU Modificado 1,0'),
                FieldDefinition(43, 20, 'float', 'id_concepto_ietu', 'ID Concepto IETU')
            ]
        )
