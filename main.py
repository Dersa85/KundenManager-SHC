from database.member import Member
from database.hard_drive import HardDrive


# Die vorlage die bei der Klasse Member ist soll in die Datei >members/0.json< gespeichet werden (ALSO JSON)
test_member = {
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
HardDrive.save(test_member, './members/0.json')


#dict = HardDrive.load('./members/0.json')
#member = Member(json)















"""
database = {
    'first-name' : 'Max',
    'last-name' : 'Helmut'
}

database2 = [
    {
        'first-name': 'Alexander',
        'last-name': 'Helmut'
    },
    {
        'first-name': 'Max',
        'last-name': 'Helmut'
    }
]
print(database2[1])

print('---------------------')
for user in database2:
    print(user['first-name'], user['last-name'])

def get_member_by_firstname(name):
    for user in database2:
        if name == user['first-name']:
            return user
print('---------------------')
print(get_member_by_firstname('Max'))

"""