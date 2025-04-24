from .base import LayoutProvider, LineLayout, FieldDefinition


class Poliza1Layout(LayoutProvider):
    """Provider for the Poliza 1 (P) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='P',
            description='Póliza 1',
            fields=[
                FieldDefinition(0, 2, 'str', 'poliza_1', 'Tipo de registro'),
                FieldDefinition(2, 8, 'date', 'fecha', 'Fecha yyyyMMdd'),
                FieldDefinition(10, 4, 'str', 'tipo_pol', 'Tipo de póliza'),
                FieldDefinition(14, 9, 'str', 'folio', 'Folio'),
                FieldDefinition(23, 1, 'str', 'clase', 'Clase'),
                FieldDefinition(24, 10, 'str', 'id_diario', 'ID Diario'),
                FieldDefinition(34, 100, 'str', 'concepto', 'Concepto'),
                FieldDefinition(134, 3, 'str', 'sist_orig', 'Sistema Origen'),
                FieldDefinition(137, 1, 'float', 'impresa', 'Impresa 1,0'),
                FieldDefinition(138, 1, 'float', 'ajuste', 'Ajuste 1,0'),
                FieldDefinition(139, 36, 'str', 'guid', 'GUID')
            ]
        )
