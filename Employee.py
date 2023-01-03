#Classes meant to represent a typical employee
from Person import Person       #Imports the Person class so that the objects in the Person class also are used for this class
import random       #Imports the random library

class Employee(Person):         #Declares the class Employee extending the class of person
	def __init__(self, first_name, last_name, yearBorn, password_length, use_special_chars, use_nums):  #TMakes itself as an object and takes the first name, last name, year of birth, the numerical length of the password, the use of special characters, and the use of numbers as parameters 
		super().__init__(first_name, last_name, yearBorn)       #Extends the class of Person
		self.password_length = password_length      #Makes a variable based on the password_length parameter
		self.use_special_chars = use_special_chars      #Makes a variable based on the use_special_chars boolean parameter
		self.use_nums = use_nums    #Makes a variable based on the use_nums parameter
	def build_password(self, preDefined):
		alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
		special_chars = '!@#$%^&*'
		nums = '0123456789'
		count = 0
		password = ""
		if preDefined == True or self.password_length == 0:
			password = "2V9PZtfXGf6Ao9"
		else:
			password = ""
			while count < self.password_length:
				randChar = random.randrange(0,52,1)
				pwChar = alphabet[randChar]
				password += pwChar
				pwChar = ""
				count += 1
	
				if self.use_special_chars and count < self.password_length:
					randSC = random.randrange(0,7,1)
					pwSC = special_chars[randSC]
					password += pwSC
					pwSC = ""
					count += 1
				if self.use_nums and count < self.password_length:
					randNum = random.randrange(0,9,1)
					pwNum = nums[randNum]
					password += pwNum
					pwNum = ""
					count += 1
		return password