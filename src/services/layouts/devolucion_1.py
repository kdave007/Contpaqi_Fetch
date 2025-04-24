from .base import LayoutProvider, LineLayout, FieldDefinition


class Devolucion1Layout(LayoutProvider):
    """Provider for the Devolucion 1 (V) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='V',
            description='Devolución 1',
            fields=[
                FieldDefinition(0, 2, 'str', 'devolucion_1', 'Tipo de registro'),
                FieldDefinition(2, 6, 'str', 'id_proveedor', 'ID Proveedor'),
                FieldDefinition(8, 20, 'float', 'imp_total', 'Importe Total'),
                FieldDefinition(28, 9, 'float', 'por_iva', 'Porcentaje IVA'),
                FieldDefinition(37, 20, 'float', 'imp_base', 'Importe Base'),
                FieldDefinition(57, 20, 'float', 'imp_iva', 'Importe IVA'),
                FieldDefinition(77, 1, 'float', 'causal_iva', 'Causal IVA 1,0'),
                FieldDefinition(78, 1, 'float', 'exento_iva', 'Exento IVA 1,0'),
                FieldDefinition(79, 15, 'str', 'serie', 'Serie'),
                FieldDefinition(94, 8, 'str', 'folio', 'Folio'),
                FieldDefinition(102, 30, 'str', 'referencia', 'Referencia'),
                FieldDefinition(132, 20, 'float', 'otros_imptos', 'Otros Impuestos'),
                FieldDefinition(152, 20, 'float', 'imp_sin_ret', 'Importe Sin Retención'),
                FieldDefinition(172, 20, 'float', 'iva_retenido', 'IVA Retenido'),
                FieldDefinition(192, 20, 'float', 'isr_retenido', 'ISR Retenido'),
                FieldDefinition(212, 20, 'float', 'gran_total', 'Gran Total'),
                FieldDefinition(232, 4, 'str', 'ejercicio_asignado', 'Ejercicio Asignado'),
                FieldDefinition(236, 4, 'str', 'periodo_asignado', 'Periodo Asignado'),
                FieldDefinition(240, 30, 'str', 'id_cuenta', 'ID Cuenta'),
                FieldDefinition(270, 20, 'float', 'iva_pag_no_acred', 'IVA Pagado No Acreditable'),
                FieldDefinition(290, 36, 'str', 'uuid', 'UUID'),
                FieldDefinition(326, 13, 'str', 'rfc', 'RFC'),
                FieldDefinition(339, 20, 'float', 'ieps', 'IEPS')
            ]
        )
