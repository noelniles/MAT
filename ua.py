''' user agent class for MAT '''
import pprint
import matconf


class UA():

    ''' dict of user agents to spoof '''
    ua = {}

    ''' fills the user agent dictionary '''
    def __init__(self):
        self.parse_ua_file(matconf.UAF)

    ''' grabs the user agents from the file fname '''
    def parse_ua_file(self, fname):
        with open(fname) as f:
            for line in f:
                if (line[0] == '['):
                    ua_name = line[1:-2]
                    ua_string = next(f)
                self.ua[ua_name] = ua_string
        return True

    def list_user_agents(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.ua)
        return True
