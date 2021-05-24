import unittest
from database.hard_drive import HardDrive
from database.member import Member


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
        self.assertEqual(self.loaded_dict['string'], 'string')
        self.assertEqual(self.loaded_dict['int'], 1)
        self.assertEqual(self.loaded_dict['float'], 0.5)
        self.assertEqual(self.loaded_dict['array'], ['0', 1, 1.5])
        self.assertEqual(self.loaded_dict['dict'], {'content': 'someone'})



class TestMember(unittest.TestCase):

    def setUp(self) -> None:
        d = HardDrive.load('./members/0.json')
        self.member = Member(d)

    def testMember(self):
        self.assertTrue(type(self.member.get_first_name()) is str)
        self.assertTrue(type(self.member.get_first_name(1)) is str)
        self.assertTrue(type(self.member.get_first_name(2)) is str)
        self.assertTrue(type(self.member.get_last_name()) is str)
        self.assertTrue(type(self.member.get_last_name(1)) is str)
        self.assertTrue(type(self.member.get_last_name(2)) is str)
        self.assertTrue(type(self.member.get_birthday()) is str)
        self.assertTrue(type(self.member.get_abo_category()) is int)
        self.assertTrue(type(self.member.get_abo_cycle()) is int)
        self.assertTrue(type(self.member.get_entry_date()) is str)
        self.assertTrue(type(self.member.get_cancellation_date()) is str)
        self.assertTrue(type(self.member.get_exit_date()) is str)
        self.assertTrue(type(self.member.get_street()) is str)
        self.assertTrue(type(self.member.get_housenumber()) is str)
        self.assertTrue(type(self.member.get_city()) is str)
        self.assertTrue(type(self.member.get_zip_code()) is str)
        self.assertTrue(type(self.member.get_contact_number()) is str)
        self.assertTrue(type(self.member.get_email()) is str)
        self.assertTrue(type(self.member.get_health_problem()) is str)

if __name__ == '__main_':
    unittest.main()





