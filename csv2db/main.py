import time
from CSV2DB import CSV2DB

start_time = time.time()

test = CSV2DB('education.csv', table='education', db='education.db')

end_time = time.time()

print('\n\nThe program ran in {time} seconds...\n\n'.format(time=round((end_time - start_time), 3)))