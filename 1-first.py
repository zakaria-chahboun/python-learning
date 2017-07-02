
def main():
	# variables : immutable : objects
	num=21
	txt="zaki"
	bool1=0 # 0 or False
	bool2=not(bool1) # true
	test = 2.15
	e,g = ['hello','salam'] # e = 'hello' and g = 'salam'
	del(test) # delete 'test' variable 

	# format text
	# s1=f"my name is {txt} and i'm {num} years old." # for python3
	s2="my name is {} and i'm {} years old.".format(txt,num)
	print(s2)

	# tuple : immutable
	tp=(1,2,3)
	x,y,z = tp # x=1,y=2,z=3

	# list : mutable
	ar1 = [1,2,3,4]
	ar2 = [5,6]
	print(ar1[:]) # [1,2,3,4]
	print(ar1[1:2]) # [3]
	print(ar1[:2]) # [1,2,3]
	print(ar1[1:]) # [2,3,4]
	ar3 = ar1+ar2 # concatenating lists 
	print(ar3) # : [1,2,3,4,5,6]
	print(ar3.append(7)) # add item to end of list  : [1,2,3,4,5,6,7]
	print(ar3.pop()) # remove the last item of list : [1,2,3,4,5,6]
	print(ar3.remove(1)) # remove an item (first instance) from list : [2,3,4,5,6]
	ar4 = [ar1,ar2,ar3] # list of multiple dimensions
	print(ar4) # [[1, 2, 3, 4], [5, 6], [2, 3, 4, 5, 6]]
	x1 = ['A','B','C'][0] # x1 = 'A'

	g=[] # void list
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
	print(ee[0:5]) # return string : hello
	print(ee[6:-3]) # return string : wor
	print(ee.upper()) # return string : HELLO+WORLD!
	print(ee.split('+')) # return list : ['hello', 'world!']
	print(len(ee)) # length : 12
	sim1 = ['welcome','to','my','tutorial']
	sim2 = 'welcome to my tutorial'
	fin1 = "-".join(sim1) # return string
	fin2 = "-".join(sim2) # return string
	print(fin1) # : welcome-to-my-tutorial
	print(fin2) # : w-e-l-c-o-m-e- -t-o- -m-y- -t-u-t-o-r-i-a-l
	print(ee.find('world')) # return first position : 6
	print("zaki "+"karouh "+str(100)+"%") # concatination : zaki karouh 100%
	print(3*"zaki ") # loop : zaki zaki zaki 

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