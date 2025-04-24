from .base import LayoutProvider, LineLayout, FieldDefinition


class IngresosNoDepositadosLayout(LayoutProvider):
    """Provider for the Ingresos No Depositados (DI) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='DI',
            description='Ingresos No Depositados',
            fields=[
                FieldDefinition(0, 2, 'str', 'ingresos_no_depositados', 'Tipo de registro'),
                FieldDefinition(2, 5, 'str', 'id_documento_de', 'ID Documento De'),
                FieldDefinition(7, 30, 'str', 'tipo_documento', 'Tipo Documento'),
                FieldDefinition(37, 20, 'str', 'folio', 'Folio'),
                FieldDefinition(57, 8, 'date', 'fecha', 'Fecha yyyyMMdd'),
                FieldDefinition(65, 4, 'str', 'ejercicio', 'Ejercicio'),
                FieldDefinition(69, 2, 'str', 'periodo', 'Periodo'),
                FieldDefinition(71, 8, 'date', 'fecha_aplicacion', 'Fecha Aplicación yyyyMMdd'),
                FieldDefinition(79, 4, 'str', 'ejercicio_ap', 'Ejercicio Aplicación'),
                FieldDefinition(83, 2, 'str', 'periodo_ap', 'Periodo Aplicación'),
                FieldDefinition(85, 6, 'str', 'codigo_persona', 'Código Persona'),
                FieldDefinition(91, 200, 'str', 'beneficiario_pagador', 'Beneficiario Pagador'),
                FieldDefinition(291, 1, 'str', 'nat_bancaria', 'Naturaleza Bancaria'),
                FieldDefinition(292, 1, 'str', 'naturaleza', 'Naturaleza'),
                FieldDefinition(293, 4, 'str', 'codigo_moneda', 'Código Moneda'),
                FieldDefinition(297, 4, 'str', 'codigo_moneda_tipo_cambio', 'Código Moneda Tipo Cambio'),
                FieldDefinition(301, 20, 'float', 'tipo_cambio', 'Tipo Cambio'),
                FieldDefinition(321, 20, 'float', 'total', 'Total'),
                FieldDefinition(341, 20, 'str', 'referencia', 'Referencia'),
                FieldDefinition(361, 100, 'str', 'concepto', 'Concepto'),
                FieldDefinition(461, 1, 'float', 'es_asociado', 'Es Asociado 1,0'),
                FieldDefinition(462, 20, 'str', 'usu_autoriza_presupuesto', 'Usuario Autoriza Presupuesto'),
                FieldDefinition(482, 10, 'str', 'posibilidad_pago', 'Posibilidad Pago'),
                FieldDefinition(492, 1, 'float', 'es_proyectado', 'Es Proyectado 1,0'),
                FieldDefinition(493, 5, 'str', 'origen', 'Origen'),
                FieldDefinition(498, 10, 'str', 'id_cheque_origen', 'ID Cheque Origen'),
                FieldDefinition(508, 20, 'str', 'tipo_cambio_deposito', 'Tipo Cambio Depósito'),
                FieldDefinition(528, 10, 'str', 'id_documento', 'ID Documento'),
                FieldDefinition(538, 1, 'float', 'es_anticipo', 'Es Anticipo 1,0'),
                FieldDefinition(539, 1, 'float', 'es_traspasado', 'Es Traspasado 1,0'),
                FieldDefinition(540, 20, 'str', 'usuario_crea', 'Usuario Crea'),
                FieldDefinition(560, 20, 'str', 'usuario_modifica', 'Usuario Modifica'),
                FieldDefinition(580, 1, 'float', 'tiene_cfd', 'Tiene CFD 1,0'),
                FieldDefinition(581, 36, 'str', 'guid', 'GUID'),
                FieldDefinition(617, 50, 'str', 'cuenta_origen', 'Cuenta Origen'),
                FieldDefinition(667, 10, 'str', 'banco_origen', 'Banco Origen'),
                FieldDefinition(677, 2, 'str', 'otro_metodo_pago', 'Otro Método de Pago'),
                FieldDefinition(679, 100, 'str', 'numero_cheque', 'Número Cheque'),
                FieldDefinition(779, 5, 'str', 'num_asoc', 'Número Asociación')
            ]
        )
