from .base import LayoutProvider, LineLayout, FieldDefinition

#validated positioning
class Poliza1Layout(LayoutProvider):
    """Provider for the Poliza 1 (P) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='P',
            description='Póliza 1',
            fields=[
                # Layout specification:
                # Layout based on field definition table:
                # Tipo  Nombre    Longitud  Formato
                # E     poliza.1   2         P
                # S     (space)    1
                # A     Fecha      8         yyyyMMdd
                # S     (space)    1
                # A     TipoPol    4
                # S     (space)    1
                # A     Folio      9         # Changed from 3 to 9
                # S     (space)    1
                # A     Clase      1
                # S     (space)    1
                # A     IdDiario   10
                # S     (space)    1
                # A     Concepto   100
                # A     SistOrig   3
                # S     (space)    1
                # A     Impresa    1         1,0
                # S     (space)    1
                # A     Ajuste     1         1,0
                # S     (space)    1
                # A     Guid       36
                # S     (space)    1
                FieldDefinition(0, 2, 'str', 'id', 'Tipo de registro'),
                FieldDefinition(3, 8, 'str', 'fecha', 'Fecha yyyyMMdd'),
                FieldDefinition(12, 4, 'str', 'tipo_pol', 'Tipo de póliza'),
                FieldDefinition(17, 9, 'str', 'folio', 'Folio'),  # Changed length to 9
                FieldDefinition(27, 1, 'str', 'clase', 'Clase'),  # Updated position
                FieldDefinition(29, 10, 'str', 'id_diario', 'ID Diario'),  # Updated position
                FieldDefinition(40, 100, 'str', 'concepto', 'Concepto'),  # Updated position
                FieldDefinition(140, 3, 'str', 'sist_orig', 'Sistema Origen'),  # Updated position
                FieldDefinition(144, 1, 'float', 'impresa', 'Impresa 1,0'),  # Updated position
                FieldDefinition(146, 1, 'float', 'ajuste', 'Ajuste 1,0'),  # Updated position
                FieldDefinition(148, 36, 'str', 'guid', 'GUID')  # Updated position
            ]
        )
