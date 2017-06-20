import urllib3,json
from collections import namedtuple # in this exapmle : for JSON to OBJECT



# run/start
def main():

	#---- HTTP ----
	urllib3.disable_warnings() # disable HTTPS warning in console

	http = urllib3.PoolManager()
	req = http.request('GET', 'https://goo.gl/E8o0wW') # Yahoo JSON
	#print(req.data) # data is a str type

	#---- JSON ----
	myjson = json.loads(req.data) # now the data is a json (dict type)
	print('Title : '+myjson['query']['results']['channel']['title'])

	# json to object (with lambda anonymous function)
	x = json.loads(req.data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
	print('2 Title: '+x.query.results.channel.title)




if __name__ == '__main__':
	main()

"""
*************************
zaki | 2017
*************************
"""