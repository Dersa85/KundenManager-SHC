from database.hard_drive import HardDrive

class Member:
    """ Daten von einem Kunden """
    def __init__(self, json):
        self._data = self._import(json)


    def _import(self, dictonary):
        return {
            'first-name': dictonary.get('first-name', ''),
            'last-name': dictonary.get('last-name', ''),
            'member-birthday': dictonary.get('member-birthday', ''),
            'parent-1-first-name': dictonary.get('parent-1-first-name', ''),
            'parent-1-last-name': dictonary.get('parent-1-last-name', ''),
            'parent-2-first-name': dictonary.get('parent-2-first-name', ''),
            'parent-2-last-name': dictonary.get('parent-2-last-name', ''),
            'abo-category': dictonary.get('abo-category', -1),
            'abo-cycle': dictonary.get('abo-cycle', -1),
            'entry-date': dictonary.get('entry-date', ''),
            'cancellation-date': dictonary.get('cancellation-date', ''),
            'exit-date': dictonary.get('exit-date', ''),
            'street': dictonary.get('street', ''),
            'housenumber': dictonary.get('housenumber', ''),
            'city': dictonary.get('city', ''),
            'zip-code': dictonary.get('zip-code', ''),
            'contact-number': dictonary.get('contact-number', ''),
            'email': dictonary.get('email', ''),
            'health-problems': dictonary.get('health-problems', '')
        }

    def get_first_name(self, parent=0):
        """ parent = 0 bedeutet das es vom Member gewollt ist.
            parent = 1 währe dann von ersten Elternteil
            parent = 2 währe dann von ersten Elternteil
        """
        if (parent == 1):
            return self._data['parent-1-first-name']
        elif (parent == 2):
            return self._data['parent-2-first-name']
        return self._data['first-name']

    def get_last_name(self, parent=0):
        """ parent = 0 bedeutet das es vom Member gewollt ist.
            parent = 1 währe dann von ersten Elternteil
            parent = 2 währe dann von ersten Elternteil
        """
        if (parent == 1):
            return self._data['parent-1-last-name']
        elif (parent == 2):
            return self._data['parent-2-last-name']
        return self._data['last-name']

    def get_birthday(self):
        return self._data['member-birthday']

    def get_abo_category(self):
        return self._data['abo-category']

    def get_abo_cycle(self):
        return self._data['abo-cycle']

    def get_entry_date(self):
        return self._data['entry-date']

    def get_cancellation_date(self):
        return self._data['cancellation-date']

    def get_exit_date(self):
        return self._data['exit-date']

    def get_street(self):
        return self._data['street']

    def get_housenumber(self):
        return self._data['housenumber']

    def get_city(self):
        return self._data['city']

    def get_zip_code(self):
        return self._data['zip-code']

    def get_contact_number(self):
        return self._data['contact-number']

    def get_email(self):
        return self._data['email']

    def get_health_problem(self):
        return self._data['health-problems']

