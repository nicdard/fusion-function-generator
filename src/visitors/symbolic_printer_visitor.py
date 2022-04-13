from src.operators.boolean_theory import BooleanConstant
from src.operators.integer_theory import IntegerConstant
from src.operators.real_theory import RealConstant
from src.visitors.printer_visitor import PrinterVisitor


class SymbolicPrinterVisitor(PrinterVisitor):
    def visit_boolean_constant(self, operator: BooleanConstant):
        return operator.name

    def visit_integer_constant(self, operator: IntegerConstant):
        return operator.name

    def visit_real_constant(self, operator: RealConstant):
        return operator.name
