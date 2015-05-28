''' makes request to a suspected malware host '''
import io
import pycurl

from conf import matconf
from src import log
from src import mal


class Request:

    ''' sets up the target list and the list of user agent strings '''
    def __init__(self, verbosity=1):
        self.verbosity = verbosity
        self.mal = mal.Mal()
        self.target_list = self.mal.targets
        self.ua_str = matconf.UA
        self.head = ['User-Agent: ' + self.ua_str,
                     'Accept:',
                     'Accept-Language: en-US,en;q=0.5',
                     'Accept-Encoding: gzip, deflate',
                     'DNT: 0',
                     'Referer: https://mail.google.com/mail/u/0/#inbox',
                     'Connection: keep-alive',
                     'Cache-Control: max-age=0']

    ''' sends to all targets in badfile.txt '''
    def sndall(self):
        for target_url in self.target_list:
            self.snd(self.ua_str, target_url)

    ''' sends a request to the target URL '''
    def snd(self, ua, target_url):

        ''' buffer for the response '''
        buf = io.BytesIO()

        ''' inits a curl handle '''
        c = pycurl.Curl()

        ''' sets the target '''
        c.setopt(pycurl.URL, target_url)

        ''' sets the custom header '''
        c.setopt(pycurl.HTTPHEADER, self.head)

        ''' turns on verbosity '''
        c.setopt(pycurl.VERBOSE, self.verbosity)

        ''' do not verify server ssl cert '''
        c.setopt(pycurl.SSL_VERIFYPEER, 0)

        ''' follow http redirects '''
        c.setopt(pycurl.FOLLOWLOCATION, 1)

        ''' sets the buf as storage for the response '''
        c.setopt(c.WRITEDATA, buf)

        try:
            ''' ATTACK! '''
            c.perform()
        except pycurl.error as e:
            'an error occured %s' % e

        ''' close it up '''
        c.close()

        body = buf.getvalue()

        ''' log the response '''
        self.log = log.Log(target_url)
        self.log.log_response(body)
