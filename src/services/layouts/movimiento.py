from .base import LayoutProvider, LineLayout, FieldDefinition


class MovimientoLayout(LayoutProvider):
    """Provider for the Movimiento (M) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='M',
            description='Movimiento de póliza',
            fields=[
                FieldDefinition(0, 2, 'str', 'movto_poliza_1', 'Tipo de registro'),
                FieldDefinition(2, 30, 'str', 'id_cuenta', 'ID de la cuenta'),
                FieldDefinition(32, 10, 'str', 'referencia', 'Referencia'),
                FieldDefinition(42, 1, 'float', 'tipo_movto', 'Tipo de movimiento 1,0'),
                FieldDefinition(43, 20, 'float', 'importe', 'Importe'),
                FieldDefinition(63, 10, 'str', 'id_diario', 'ID Diario'),
                FieldDefinition(73, 20, 'float', 'importe_me', 'Importe ME'),
                FieldDefinition(93, 100, 'str', 'concepto', 'Concepto'),
                FieldDefinition(193, 4, 'str', 'id_seg_neg', 'ID Segmento Negocio')
            ]
        )