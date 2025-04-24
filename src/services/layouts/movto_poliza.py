from .base import LayoutProvider, LineLayout, FieldDefinition


class MovtoPolizaLayout(LayoutProvider):
    """Provider for the Movto Poliza (M1) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='M1',
            description='Movimiento de Póliza',
            fields=[
                FieldDefinition(0, 2, 'str', 'movto_poliza', 'Tipo de registro'),
                FieldDefinition(2, 30, 'str', 'id_cuenta', 'ID Cuenta'),
                FieldDefinition(32, 30, 'str', 'referencia', 'Referencia'),
                FieldDefinition(62, 1, 'float', 'tipo_movto', 'Tipo Movimiento 1,0'),
                FieldDefinition(63, 20, 'float', 'importe', 'Importe'),
                FieldDefinition(83, 10, 'str', 'id_diario', 'ID Diario'),
                FieldDefinition(93, 20, 'float', 'importe_me', 'Importe ME'),
                FieldDefinition(113, 100, 'str', 'concepto', 'Concepto'),
                FieldDefinition(213, 4, 'str', 'id_seg_neg', 'ID Segmento Negocio'),
                FieldDefinition(217, 36, 'str', 'guid', 'GUID'),
                FieldDefinition(253, 8, 'date', 'fecha_aplicacion', 'Fecha Aplicación yyyyMMdd')
            ]
        )
