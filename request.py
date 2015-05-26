''' makes request to a suspected malware host '''
import io

import pycurl

import log
import mal
import ua


class Request:

    ''' sets up the target list and the list of user agent strings '''
    def __init__(self):
        self.ua = ua.UA()
        self.mal = mal.Mal()
        self.target_list = self.mal.targets
        self.ua_list = self.ua.ua_strings

    ''' sends to all targets in badfile.txt with all user agents '''
    def sndall(self):
        for target_url in self.target_list:
            for uaname, uastr in self.ua_list.items():
                print('sending request to %s with User Agent: %s'
                      % (target_url, uaname))
                self.snd(uastr, target_url)

    ''' sends a request to the target URL with the user agent ua '''
    def snd(self, ua, target_url):

        ''' starts the log '''
        log_name = target_url.replace('http://', '')
        log_name = target_url.replace('https://', '')
        self.log = log.Log(log_name)

        ''' buffer for the response '''
        buf = io.BytesIO()

        ''' inits a curl handle '''
        c = pycurl.Curl()

        ''' turns on verbosity '''
        c.setopt(pycurl.VERBOSE, 1)

        ''' force http v2 '''
        c.setopt(pycurl.HTTP_VERSION, 2)

        ''' sets the target '''
        c.setopt(pycurl.URL, target_url)

        ''' do not verify server ssl cert '''
        c.setopt(pycurl.SSL_VERIFYPEER, 0)

        ''' sets the referrer to gmail '''
        c.setopt(pycurl.REFERER, 'https://mail.google.com/mail/u/0/#inbox')

        ''' follow http redirects '''
        c.setopt(pycurl.FOLLOWLOCATION, 1)

        ''' sets the user agent '''
        c.setopt(pycurl.USERAGENT, ua)

        ''' sets the buf as storage for the response '''
        c.setopt(c.WRITEDATA, buf)

        ''' ATTACK! '''
        c.perform()

        ''' close it up '''
        c.close()

        body = buf.getvalue()

        ''' log the response '''
        self.log.log_response(body.decode('iso-8859-1'))
        print(body.decode('iso-8859-1'))
