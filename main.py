from Profile import Profile
from prettytable import PrettyTable

user_1 = Profile()
user_1.properties['f_name'] = 'Felisha'
user_1.properties['l_name'] = 'Stone'
user_1.properties['dob'] = '09/06/1992'
user_1.properties['email'] = 'felisha.stone@gmail.com'

user_2 = Profile()
user_2.properties['f_name'] = 'Samuel'
user_2.properties['l_name'] = 'Fuel'
user_2.properties['dob'] = '01/06/1985'
user_2.properties['email'] = 'samuel.fuel@gmail.com'

user_3 = Profile()
user_3.properties['f_name'] = 'Jakie'
user_3.properties['l_name'] = 'Chan'
user_3.properties['email'] = 'kay_ra_tay@gmail.com'

user_4 = Profile()
user_4.properties['f_name'] = 'Tricky'
user_4.properties['l_name'] = 'Dicky'
user_4.properties['dob'] = '12/30/2001'

user_5 = Profile()
user_5.properties['f_name'] = 'Slap'
user_5.properties['l_name'] = 'Janiper'
user_5.properties['dob'] = '03/10/1994'
user_5.properties['email'] = 'samuel.fuel@gmail.com'

user_list = [user_1,user_2,user_3,user_4,user_5]

table = PrettyTable(('First', 'Last', 'DoB', 'Email'))

for user in user_list:
	table.add_row(user.properties.values())

print(table)