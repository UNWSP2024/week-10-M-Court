# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

#create class
class Employee:
		#initialize attributes	
		def __init__(self, name, number, department, job_title):
				self.name = name
				self.number = number
				self.department = department
				self.job_title = job_title
	
		#read all attributes
		def get_name(self, name):
				self.name = name
		def get_number(self, number):
				self.number = number
		def get_department(self, department):
				self.department = department
		def get_job_title(self, job_title):
				self.job_title = job_title
		
		def print_employee(self):
				print(f"Name: {self.name}")
				print(f"Number: {self.number}")
				print(f"Department: {self.department}")
				print(f"Job Title: {self.job_title}")
		
#create objects
#instance 1
employee1 = Employee("Susan Meyers", 47899,	"Accounting", "Vice President")
#instance 2
employee2 = Employee("Mark Jones", 39119,	"IT",	"Programmer")
#instance 3
employee3 = Employee("Joy Rogers", 81774,	"Manufacturing", "Engineer")

#print employee info
Employee.print_employee(employee1)
#new line
print("\n")
Employee.print_employee(employee2)
#new line
print("\n")
Employee.print_employee(employee3)