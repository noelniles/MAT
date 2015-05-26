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
        self.target_name = target_name
        self.target_log = os.path.join(matconf.OUTD, self.target_name)

    ''' log the response '''
    def log_response(self):
        logname = '%s_response.log' % self.logtime
        response_log = os.path.join(self.target_log, logname)
        self.make_sure_path_exists(response_log)
        return True

    ''' log the cookies '''
    def log_cookies(self):
        logname = '%s_cookies.log' % self.logtime
        cookies_log = os.path.join(self.target_log, logname)
        self.make_sure_path_exists(cookies_log)
        return True
