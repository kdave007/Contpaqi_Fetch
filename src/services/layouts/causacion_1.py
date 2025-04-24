from .base import LayoutProvider, LineLayout, FieldDefinition


class Causacion1Layout(LayoutProvider):
    """Provider for the Causacion 1 (C) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='C',
            description='Causación 1',
            fields=[
                FieldDefinition(0, 2, 'str', 'causacion_1', 'Tipo de registro'),
                FieldDefinition(2, 1, 'str', 'tipo', 'Tipo'),
                FieldDefinition(3, 20, 'float', 'tot_tasa15', 'Total Tasa 15%'),
                FieldDefinition(23, 20, 'float', 'base_tasa15', 'Base Tasa 15%'),
                FieldDefinition(43, 20, 'float', 'iva_tasa15', 'IVA Tasa 15%'),
                FieldDefinition(63, 20, 'float', 'tot_tasa10', 'Total Tasa 10%'),
                FieldDefinition(83, 20, 'float', 'base_tasa10', 'Base Tasa 10%'),
                FieldDefinition(103, 20, 'float', 'iva_tasa10', 'IVA Tasa 10%'),
                FieldDefinition(123, 20, 'float', 'tot_tasa0', 'Total Tasa 0%'),
                FieldDefinition(143, 20, 'float', 'base_tasa0', 'Base Tasa 0%'),
                FieldDefinition(163, 20, 'float', 'tot_tasa_exento', 'Total Tasa Exento'),
                FieldDefinition(183, 20, 'float', 'base_tasa_exento', 'Base Tasa Exento'),
                FieldDefinition(203, 20, 'float', 'tot_otra_tasa', 'Total Otra Tasa'),
                FieldDefinition(223, 20, 'float', 'base_otra_tasa', 'Base Otra Tasa'),
                FieldDefinition(243, 20, 'float', 'iva_otra_tasa', 'IVA Otra Tasa'),
                FieldDefinition(263, 20, 'float', 'isr_retenido', 'ISR Retenido'),
                FieldDefinition(283, 20, 'float', 'tot_otros', 'Total Otros'),
                FieldDefinition(303, 20, 'float', 'iva_retenido', 'IVA Retenido'),
                FieldDefinition(323, 1, 'float', 'captado', 'Captado 1,0'),
                FieldDefinition(324, 1, 'float', 'no_causar', 'No Causar 1,0'),
                FieldDefinition(325, 20, 'float', 'ieps', 'IEPS')
            ]
        )
