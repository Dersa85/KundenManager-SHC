import unittest
from database import hard_drive


class TestHardDrive(unittest.TestCase):


    def test_load(self):
        drive = hard_drive.HardDrive()
        self.assertEqual(drive.load('members/0.json'), None)




if __name__ == '__main_':
    unittest.main()





