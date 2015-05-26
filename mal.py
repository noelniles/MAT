''' manages the list of suspected malware hosts for MAT

    The list is a dummy filled with safe URLs for use during development
'''
import matconf


class Mal:

    targets = {}

    ''' calls parse_bad_file to set up the targets dict '''
    def __init__(self):
        self.parse_badfile(matconf.BADFILE)

    def parse_badfile(self, badfile):

        with open(badfile) as f:
            for line in f:
                if line[0] == '[':
                    target_name = line[1:-2]
                    target_url = next(f)
                self.targets[target_name] = target_url
