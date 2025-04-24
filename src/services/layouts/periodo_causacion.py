from .base import LayoutProvider, LineLayout, FieldDefinition


class PeriodoCausacionLayout(LayoutProvider):
    """Provider for the Periodo Causacion (R) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='R',
            description='Periodo Causación',
            fields=[
                FieldDefinition(0, 2, 'str', 'periodo_causacion', 'Tipo de registro'),
                FieldDefinition(2, 4, 'str', 'ejercicio_asignado', 'Ejercicio Asignado'),
                FieldDefinition(6, 2, 'str', 'periodo_asignado', 'Periodo Asignado')
            ]
        )
