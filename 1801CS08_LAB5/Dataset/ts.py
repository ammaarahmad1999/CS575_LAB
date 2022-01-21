from pandas_datareader import data as pdr
from datetime import datetime
ibm =   pdr.DataReader('IBM', 'yahoo', start=datetime(2019, 1, 1),end=datetime(2019, 12, 31))
aapl =  pdr.DataReader('AAPL', 'yahoo', start=datetime(2019, 1, 1),end=datetime(2019, 12, 31))
fb =    pdr.DataReader('FB', 'yahoo', start=datetime(2019, 1, 1),end=datetime(2019, 12, 31))
googl = pdr.DataReader('GOOGL', 'yahoo', start=datetime(2019, 1, 1),end=datetime(2019, 12, 31))
itc =   pdr.DataReader('ITC.NS', 'yahoo', start=datetime(2019, 1, 1),end=datetime(2019, 12, 31))
infy=   pdr.DataReader('INFY.NS', 'yahoo', start=datetime(2019, 1, 1),end=datetime(2019, 12, 31))


ibm.to_csv('IBM_stock.csv', sep=',')
aapl.to_csv('Apple_stock.csv', sep=',')
fb.to_csv('Facebook_stock.csv', sep=',')
googl.to_csv('Google_stock.csv', sep=',')
itc.to_csv('ITC_stock.csv', sep=',')
infy.to_csv('Infosys_stock.csv', sep=',')