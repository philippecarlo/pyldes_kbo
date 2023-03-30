from unittest import TestLoader, TextTestRunner, TestSuite
from pyldes_kbo.cegekaKBO.cegeka_kbo_pagination.kbo_pagination_default import   TestDefaultPagination
from pyldes_kbo.cegekaKBO.cegeka_kbo_substring.kbo_substring_default import TestDefaultSubstring
if __name__ == "__main__":

    loader = TestLoader()
    tests = [
        loader.loadTestsFromTestCase(test)
        for test in (TestDefaultPagination, TestDefaultSubstring)
    ]
    suite = TestSuite(tests)

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)