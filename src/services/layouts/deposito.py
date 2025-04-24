from .base import LayoutProvider, LineLayout, FieldDefinition


class DepositoLayout(LayoutProvider):
    """Provider for the Deposito (DE) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='DE',
            description='Depósito',
            fields=[
                FieldDefinition(0, 2, 'str', 'deposito', 'Tipo de registro'),
                FieldDefinition(2, 5, 'str', 'id_documento_de', 'ID Documento De'),
                FieldDefinition(7, 30, 'str', 'tipo_documento', 'Tipo Documento'),
                FieldDefinition(37, 20, 'str', 'folio', 'Folio'),
                FieldDefinition(57, 8, 'date', 'fecha', 'Fecha yyyyMMdd'),
                FieldDefinition(65, 4, 'str', 'ejercicio', 'Ejercicio'),
                FieldDefinition(69, 2, 'str', 'periodo', 'Periodo'),
                FieldDefinition(71, 8, 'date', 'fecha_aplicacion', 'Fecha Aplicación yyyyMMdd'),
                FieldDefinition(79, 4, 'str', 'ejercicio_ap', 'Ejercicio Aplicación'),
                FieldDefinition(83, 2, 'str', 'periodo_ap', 'Periodo Aplicación'),
                FieldDefinition(85, 20, 'str', 'id_cuenta_cheques', 'ID Cuenta Cheques'),
                FieldDefinition(105, 1, 'str', 'nat_bancaria', 'Naturaleza Bancaria'),
                FieldDefinition(106, 1, 'str', 'naturaleza', 'Naturaleza'),
                FieldDefinition(107, 20, 'float', 'total', 'Total'),
                FieldDefinition(127, 20, 'str', 'referencia', 'Referencia'),
                FieldDefinition(147, 100, 'str', 'concepto', 'Concepto'),
                FieldDefinition(247, 1, 'float', 'es_conciliado', 'Es Conciliado 1,0'),
                FieldDefinition(248, 10, 'str', 'id_mov_edo_cta', 'ID Movimiento Estado Cuenta'),
                FieldDefinition(258, 4, 'str', 'ejercicio_pol', 'Ejercicio Póliza'),
                FieldDefinition(262, 2, 'str', 'periodo_pol', 'Periodo Póliza'),
                FieldDefinition(264, 10, 'str', 'tipo_pol', 'Tipo Póliza'),
                FieldDefinition(274, 10, 'str', 'num_pol', 'Número Póliza'),
                FieldDefinition(284, 1, 'str', 'forma_deposito', 'Forma Depósito'),
                FieldDefinition(285, 10, 'str', 'id_poliza', 'ID Póliza'),
                FieldDefinition(295, 5, 'str', 'origen', 'Origen'),
                FieldDefinition(300, 10, 'str', 'id_documento', 'ID Documento'),
                FieldDefinition(310, 1, 'float', 'poliza_agrupada', 'Póliza Agrupada 1,0'),
                FieldDefinition(311, 20, 'str', 'usuario_crea', 'Usuario Crea'),
                FieldDefinition(331, 20, 'str', 'usuario_modifica', 'Usuario Modifica'),
                FieldDefinition(351, 1, 'float', 'tiene_cfd', 'Tiene CFD 1,0'),
                FieldDefinition(352, 36, 'str', 'guid', 'GUID')
            ]
        )
