from database.hard_drive import HardDrive

class Member:
    """ Daten von einem Kunden """
    def __init__(self, json):
        self._data = json
        # Test variable
        self.test_member = {
            'first-name': 'Max',
            'last-name': 'Helmut',
            'member-birthday': '16.09.2005',
            'parent-1-first-name': 'Eduard',
            'parent-1-last-name': 'Helmut',
            'parent-2-first-name': 'Marina',
            'parent-2-last-name': 'Helmut',
            'abo-category': 0,
            'abo-cycle': 6,
            'entry-date': '01.01.2000',
            'cancellation-date': '',
            'exit-date': '',
            'street': 'Teststr',
            'housenumber': '10',
            'city': 'Schwelm',
            'zip-code': '12345',
            'contact-number': '0160/12345678',
            'email': 'test.test@test.test',
            'health-problems': ''
        }


