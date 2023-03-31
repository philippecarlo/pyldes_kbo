import unittest

from pyldes_kbo.automation.tests.kbo_pagination_default import TestDefaultPagination as TestExample2
from pyldes_kbo.automation.tests.kbo_substring_default import TestDefaultSustring as TestExample1

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestExample1)
    suite = loader.loadTestsFromTestCase(TestExample2)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

#to run under current directory
#pytest -s test_example.py