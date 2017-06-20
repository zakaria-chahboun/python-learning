# import second_oop1 # Module : 1 Method
from second_oop1 import Car # Module : 2 Method
import re # regex
import sqlite3 # sqlite3

# run/start
def main():
	#------- Module -------
	# a_car = second_oop1.Car() # instance of Car :: 1 Method
	a_car = Car() # instance of Car
	a_car.setName("ford")
	a_car.getName()

	#------- FILES -------
	try:
		# myfile = open('text.txt','w') # write mode 
		# myfile.write("zakaria\n") # write in file
		myfile = open('text.txt','r') # read mode 
		for line in myfile:
			print(line)
		myfile.close()
	except Exception as e:
		print('MSG : {}'.format(e))

	#------- REGEX -------
	books = ['php learning','nodejs learning','c++ powerful']
	for el in books:
		if re.search("^p.*ing$",el): # start with 'p', end with 'ing'
			print el
	
	#--- SQL DATABASE ---
	#SQLite:
	conn = sqlite3.connect("test_python_db.db")
	conn.row_factory = sqlite3.Row # to change read mode infos "to dictionary variable"
	try:
		conn.execute("insert into mytab(name,age) values(?,?)",("test",10))
		rows = conn.execute("select * from mytab")

		for row in rows:
			print('ID: {} | Name: {} | Age: {}'.format(row['id'],row['name'],row['age']))

		conn.commit() # Save (commit) the changes
		conn.close()
	except Exception as e:
		print('MSG : {}'.format(e))


if __name__ == '__main__':
	main()

"""
*************************
zaki | 2017
*************************
"""