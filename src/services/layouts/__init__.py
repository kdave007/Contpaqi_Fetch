from .base import FieldDefinition, LineLayout, LayoutProvider
from .registry import LayoutRegistry
from .poliza_1 import Poliza1Layout
from .poliza_2 import Poliza2Layout
from .movimiento import MovimientoLayout
from .movimiento_cfd import MovimientoCFDLayout
from .movto_poliza import MovtoPolizaLayout
from .causacion_1 import Causacion1Layout
from .causacion_2 import Causacion2Layout
from .causacion_3 import Causacion3Layout
from .periodo_causacion import PeriodoCausacionLayout
from .devolucion import DevolucionLayout
from .devolucion_1 import Devolucion1Layout
from .devolucion_2 import Devolucion2Layout
from .asoc_docto import AsocDoctoLayout
from .asoc_movto import AsocMovtoLayout
from .cheque import ChequeLayout
from .egreso import EgresoLayout
from .ingreso import IngresoLayout
from .deposito import DepositoLayout
from .ingresos_no_depositados import IngresosNoDepositadosLayout
from .asoc_nodo_pago import AsocNodoPagoLayout
from .dispersion_pago import DispersionPagoLayout

# Create and configure the registry
registry = LayoutRegistry()
registry.register_layout('P', Poliza1Layout().get_layout())
registry.register_layout('FE', Poliza2Layout().get_layout())
registry.register_layout('M', MovimientoLayout().get_layout())
registry.register_layout('MC', MovimientoCFDLayout().get_layout())
registry.register_layout('M1', MovtoPolizaLayout().get_layout())
registry.register_layout('C', Causacion1Layout().get_layout())
registry.register_layout('D', Causacion2Layout().get_layout())
registry.register_layout('E', Causacion3Layout().get_layout())
registry.register_layout('R', PeriodoCausacionLayout().get_layout())
registry.register_layout('V', Devolucion1Layout().get_layout())
registry.register_layout('W', DevolucionLayout().get_layout())
registry.register_layout('W2', Devolucion2Layout().get_layout())
registry.register_layout('AD', AsocDoctoLayout().get_layout())
registry.register_layout('AM', AsocMovtoLayout().get_layout())
registry.register_layout('CH', ChequeLayout().get_layout())
registry.register_layout('EG', EgresoLayout().get_layout())
registry.register_layout('IN', IngresoLayout().get_layout())
registry.register_layout('DE', DepositoLayout().get_layout())
registry.register_layout('DI', IngresosNoDepositadosLayout().get_layout())
registry.register_layout('AP', AsocNodoPagoLayout().get_layout())
registry.register_layout('DP', DispersionPagoLayout().get_layout())

def get_layout_for_line(line: str):
    """Helper function to get the layout for a specific line"""
    return registry.get_layout(line)