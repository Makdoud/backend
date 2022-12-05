import unittest
from command_line import main



class TestMycommand_line(unittest.TestCase):

    def test_filter(self):
        parser = main(['--filter=ry'])
        self.assertListEqual(parser, [{'name': 'Uzuzozne', 'people': [{'name': 'Lillie Abbott', 'animals': [{'name': 'John Dory'}]}]}, {'name': 'Satanwi', 'people': [{'name': 'Anthony Bruno', 'animals': [{'name': 'Oryx'}]}]}])    

    def test_count(self):
        parser = main(['--count'])
        self.assertListEqual(parser, [{'name': 'Uzuzozne [2]', 'people': [{'name': 'Lillie Abbott [1]', 'animals': [{'name': 'John Dory'}]}]}, {'name': 'Satanwi [2]', 'people': [{'name': 'Anthony Bruno [1]', 'animals': [{'name': 'Oryx'}]}]}, {'name': 'Dillauti [16]', 'people': [{'name': 'Winifred Graham [6]', 'animals': [{'name': 'Anoa'}, {'name': 'Duck'}, {'name': 'Narwhal'}, {'name': 'Badger'}, {'name': 'Cobra'}, {'name': 'Crow'}]}, {'name': 'Blanche Viciani [8]', 'animals': [{'name': 'Barbet'}, {'name': 'Rhea'}, {'name': 'Snakes'}, {'name': 'Antelope'}, {'name': 'Echidna'}, {'name': 'Crow'}, {'name': 'Guinea Fowl'}, {'name': 'Deer Mouse'}]}]}])
       
    def test_arg_is_None(self):
        parser = main(None)
        self.assertIsNone(parser)

if __name__ == '__main__':
    unittest.main()
