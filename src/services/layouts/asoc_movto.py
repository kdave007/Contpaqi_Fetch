from .base import LayoutProvider, LineLayout, FieldDefinition

#validated positioning
class AsocMovtoLayout(LayoutProvider):
    """Provider for the Asoc Movto (AM) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='AM',
            description='Asociación Movimiento',
            fields=[
                FieldDefinition(0, 2, 'str', 'asoc_movto', 'Tipo de registro'),
                FieldDefinition(3, 36, 'str', 'uuid', 'UUID')
            ]
        )
