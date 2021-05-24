import unittest
from database.hard_drive import HardDrive


class TestHardDrive(unittest.TestCase):

    def setUp(self) -> None:
        d = {
            'string': 'string',
            'int': 1,
            'float': 0.5,
            'array': ['0', 1, 1.5],
            'dict': {'content': 'someone'}
        }
        HardDrive.save(d, 'test.json')
        self.loaded_dict = HardDrive.load('test.json')

    def test_HardDrive(self):
        self.assertEqual(self.loaded_dict[''], None)




if __name__ == '__main_':
    unittest.main()





