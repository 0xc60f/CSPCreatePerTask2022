#Classes meant to represent a typical person``
import datetime     # Imports the datetime class for the 3rd function

class Person:
    def __init__(self, first_name, last_name, yearBorn):        #Takes in the input of the first name, last name, and year born from the main program
        self.first_name = first_name    #Assigns the value(first_name) of this function from input from the main program
        self.last_name = last_name  #Assigns the value(last_name) of this function from input from the main program
        self.yearBorn = yearBorn    #Assigns the value(yearBorn) of this function from input from the main program
    def greeting(self):     #Takes the object "self" as a parameter
        greeting = f"Welcome, {self.first_name}"       #Finds the value of the first name from the self object and concatenates it with "Welcome"
        return greeting     #Returns the greeting to the main program
    def age(self):      #Takes the object "self" as a parameter
        today = datetime.date.today()    #Finds the current date in full form and assigns it to a variable
        age = today.year - int(self.yearBorn)   #Finds the age by subtracting the current year and the year inputted from the self object
             
        return age      #Returns the result to the main console