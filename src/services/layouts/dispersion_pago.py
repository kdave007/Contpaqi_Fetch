from .base import LayoutProvider, LineLayout, FieldDefinition


class DispersionPagoLayout(LayoutProvider):
    """Provider for the Dispersion Pago (DP) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='DP',
            description='Dispersión Pago',
            fields=[
                FieldDefinition(0, 2, 'str', 'dispersion_pago', 'Tipo de registro'),
                FieldDefinition(2, 36, 'str', 'uuid', 'UUID'),
                FieldDefinition(38, 36, 'str', 'uuid_rep', 'UUID Rep'),
                FieldDefinition(74, 36, 'str', 'guid_ref', 'GUID Ref'),
                FieldDefinition(110, 5, 'str', 'num_nodo_pago', 'Número Nodo Pago'),
                FieldDefinition(115, 8, 'date', 'fecha_pago', 'Fecha Pago yyyyMMdd'),
                FieldDefinition(123, 20, 'float', 'total_pago', 'Total Pago'),
                FieldDefinition(143, 20, 'float', 'tipo_cambio', 'Tipo Cambio'),
                FieldDefinition(163, 20, 'float', 'total_pago_comprobante', 'Total Pago Comprobante')
            ]
        )
