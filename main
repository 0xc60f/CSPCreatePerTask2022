#Import Section
import json         #Imports the json module for reading diles
import getpass      #Import for finding the system user
from datetime import date       #Imports the date module
import matplotlib.pyplot as plt #Imports matplotlib module for making graphs

##############################
#
# Name: Soumya Sudhindra
# Date: 3/01/2022
# Program Description:
# The program takes in a text file as input and reads it through. The program makes a matplotlib graph based on the
# information provided by the included text file. Lastly, the program saves this info to the employee dictionary,
# saves the edited employee dictionary in the text file, and prints out the system name, the date, the eployee dictionary,
# graphs reflecting user input, and tables showing the hours inputted by the user.
###############################

#Variables Section
week_ending = ""            #Makes a variable storing the week ended
hours_worked = 0.0          #Makes a variable storing how many hours have currently been worked
graph_title = ""            #Makes a variable storing the graph titlr
graph_x_label = "Week Ending"   #Makes a x label for the graph
graph_y_label = "Hours Worked"  #Makes a y label for the graph

#Functions section
def make_plot(work_dates, hours_worked_each_week, graph_title, graph_x_label, graph_y_label):       #Takes the work dates, hours worked each week, the graph title, and the graph axes variables as parameters
    plt.plot(work_dates,hours_worked_each_week, linewidth=1)            #Makes a line graph with the work dates and hours worked each week with a line width of 1
    plt.title(graph_title, fontsize=24)                                 #Makes the graph title with a font size of 24 pt
    plt.xlabel(graph_x_label, fontsize=14)                              #Makes the graph x-label with a font zie of 14 pt
    plt.ylabel(graph_y_label, fontsize=14)                              #Makes the graph x-label with a font zie of 14 pt
    plt.tick_params(axis='both', labelsize=14)                          #Makes the labels show on both axes
    plt.show()                                                          #Makes the graph show
#Input Section
try:                                                        #Default block that runs
    with open("employee_data.txt", "r+") as file:                 #Opens the text file as a file type
        for line in file:                                   #Goes through each line in the text file
            temp_dict = str(line)                           #Makes a dictionary by making each line in the text file a string
            temp_dict = temp_dict.replace("\'", "\"")       #Replaces the single quotes in the dictionary with double quotes
            employee_dictionary = json.loads(temp_dict)     #Loads the info from the text file into the dictionary
except FileNotFoundError:                                   #If the file not found error is found, this block runs
    print(f"Sorry, the file {file} does not exist.")
else:                                                       #As a failsafe, this block of code runs
    file.close()                                            #Closes the file

for username,employee_data in employee_dictionary.items():              #Loops through each person in the dictionary in the text file
    work_dates_list = []                        #Creates a list to store the weeks ending
    hours_worked_list = []                      #Creates a list to store the hours worked

    for i in range (0,4):                           #Repeats 4 times
        week_ending = input(f"Enter a date for week ending for {username}: ")       #Asks for a week end date
        hours = input(f"Enter hours worked for {username} for week ending {week_ending}: ")     #Asks for hours worked for the employee for the week based on the above input
        hours_worked_list.append(float(hours))          #Adds the hours worked to hours_worked_list
        work_dates_list.append(week_ending)             #Adds the week endings to  work_dates_list
#Process Section
    avg_hours_worked = sum(hours_worked_list) / len(work_dates_list)            #Gets the average hours worked by dividing the hours worked by the amount of weeks 
    min_hour = min(hours_worked_list)       #Finds the lowest value in hours_worked_list
    max_hour = max(hours_worked_list)       #Finds the lowest value in hours_worked_list
    work_hour_stat = [avg_hours_worked, min_hour, max_hour]     #Makes a list storing each of the variables above

    #Appending these lists to the employee dictionaru
    employee_dictionary[username].append(work_dates_list)       
    employee_dictionary[username].append(hours_worked_list)
    employee_dictionary[username].append(work_hour_stat)

try:            #Default block of code
    with open("employee_data.txt", "w") as file:        #Opens writable file as a file
        file.write(str(employee_dictionary))            #Writes the employee dictionary to the text file
except FileNotFoundError:           #If a FileNotFoundError is found, the below statement is printed
    print(f"Sorry, the file {file} could not be found.")
else:           #At the end
    file.close()            #Closes the file
#Output Section
print(getpass.getuser())                                    #Prints the system user
print(date.today())                                         #Prints the current date

for username,employee_data in employee_dictionary.items():          #Loops through the dictionary
    print(username)

    graph_title = f"Hours worked for {employee_data[0]} {employee_data[1]}"     #Sets the graph title based on the employee name

    make_plot(employee_data[4], employee_data[5], graph_title, graph_x_label, graph_y_label)            #Takes the employee variables to call the function
    print(f"{employee_data[0]} {employee_data[1]} was born in {employee_data[2]}")
    print("{:<0} {:<15}".format("Date", "Hours"))               #Prints a table reporting the employee's hours
    for i in range(0,4):        #Repeats 4 times
        print("{:<0} {:<15}".format(employee_data[4][1], employee_data[5][1]))          #Prints each row in the table

    #Print the result of the variables
    print(f"The average amount of hours worked was {str(employee_data[6][0])}")
    print(f"The least amount of hours worked was {str(employee_data[6][1])}")
    print(f"The most amount of hours worked was {str(employee_data[6][2])}")

print(employee_dictionary)



