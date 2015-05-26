''' test the request class of MAT '''
import request


class RequestTest:

    ''' set up request tests '''
    def __init__(self):
        self.req = request.Request()

    def test_snd(self):
        test_ua = 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)'
        test_target = 'http://live.com'
        self.req.snd(test_ua, test_target)

    def test_sndall(self):
        self.req.sndall()
