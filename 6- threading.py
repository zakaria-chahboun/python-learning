# always in the beginning :: for use print(..) like python 3
from __future__ import print_function
import threading
import time

def testTread():
	for i in range(1,11):
		print('{}/10'.format(i),end='\r') # overwrite same line :)
		time.sleep(1)


def main():

	MyTread = threading.Thread(target=testTread, name="MyTread")
	
	print('from {}'.format(MyTread.getName()))
	MyTread.start()

if __name__ == '__main__':	main()




### zakaria chahboun | 2017