#Ques3 (a)
# Function is defined to check if a entered string is palindrome or not.
# We have stored the reverse of the string in a new variable named rev_str.
# Conditional statements are used to check if the string are equal or not.
# The function is returning true if a string is palindrome otherwise it will return false.
def check_palindrome(str):
    rev_str = str[::-1]
    if str == rev_str:
        return True
    else:
        return False

# Ques3 (b)
# The function is converting the string into uppercase letters
# It is counting the most occuring letter in the string enetered by user.
def frequent_letter(s):
    upper_s = s.upper()
    print("The string in upper case is: ", upper_s)
    alpha_counts = {}
    for alpha in upper_s:
        if alpha not in alpha_counts:
            alpha_counts[alpha] = 1
        else:
            alpha_counts[alpha] = alpha_counts[alpha] + 1     # Variable is increased everytime the letter appears.

    return max(alpha_counts, key=alpha_counts.get)            # Max function is used to return the most frequent letter.



# Ques3(c)
# This function is taking string as an arguments and it is counting the letter, digits and spaces.
# The final output is returned in the form of dictionary.
# String method are used.

def counting(s):
    output_dict = {"Letter": 0, "Digits": 0, "Spaces": 0}      # Empty dictionary is created
    for i in s:
        if i.isalpha():
            output_dict["Letter"] = output_dict["Letter"] + 1
        elif i.isdigit():
            output_dict["Digits"] = output_dict["Digits"] + 1
        elif i.isspace():
            output_dict["Spaces"] = output_dict["Spaces"] + 1

    return output_dict

