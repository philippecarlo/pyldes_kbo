import unittest

from pyldes_kbo.automation.tests.kbo_pagination_default import TestDefaultPagination as DefaultPagination
from pyldes_kbo.automation.tests.kbo_substring_default import TestDefaultSustring as DefaultSubstring
from pyldes_kbo.automation.tests.kbo_notreepath_pagination import TestNoPathSubstring as NoPathSubstring

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(DefaultPagination)
    suite = loader.loadTestsFromTestCase(DefaultSubstring)
    suite = loader.loadTestsFromTestCase(NoPathSubstring)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

#to run under current directory e.g. .\conformanceTesting\pyldes_kbo\automation\tests
#pytest -s runall.py
