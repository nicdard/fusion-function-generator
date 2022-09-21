import unittest

from ffg.gen.tree_generation import generate_tree


class TestRegressions(unittest.TestCase):
    def testGeneratorCompatibility(self):
        # it is sufficient to parse the code to replicate the issue.
        pass
