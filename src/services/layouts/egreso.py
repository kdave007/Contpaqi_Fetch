from .base import LayoutProvider, LineLayout, FieldDefinition


class EgresoLayout(LayoutProvider):
    """Provider for the Egreso (EG) layout"""
    def get_layout(self) -> LineLayout:
        return LineLayout(
            identifier='EG',
            description='Egreso',
            fields=[
                FieldDefinition(0, 2, 'str', 'egreso', 'Tipo de registro'),
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
                FieldDefinition(348, 30, 'str', 'banco_destino', 'Banco Destino'),
                FieldDefinition(378, 30, 'str', 'cuenta_destino', 'Cuenta Destino'),
                FieldDefinition(408, 5, 'str', 'otro_metodo_pago', 'Otro Método de Pago'),
                FieldDefinition(413, 36, 'str', 'guid', 'GUID'),
                FieldDefinition(449, 13, 'str', 'rfc', 'RFC'),
                FieldDefinition(462, 20, 'float', 'tipo_cambio', 'Tipo Cambio'),
                FieldDefinition(482, 36, 'str', 'uuid_rep', 'UUID Rep'),
                FieldDefinition(518, 3, 'str', 'nodo_pago', 'Nodo Pago'),
                FieldDefinition(521, 4, 'str', 'codigo_moneda_tipo_cambio', 'Código Moneda Tipo Cambio'),
                FieldDefinition(525, 5, 'str', 'num_asoc', 'Número Asociación')
            ]
        )
