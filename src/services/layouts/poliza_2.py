from .base import LayoutProvider, LineLayout, FieldDefinition


class Poliza2Layout(LayoutProvider):
    """Provider for the Poliza 2 (FE) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='FE',
            description='Póliza 2',
            fields=[
                FieldDefinition(0, 2, 'str', 'poliza_2', 'Tipo de registro'),
                FieldDefinition(2, 254, 'str', 'ruta_anexo', 'Ruta Anexo'),
                FieldDefinition(256, 254, 'str', 'archivo_anexo', 'Archivo Anexo')
            ]
        )
