''' manages the list of suspected malware hosts for MAT

    The list is a dummy filled with safe URLs for use during development
'''
import matconf
import pprint


class Mal:

    targets = []

    ''' calls parse_bad_file to set up the targets dict '''
    def __init__(self):
        self.parse_badfile(matconf.BADFILE)

    def parse_badfile(self, badfile):

        with open(badfile) as f:
            for line in f:
                self.targets.append(line.rstrip())

    def list_badguys(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.targets)
        return True
