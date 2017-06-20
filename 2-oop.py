
class Car(object): # 2.x
	# properties
	name = "NO NAME"
	# constructor
	def __init__(self):
		print("Hello Car!")
	# setter	
	def setName(self,name):
		self.name = name
	# getter
	def getName(self):
		print("Car name is : {}".format(self.name))
	# method with kwargs
	def simple(self,**kwargs):
		model = kwargs['model']
		color = kwargs['color']
		year = kwargs['year']
		print("Model : "+model)
		print("color : "+color)
		print("Year : "+year)

# Inheritance
class PC(Car):
	# if this class does not have a constructor, by default the super constructor running
	def __init__(self):
		print("Hello PC!")
	# overriding
	def getName(self):
		print("overriding exapmle!")
	# super methods
	def getName2(self):
		super(PC,self).getName() #2.x
		# super().getName() # 3.x


# run/start
def main():
	mycar = Car() # instance of Car
	mycar.setName("toyota")
	mycar.getName()
	mycar.simple(model='1500A',year='2017',color='red')

	mypc = PC() # instance of PC
	mypc.getName()
	mypc.getName2()


if __name__ == '__main__':
	main()

"""
*************************
zaki | 2017
*************************
"""