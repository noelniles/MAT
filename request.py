''' makes request to a suspected malware host '''
import io

import pycurl

import ua
import mal

class Request:


    ''' sets up the target list and the list of user agent strings '''
    def __init__(self):
        self.ua = ua.UA()
        self.mal = mal.Mal()
        self.target_list = self.mal.targets
        self.ua_list = self.ua.ua_strings

    ''' send to all the target in the bad file using all the user agents '''
    def sndall(self):
        for target in self.target_list:
            for uaname, ua in self.ua_list.items():
                print('sending request to %s with User Agent: %s'
                      % (target,uaname))
                self.snd(ua, target)

    ''' sends a request to the target with the user agent ua '''
    def snd(self, ua, target):
        buf = io.BytesIO()
        c = pycurl.Curl()

        ''' turns on verbosity '''
        c.setopt(pycurl.VERBOSE, 1)
        ''' sets the target '''
        c.setopt(pycurl.URL, target)

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
        print (body.decode('iso-8859-1'))
