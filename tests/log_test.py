''' tests the log class of MAT '''
from src import log

class LogTest:

    def __init__(self):
        print('\n\n***BEGIN LOG TESTS***')
        self.logger = log.Log('example.com')
        self.test_data = b'x'*1000

    def test_all(self):
        if self.test_log_response() and self.test_log_cookies():
            print('SUCCESS: all log tests passed')
        else:
            print('FAIL: some log tests failed')

        print('***END LOG TESTS***\n\n')

    def test_log_response(self):
        try:
            assert self.logger.log_response(self.test_data) > 0, \
                'response log is empty'
            return True
        except AssertionError as e:
            print(e.message)
            return False

    def test_log_cookies(self):
        try:
            assert self.logger.log_cookies(self.test_data) > 0, \
                'cookie log is empty'
            return True
        except AssertionError as e:
            print(e.message)
            return False
