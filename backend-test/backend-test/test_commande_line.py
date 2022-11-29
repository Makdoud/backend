import unittest
from collections import namedtuple
from command_line import main

class TestMycommand_line(unittest.TestCase):

    args=['--filter=ry','--count']

    def test_filter(self):
        args = TestMycommand_line.args[0]
        print(args)
        res = main(args)
      

    def test_count(self):
        args = TestMycommand_line.args[1]
        res = main(args)
       

if __name__ == '__main__':
    unittest.main()