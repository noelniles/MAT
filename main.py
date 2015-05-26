'''
import log
import matconf
import ua
'''
from tests import log_test
from tests import ua_test
from tests import request_test

def main():

    ''' tests logs '''
    logtester = log_test.LogTest()
    logtester.test_log_response()
    logtester.test_log_cookies()

    ''' tests user agents '''
    uatester = ua_test.UATest()
    uatester.test_list_agents()

    ''' tests request '''
    request_tester = request_test.RequestTest()
    request_tester.test_snd()
    request_tester.test_sndall()

if __name__ == '__main__':
    main()
