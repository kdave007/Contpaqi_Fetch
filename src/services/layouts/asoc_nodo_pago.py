from .base import LayoutProvider, LineLayout, FieldDefinition


class AsocNodoPagoLayout(LayoutProvider):
    """Provider for the Asoc Nodo Pago (AP) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='AP',
            description='Asociación Nodo Pago',
            fields=[
                FieldDefinition(0, 2, 'str', 'asoc_nodo_pago', 'Tipo de registro'),
                FieldDefinition(2, 36, 'str', 'uuid_rep', 'UUID Rep'),
                FieldDefinition(38, 2, 'str', 'num_nodo_pago', 'Número Nodo Pago'),
                FieldDefinition(40, 36, 'str', 'guid_referencia', 'GUID Referencia'),
                FieldDefinition(76, 30, 'str', 'application_type', 'Application Type')
            ]
        )
