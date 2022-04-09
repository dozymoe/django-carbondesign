from django.test import TransactionTestCase
from django.test.runner import DiscoverRunner
from unittest.suite import TestSuite


class IntegrationTestRunner(DiscoverRunner):

    def build_suite(self, *args, **kwargs):
        suite = super().build_suite(*args, **kwargs)
        tests = [t for t in suite._tests if self.filter(t)]
        return TestSuite(tests=tests)

    def filter(self, test):
        return issubclass(test.__class__, TransactionTestCase)


class UnitTestRunner(DiscoverRunner):

    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass

    def build_suite(self, *args, **kwargs):
        suite = super().build_suite(*args, **kwargs)
        tests = [t for t in suite._tests if self.filter(t)]
        return TestSuite(tests=tests)

    def filter(self, test):
        return not issubclass(test.__class__, TransactionTestCase)
