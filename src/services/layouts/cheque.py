from .base import LayoutProvider, LineLayout, FieldDefinition


class ChequeLayout(LayoutProvider):
    """Provider for the Cheque (CH) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='CH',
            description='Cheque',
            fields=[
                FieldDefinition(0, 2, 'str', 'cheque', 'Tipo de registro'),
                FieldDefinition(2, 5, 'str', 'id_documento_de', 'ID Documento De'),
                FieldDefinition(7, 30, 'str', 'tipo_documento', 'Tipo Documento'),
                FieldDefinition(37, 20, 'str', 'folio', 'Folio'),
                FieldDefinition(57, 8, 'date', 'fecha', 'Fecha yyyyMMdd'),
                FieldDefinition(65, 8, 'date', 'fecha_aplicacion', 'Fecha Aplicación yyyyMMdd'),
                FieldDefinition(73, 6, 'str', 'codigo_persona', 'Código Persona'),
                FieldDefinition(79, 200, 'str', 'beneficiario_pagador', 'Beneficiario Pagador'),
                FieldDefinition(279, 20, 'str', 'id_cuenta_cheques', 'ID Cuenta Cheques'),
                FieldDefinition(299, 4, 'str', 'codigo_moneda', 'Código Moneda'),
                FieldDefinition(303, 20, 'float', 'total', 'Total'),
                FieldDefinition(323, 20, 'str', 'referencia', 'Referencia'),
                FieldDefinition(343, 5, 'str', 'origen', 'Origen'),
                FieldDefinition(348, 30, 'str', 'cuenta_destino', 'Cuenta Destino'),
                FieldDefinition(378, 5, 'str', 'banco_destino', 'Banco Destino'),
                FieldDefinition(383, 36, 'str', 'guid', 'GUID'),
                FieldDefinition(419, 13, 'str', 'rfc', 'RFC'),
                FieldDefinition(432, 5, 'str', 'otro_metodo_pago', 'Otro Método de Pago'),
                FieldDefinition(437, 20, 'float', 'tipo_cambio', 'Tipo Cambio'),
                FieldDefinition(457, 36, 'str', 'uuid_rep', 'UUID Rep'),
                FieldDefinition(493, 3, 'str', 'nodo_pago', 'Nodo Pago'),
                FieldDefinition(496, 4, 'str', 'codigo_moneda_tipo_cambio', 'Código Moneda Tipo Cambio'),
                FieldDefinition(500, 5, 'str', 'num_asoc', 'Número Asociación')
            ]
        )
