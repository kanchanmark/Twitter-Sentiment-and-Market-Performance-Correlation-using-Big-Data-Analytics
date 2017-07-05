from yahoo_finance import Share
import json
from pprint import pprint

American = Share('AAL').get_historical('2017-04-15', '2017-05-14')
for item in American:
	variation = float(item['Close']) - float(item['Open'])
	date = item['Date']
	print(date +'  --->  open: ' + str(item['Open'])+'  Close: '+str(item['Close'])+'  Variation: '+str(variation))