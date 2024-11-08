# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.  These values should be assigned to the object's __year_model and __make data attributes.  It should also assign 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute each time it it called.
# The brake method should subtract 5 from the speed data attribute each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.  After each call to the accelerate method, get the current speed of the car and display it.  The call the brake method.  After each call to the brake method, get the current speed of the car and display it.


#get user input
#get model
user_model = input("Enter model: ")
#get make
user_make = input("Enter make: ") 
#get speed
user_speed = int(input("Enter speed in mph: "))

#create class
class Car:
		def __init__ (self, model, make, speed):
				#add attributes
				self.model = model
				self.make = make
				self.speed = speed	
		
		#accelerate method
		def accelerate(self):
				#add 5
				self.speed += 5
				
		#brake method 
		def brake(self):
				#subtract 5
				self.speed -= 5

#create object with user input
car1 = Car(user_model, user_make, user_speed)

#set count at 0
count = 0
#display accelerate
print("Applying gas...")

while count < 5:
		car1.accelerate()
		print(f"current speed is {car1.speed} mph")
		count += 1

#reset count at 0
count = 0
#display brake
print("Applying brake...")

while count < 5:
		car1.brake()
		print(f"current speed is {car1.speed} mph")
		count += 1
