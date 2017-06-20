

# run/start
def main():

	#---- Normal Function ----
	def f1(x,y):
		return x+y
	
	#---- LAMBDA Function ----
	f2 = lambda x, y : x + y

	print f1(1,2)
	print f2(1,2)

	#---- Example use with filter() ----
	""" Program to filter out only the even items from a list """

	my_list = [1, 5, 4, 6, 8, 11, 3, 12]
	new_list = filter(lambda x: (x%2 == 0) , my_list) # in python 3.x : list(filter(..etc))
	print(new_list)
	
	#---- Example use with map() ----
	""" Program to double each item in a list using map() """
	my_list = [1, 5, 4, 6, 8, 11, 3, 12]
	new_list = map(lambda x: x * 2 , my_list) # in python 3.x : list(map(...ect))
	print(new_list)



if __name__ == '__main__':
	main()

"""
*************************
1- In Python, we generally use lambda functions as an argument
	to a higher-order function (a function that
		takes in other functions as arguments).

2- The filter() function in Python takes in a function and a list as arguments.
	The function is called with all the items in the list
		and a new list is returned which contains items
			for which the function evaluats to True.

3- The map() function in Python takes in a function and a list.
	The function is called with all the items in the list
		and a new list is returned which contains items
		returned by that function for each item.


zakaria chahboun | 2017
*************************
"""