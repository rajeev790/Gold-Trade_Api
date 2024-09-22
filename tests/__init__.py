import unittest

# You can include any setup or teardown code for your tests here
# For example, you might set up a test database or configure test logging

def run_tests():
    """
    Run all the unit tests in the tests directory.
    """
    # Discover and run all tests
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_tests()
