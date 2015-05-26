''' tests the log class of MAT '''
import log


class LogTest:

    def __init__(self):
        self.logger = log.Log('example.com')
        self.test_data = 'x'*1000

    ''' test the response logger '''
    def test_log_response(self):
        self.logger.log_response(self.test_data)

    ''' test the cookie logger '''
    def test_log_cookies(self):
        self.logger.log_cookies(self.test_data)
