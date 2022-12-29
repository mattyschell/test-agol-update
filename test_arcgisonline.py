import os
import pathlib
import unittest

import arcgisonline


class ArcgisonlineUserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.AgolTxt = pathlib.Path(__file__).parent \
                                        .joinpath('AGOL_Publishing') \
                                        .joinpath('Data') \
                                        .joinpath('Other') \
                                        .joinpath('Agol.txt')

        with open(self.AgolTxt) as f:
            lines = f.read()

        self.user     = lines.split('\n')[0].split(',')[0]
        self.password = lines.split('\n')[0].split(',')[1]

        self.dummyuser = arcgisonline.User(self.user
                                          ,self.password)

    def test_agettoken(self):

        token = self.dummyuser.gettoken()
         
        # assert that we got back a long string of letters and numbers         
        self.assertGreater(len(token),10)
    

if __name__ == '__main__':
    unittest.main()