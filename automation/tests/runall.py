import unittest

from pyldes_kbo.automation.tests.kbo_pagination_default import TestDefaultPagination as TestExample1
from pyldes_kbo.automation.tests.kbo_substring_default import TestDefaultSustring as TestExample2
from pyldes_kbo.automation.tests.kbo_notreepath_pagination import TestNoPathSubstring as TestExample3

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestExample1)
    suite = loader.loadTestsFromTestCase(TestExample2)
    suite = loader.loadTestsFromTestCase(TestExample3)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

#to run under current directory e.g. .\conformanceTesting\pyldes_kbo\automation\tests
#pytest -s runall.py
