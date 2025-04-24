from .base import LayoutProvider, LineLayout, FieldDefinition

#validated positioning
class AsocDoctoLayout(LayoutProvider):
    """Provider for the Asoc Docto (AD) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='AD',
            description='Asociación Documento',
            fields=[
                FieldDefinition(0, 2, 'str', 'asoc_docto', 'Tipo de registro'),
                FieldDefinition(3, 36, 'str', 'uuid', 'UUID')
            ]
        )
