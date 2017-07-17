import time
from CSV2DB import CSV2DB
from DataPull import DataPull

start_time = time.time()

url = 'http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv'

populationPull = DataPull(url, file='population.csv')
populationPull.download()

test = CSV2DB('population.csv', table='population', db='population.db')

end_time = time.time()

print('\n\nThe program ran in {time} seconds...\n\n'.format(time=round((end_time - start_time), 3)))