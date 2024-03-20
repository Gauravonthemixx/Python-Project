# The function is used to check for the non prime numbers
# We are providing the argument to the function from lower to higher range
def non_prime_no(lower_limit, upper_limit):
    output = []    # empty list is initialised
    for number in range(lower_limit, upper_limit+1):
        if number >= 1:
            for i in range(2, number):
                if (number % i) == 0:      # if the number has more than one factor than it is a non prime number.
                    output.append(number)  # Non prime numbers are being added to the output list.
                    break
    return output

# Asking the user for the input
lower_limit= input("Enter the starting of the range ")
upper_limit= input("Enter the ending of the range")

# Converting the input to int as it is a string by default
l_limit= int(lower_limit)
u_limit= int(upper_limit)

# if the user enters higer value in the lower limit than this will convert the range
if l_limit > u_limit:
    t= l_limit             # I have used third variable to swap the lower limit and upper limit.
    l_limit= u_limit
    u_limit=t

# if user enters value less than 1 than it will give an error
if l_limit < 1 or u_limit < 1:
    print("Inavlid input entered, try entering positive number.")
# if the validation is correct than it will pass the arguments to the function
else:
    output = non_prime_no(l_limit, u_limit)
    if output:
        for i in range(0, len(output), 10):
            print(output[i:i+10])     # This we have used to format the output to print 10 items in a line.
    else:
        print("There are no non-prime numbers between the given range.")

