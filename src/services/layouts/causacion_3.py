from .base import LayoutProvider, LineLayout, FieldDefinition


class Causacion3Layout(LayoutProvider):
    """Provider for the Causacion 3 (E) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='E',
            description='Causación 3',
            fields=[
                FieldDefinition(0, 2, 'str', 'causacion_3', 'Tipo de registro'),
                FieldDefinition(2, 20, 'str', 'id_concepto_ietu', 'ID Concepto IETU')
            ]
        )
