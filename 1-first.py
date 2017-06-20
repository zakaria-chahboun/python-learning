
def main():
	# variables : immutable : objects
	num=21
	txt="zaki"
	bool1=0 # 0 or False
	bool2=not(bool1) # true

	# format text
	# s1=f"my name is {txt} and i'm {num} years old." # for python3
	s2="my name is {} and i'm {} years old.".format(txt,num)
	print(s2)

	# tuple : immutable
	tp=(1,2,3)

	# list : mutable
	ar=[1,2,3,4]
	g=[]
	g[:]=range(8) # g = [0, 1, 2, 3, 4, 5, 6, 7]
	for item in g:
		#print(item,end=" | ") # python 3 :: print in same line
		print item, # python 2.7  :: print in same line
	print

	# dictionary : mutable
	dc={'a':10,'b':20,'c':30}

	# logic
	x=y=10
	print(x is y) # is : compare by (id) : same value = same id
	print(x==y and x!=y) # compare by (value)
	
	# bitwise
	bnr=0b1111 # (1111)bin = (15)int
	hx=0xA5 # (A5)hex = (165)int
	oc=0o45 # (45)octal = (37)int
	conv=hex(bnr) # hex() oct() bin() int() float() ect..
	print bnr,hx,oc,conv

	# exceptions
	try:
		a=1/0
	except Exception as e:
		print('cannot divide by 0!')

	# strings
	ee = "hello+world!"
	print(ee.upper()) # return new string
	print(ee.split('+')) # return list
	print "lenght of",ee,"is",len(ee)
	sim1 = ['welcome','to','my','tutorial']
	sim2 = 'welcome to my tutorial'
	fin1 = "-".join(sim1) # return string
	fin2 = "-".join(sim2) # return string
	print(fin1)
	print(fin2)
	print(ee.find('world'))
	print "zaki "+"karouh "+str(100)+"%"

#### Start here ###
if __name__ == '__main__':
	main()

"""
*************************
immutable : unable to be changed.
mutable : can be changed.

zaki | 2017
*************************
"""