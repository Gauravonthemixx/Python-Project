import os  # We have imported the library to get the functionality of OS functions

'''We have created a function that takes three arguments and print the employee details based on the salary ranges 
provided by the user.'''


def employee_details_sort(employees_details, salary_lower, salary_highest):
    employees_output = []                                      # Empty list is created
    for employee in employees_details:
        name, job_title, salary = employee                     # Elements of tuples are assigned to the variable
        if salary_lower <= salary <= salary_highest:
            employees_output.append((name, job_title, salary))
    if not employees_output:
        print("There are no employee in the specified range of the salaries.")
        return
    employees_output.sort(key=lambda x: x[2], reverse=True)    # lambda function is used to sort the tuple using index.
    print("{:<20} {}".format("Name", "Job Title"))             # It will only print employee name and the job title.
    print("*" * 30)
    for employee in employees_output:
        name, job_title, salary = employee
        print("{:<20} {}".format(name, job_title))

'''We will ask the user to input a file which has all the details of employees. If the file is not present in the
specified path then it will throw an error'''
while True:
    file = input("Enter the name of your file ")
    if os.path.exists(file):
        print("The file exists")
        break
    else:
        print("The file does not exist!")

# 'Open' function is used to extract the file given by the user.
with open(file, 'r') as i:
    text = i.readlines()       # It will read the text of the file line by line.
    print(text)
new_tup = []                   # Variable is used to store the details of employees from the file.
for line in text:
    line = line.split(',')     # split function is used to split the string by comma separated value.
    print(line)
    line[2] = int(line[2].replace('\n', ''))  # Removes line separator if it exists at eol
    new_tup.append(tuple(line))    # A tuple is formed which has all the values

'''Asking the user to input the salary ranges from lower to higher and calling the function to sort the tuple
 on the basis of salaries '''

while True:
    choice = input("Press 'Y' to provide the salary ranges, else press 'N' to exit the program")
    if choice == 'Y' or choice == 'y':           # Asking the user if he wants to perform the task again or not
        salary_lower = input("Enter the lowest salary range")
        salary_upper = input("Enter the upper salary range")
        salary_lower = int(salary_lower)
        salary_upper = int(salary_upper)
        employee_details_sort(new_tup, salary_lower, salary_upper)
    if choice == 'N' or choice == 'n':           # If the user wishes to exit then press N or n.
        print("Thank you so much!")
        break;
