''' user agent tests for MAT '''
import ua


class UATest:

    def __init__(self):
        ''' a user agent object see ua.py '''
        self.ua = ua.UA()

    def test_list_agents(self):
        self.ua.list_user_agents()
