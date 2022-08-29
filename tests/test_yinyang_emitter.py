import unittest
import tempfile

from ffg.emitter import yinyang_emitter
from ffg.operators.boolean_theory import *
from ffg.visitors.initialization_visitor import InitializationVisitor


class TestYinYangEmitter(unittest.TestCase):
    def test_function_emission_easy(self):
        tree = BooleanEquality(BooleanVariable(), BooleanXor(
            BooleanVariable(), BooleanVariable()))
        tree.accept(InitializationVisitor(['x', 'y'], 'z'))

        with tempfile.TemporaryFile('r+') as file:
            yinyang_emitter.emit_function(tree, file)
            file.seek(0)
            self.assertEqual("#begin\n"
                             "(declare-const x Bool)\n"
                             "(declare-const y Bool)\n"
                             "(declare-const z Bool)\n"
                             "(assert (= z (xor x y)))\n"
                             "(assert (= x (xor y z)))\n"
                             "(assert (= y (xor x z)))\n"
                             "#end\n\n", file.read())
