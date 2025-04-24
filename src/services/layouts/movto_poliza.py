from .base import LayoutProvider, LineLayout, FieldDefinition

#validated positioning
class MovtoPolizaLayout(LayoutProvider):
    """Provider for the Movto Poliza (M1) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='M1',
            description='Movimiento de Póliza',
            fields=[
                # Layout based on field definition table with spaces:
                # Tipo  Nombre           Longitud  Formato
                # E     movto.1          2         M1
                # S     (space)          1
                # A     Cuenta           30
                # S     (space)          1
                # A     Referencia       30
                # S     (space)          1
                # A     TipoMovto        1         1,0
                # S     (space)          1
                # A     Debe             20
                # S     (space)          1
                # A     IdDiario         10
                # S     (space)          1
                # A     Haber            20
                # S     (space)          1
                # A     Concepto         100
                # S     (space)          1
                # A     IdSegNeg         4
                # S     (space)          1
                # A     Guid             36
                # S     (space)          1
                # A     FechaAplicacion  8         yyyyMMdd
                FieldDefinition(0, 2, 'str', 'id', 'Tipo de registro'),
                FieldDefinition(3, 30, 'str', 'cuenta', 'Cuenta'),
                FieldDefinition(34, 30, 'str', 'referencia', 'Referencia'),
                FieldDefinition(65, 1, 'str', 'tipo_movto', 'Tipo Movimiento 1,0'),
                FieldDefinition(67, 20, 'float', 'debe', 'Debe'),
                FieldDefinition(88, 10, 'str', 'id_diario', 'ID Diario'),
                FieldDefinition(99, 20, 'float', 'haber', 'Haber'),
                FieldDefinition(120, 100, 'str', 'concepto', 'Concepto'),
                FieldDefinition(221, 4, 'str', 'id_seg_neg', 'ID Segmento Negocio'),
                FieldDefinition(226, 36, 'str', 'guid', 'GUID'),
                FieldDefinition(263, 8, 'str', 'fecha_aplicacion', 'Fecha Aplicación yyyyMMdd')
            ]
        )
