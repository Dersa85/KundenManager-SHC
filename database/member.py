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

    def _import(self, dictonary):
        self._data = {
            'first-name': dictonary.get('first-name', ''),
            'last-name': dictonary.get('last-name', ''),
            'member-birthday': '16.09.2005',
            'parent-1-first-name': 'Eduard',
            'parent-1-last-name': 'Helmut',
            'parent-2-first-name': 'Marina',
            'parent-2-last-name': 'Helmut',
            'abo-category': dictonary.get('abo-category', -1),
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

    def get_first_name(self, parent=0):
        """ parent = 0 bedeutet das es vom Member gewollt ist.
            parent = 1 währe dann von ersten Elternteil
            parent = 2 währe dann von ersten Elternteil
        """
        return

    def get_last_name(self, parent=0):
        """ parent = 0 bedeutet das es vom Member gewollt ist.
            parent = 1 währe dann von ersten Elternteil
            parent = 2 währe dann von ersten Elternteil
        """
        return

    def get_birthday(self):
        return

    def get_abo_category(self):
        return

    def get_abo_cycle(self):
        return

    def get_entry_date(self):
        return

    def get_cancellation_date(self):
        return

    def get_exit_date(self):
        return

    def get_street(self):
        return

    def get_housenumber(self):
        return

    def get_city(self):
        return

    def get_zip_code(self):
        return

    def get_contact_number(self):
        return

    def get_email(self):
        return

    def get_health_problem(self):
        return

