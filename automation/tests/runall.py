import unittest

from pyldes_kbo.automation.tests.kbo_pagination_default import TestDefaultPagination as DefaultPagination
from pyldes_kbo.automation.tests.kbo_substring_default import TestDefaultSubstring as DefaultSubstring
from pyldes_kbo.automation.tests.kbo_notreepath_pagination import TestNoPathSubstring as NoPathSubstring
from pyldes_kbo.automation.tests.kbo_geofragment_default import TestDefaultGeoFragment as DefaultGeoFragment
# from pyldes_kbo.automation.tests.kbo_timebased_default import TestDefaultTimebase as DefaultTimebase
from pyldes_kbo.automation.tests.kbo_multiview_default import TestDefaultMultiview as DefaultMultiview

if __name__ == '__main__':
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromTestCase(DefaultPagination)
    suite = loader.loadTestsFromTestCase(DefaultSubstring)
    # suite = loader.loadTestsFromTestCase(NoPathSubstring)
    suite = loader.loadTestsFromTestCase(DefaultGeoFragment)
    # suite = loader.loadTestsFromTestCase(DefaultTimebase)
    suite = loader.loadTestsFromTestCase(DefaultMultiview)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

#to run under current directory e.g. .\conformanceTesting\pyldes_kbo\automation\tests
#pytest -s runall.py
