''' logging class for MAT '''
import matconf
import os
import time


class Log:
    def make_sure_path_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def __init__(self, target_name):
        self.logtime = time.strftime("%Y%m%d-%H%M%S")
        self.logpath = os.path.join(matconf.OUTD, target_name)
        self.make_sure_path_exists(self.logpath)

    ''' log the response '''
    def log_response(self, data):
        logname = '%s_response.log' % self.logtime
        response_log = os.path.join(self.logpath, logname)

        with open(response_log, "wt") as out_file:
            out_file.write(data)
            print('file written to %s' % response_log)

        return True

    ''' log the cookies '''
    def log_cookies(self, data):
        logname = '%s_cookies.log' % self.logtime
        cookies_log = os.path.join(self.logpath, logname)

        with open(cookies_log, "wt") as out_file:
            out_file.write(data)
            print('file written to %s' % cookies_log)

        return True
