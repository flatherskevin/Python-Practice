import time
from CSV2DB import CSV2DB
from DataPull import DataPull

start_time = time.time()

url = 'http://en.openei.org/doe-opendata/dataset/a7fea769-691d-4536-8ed3-471e993a2445/resource/86c50aa8-e40f-4859-b52e-29bb10166456/download/populationbycountry19802010millions.csv'

populationPull = DataPull(url, file='population.csv')
populationPull.download()

test = CSV2DB('population.csv', table='population', db='population.db')

end_time = time.time()

print('\n\nThe program ran in {time} seconds...\n\n'.format(time=round((end_time - start_time), 3)))