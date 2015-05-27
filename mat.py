#!/usr/bin/env python

import argparse
from tests import log_test
from tests import request_test
import request


class Mat():

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Analyze malicious responses.')
        self.parser.add_argument('-t', '--test', nargs=1,
                                 help='run a single test')
        self.parser.add_argument('-T', '--test-all', help='run all tests',
                                 action='store_true')
        self.parser.add_argument('-v', '--verbose',
                                 help="increase verbosity of curl",
                                 action='store_true')
        self.args = self.parser.parse_args()

    def run_test(self, test='all'):
        if test == 'logs':
            logtest = log_test.LogTest()
            logtest.test_all()

        elif test == 'request':
            req_test = request_test.RequestTest()
            req_test.test_all()

        elif test == 'all':
            logtest = log_test.LogTest()
            logtest.test_all()
            req_test = request_test.RequestTest()
            req_test.test_all()

        else:
            print('test: <%s> is not implemented' % test)

    def run_mat(self, verbosity=0):
        print('MAT has started reaching out to the bad guys')
        m = request.Request()
        m.sndall()

    def main(self):
        if self.args.test:
            test = self.args.test[0]
            self.run_test(test)
        elif self.args.test_all:
            self.run_test()
        elif self.args.verbose:
            self.run_mat(1)
        else:
            self.run_mat()

        return True

if __name__ == '__main__':
    mat = Mat()
    mat.main()
