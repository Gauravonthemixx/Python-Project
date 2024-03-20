# We have imported the datetime so that we can use today's date to calculate the age of the user.
from datetime import date

# A variable named current_date is initialised which contains the value of today's date.
current_date = date.today()
european_date = current_date.strftime('%d-%m-%Y')
print("The date in European format is: ", european_date)

# We have asked the user to input his/her date of birth in the specified format.
user_dob = input("Enter your date of birth in the format of mm/dd/yyyy")

# if condition is used to check if the format is valid or not using string methods and referencing the index of string.
if len(user_dob) != 10 or user_dob[2] != '/' or user_dob[5] != '/':
    print("Error: The format of date is not correct. ")
    exit()

# Month, date and year are stored in separate variable and string method 'split' is used to achieve that
user_dob_month, user_dob_day, user_dob_year = user_dob.split('/')

# conditions are used below to check if the date is valid or not because the date must be in American date format
if int(user_dob_month) < 1 or int(user_dob_month) > 12 :
    print("Error : The entered date is not valid ")
    exit()

if int(user_dob_day) < 1 or int(user_dob_day) > 31:
    print("Error : The entered date is not valid ")
    exit()

if int(user_dob_month) == 2 and int(user_dob_day) > 29:
    print("Error : The entered date is not valid ")
    exit()

if (user_dob_month == 4 or user_dob_month == 6 or user_dob_month == 9 or user_dob_month == 11) and user_dob_day > 30:
    print("Error: The entered date is not valid ")
    exit()

# We subtract the date of birth's year with current year to get the age of the user.
age = current_date.year - int(user_dob_year)

# The date of birth cannot be a year from the future otherwise it will give a negative output which is invalid.
if int(user_dob_year) > current_date.year:
    print("invalid birth year entered")
    exit()

# If birthday month is greater than the current month then we will subtract the age by 1.
if int(user_dob_month) > current_date.month:
    print(age-1)

# If months are same then we have to check for the days, if it is greater than we have to subtract it by -1.
elif int(user_dob_month) == current_date.month:
    if int(user_dob_day) > current_date.day:
        print(age-1)
    else:
        print(age)

# if month is less than the current month then simply we will get the age by subtracting the years.
else:
    print(age)






