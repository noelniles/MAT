''' logging class for MAT '''
import os
import time

from conf import matconf

class Log:

    ''' creates the log file path if it doesn't exist '''
    def make_sure_path_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def __init__(self, target_name):
        self.logdirname = target_name.replace('http://', '')
        self.logtime = time.strftime("%Y%m%d-%H%M%S")
        self.logpath = os.path.join(matconf.OUTD, self.logdirname)
        self.make_sure_path_exists(self.logpath)

    ''' returns -1 on failure and size of data on success '''
    def log_response(self, data):

        data_size = -1

        logname = '%s_response.log' % self.logtime
        response_log = os.path.join(self.logpath, logname)

        try:
            with open(response_log, "wb") as out_file:
                data_size = out_file.write(data)
                print('wrote %s bytes to %s' % (data_size, response_log))
        except IOError as e:
            print('error logging response: %s' % e.errno)

        return data_size

    def log_cookies(self, data):

        ''' return code -1 for failure; byte size of data on success '''
        data_size = -1

        logname = '%s_cookies.log' % self.logtime
        cookies_log = os.path.join(self.logpath, logname)

        try:
            with open(cookies_log, "wb") as out_file:
                data_size = out_file.write(data)
                print('wrote %s bytes to %s' % (data_size, cookies_log))
        except IOError as e:
            print('error logging response: %s' % e.errno)

        return data_size
