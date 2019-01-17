# -*- coding:UTF-8 -*-

import unittest
from src.search_products_cls_test import ProductTests

prod_test = unittest.TestLoader().loadTestsFromTestCase(ProductTests)
suit_tests = unittest.TestSuite([prod_test])

unittest.TextTestRunner(verbosity=2).run(suit_tests)

