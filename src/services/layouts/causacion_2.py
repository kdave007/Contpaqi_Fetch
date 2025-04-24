from .base import LayoutProvider, LineLayout, FieldDefinition


class Causacion2Layout(LayoutProvider):
    """Provider for the Causacion (D) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='D',
            description='Causación',
            fields=[
                FieldDefinition(0, 2, 'str', 'causacion_2', 'Tipo de registro'),
                FieldDefinition(2, 20, 'float', 'iva_tasa15_no_acred', 'IVA Tasa 15% No Acreditable'),
                FieldDefinition(22, 20, 'float', 'iva_tasa10_no_acred', 'IVA Tasa 10% No Acreditable'),
                FieldDefinition(42, 20, 'float', 'ietu', 'IETU'),
                FieldDefinition(62, 1, 'int', 'modificado', 'Modificado'),
                FieldDefinition(63, 1, 'str', 'origen', 'Origen'),
                FieldDefinition(64, 20, 'float', 'tot_tasa16', 'Total Tasa 16%'),
                FieldDefinition(84, 20, 'float', 'base_tasa16', 'Base Tasa 16%'),
                FieldDefinition(104, 20, 'float', 'iva_tasa16', 'IVA Tasa 16%'),
                FieldDefinition(124, 20, 'float', 'iva_tasa16_no_acred', 'IVA Tasa 16% No Acreditable'),
                FieldDefinition(144, 20, 'float', 'tot_tasa11', 'Total Tasa 11%'),
                FieldDefinition(164, 20, 'float', 'base_tasa11', 'Base Tasa 11%'),
                FieldDefinition(184, 20, 'float', 'iva_tasa11', 'IVA Tasa 11%'),
                FieldDefinition(204, 20, 'float', 'iva_tasa11_no_acred', 'IVA Tasa 11% No Acreditable'),
                FieldDefinition(224, 20, 'float', 'tot_tasa8', 'Total Tasa 8%'),
                FieldDefinition(244, 20, 'float', 'base_tasa8', 'Base Tasa 8%'),
                FieldDefinition(264, 20, 'float', 'iva_tasa8', 'IVA Tasa 8%'),
                FieldDefinition(284, 20, 'float', 'iva_tasa8_no_acred', 'IVA Tasa 8% No Acreditable')
            ]
        )