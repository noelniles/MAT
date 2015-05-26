'''
import pycurl
import matconf
'''


class Mat():

    ''' directory for current scan output '''
    outdir = ''

    ''' dict of files to store responses from target'''
    respfile = {}

    ''' logs the responses from the curl '''
    def log_response():
        return True

    ''' sends data to the target '''
    def send_data():
        return True

    ''' logs the cookies sent to our machine from the target '''
    def log_cookies():
        return True
