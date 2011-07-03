#-*- coding:utf-8 -*-
from should_dsl import should, should_not
import unittest

from trabalho_1.bl import BancoLogico

class TestRenda(unittest.TestCase):
    def test_renda_inadequada(self):
        bl = BancoLogico()

        dependentes = 1
        ganhos = 18999
        bl.renda(dependentes, ganhos) |should| equal_to(bl.INADEQUADA)
        ganhos = 19000
        bl.renda(dependentes, ganhos) |should_not| equal_to(bl.INADEQUADA)
        ganhos = 19001
        bl.renda(dependentes, ganhos) |should_not| equal_to(bl.INADEQUADA)

        dependentes = 2
        ganhos = 22999
        bl.renda(dependentes, ganhos) |should| equal_to(bl.INADEQUADA)
        ganhos = 23000
        bl.renda(dependentes, ganhos) |should_not| equal_to(bl.INADEQUADA)
        ganhos = 23001
        bl.renda(dependentes, ganhos) |should_not| equal_to(bl.INADEQUADA)

        dependentes = 3
        ganhos = 26999
        bl.renda(dependentes, ganhos) |should| equal_to(bl.INADEQUADA)
        ganhos = 27000
        bl.renda(dependentes, ganhos) |should_not| equal_to(bl.INADEQUADA)
        ganhos = 27001
        bl.renda(dependentes, ganhos) |should_not| equal_to(bl.INADEQUADA)

    def test_renda_adequada(self):
        bl = BancoLogico()

        dependentes = 1
        ganhos = 18999
        bl.renda(dependentes, ganhos) |should_not| equal_to(bl.ADEQUADA)
        ganhos = 19000
        bl.renda(dependentes, ganhos) |should| equal_to(bl.ADEQUADA)
        ganhos = 19001
        bl.renda(dependentes, ganhos) |should| equal_to(bl.ADEQUADA)

        dependentes = 2
        ganhos = 22999
        bl.renda(dependentes, ganhos) |should_not| equal_to(bl.ADEQUADA)
        ganhos = 23000
        bl.renda(dependentes, ganhos) |should| equal_to(bl.ADEQUADA)
        ganhos = 23001
        bl.renda(dependentes, ganhos) |should| equal_to(bl.ADEQUADA)

        dependentes = 3
        ganhos = 26999
        bl.renda(dependentes, ganhos) |should_not| equal_to(bl.ADEQUADA)
        ganhos = 27000
        bl.renda(dependentes, ganhos) |should| equal_to(bl.ADEQUADA)
        ganhos = 27001
        bl.renda(dependentes, ganhos) |should| equal_to(bl.ADEQUADA)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestRenda)
    unittest.TextTestRunner(verbosity=2).run(suite)

