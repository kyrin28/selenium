# -*- coding:UTF-8 -*-
import os
import unittest
from utils.HTMLTestRunner3 import HTMLTestRunner
from src.search_products_cls_test import ProductTests


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

prod_test = unittest.TestLoader().loadTestsFromTestCase(ProductTests)
suit_tests = unittest.TestSuite([prod_test])

out_file = open(base_dir + '/logs/report.html', 'wb')
runner = HTMLTestRunner(stream=out_file, title='Test Report', description='production test')
runner.run(suit_tests)
