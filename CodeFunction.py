# What we learn in this code 
# - Functions

# - Modules libraries
# - Code readability

# Lets start from - Functions -  A section of code that can be reused in a program

# Lets start with user define functions - key word uesd for this is "def"
# def greet_employee():
#     print ("Welcome ! You are logged In.")

# # Lets call our function greet_employee
# greet_employee()

# Function with parameters eg. name
# def greet_employee(first_name, last_name):
#     print ("Welcome ! You are logged in", first_name, last_name)
# greet_employee("Varinder", "Kumar")


# Return function - a python statement that executes inside a function and sends inforamtion back to the function call.

# def calculate_fails(total_attempts, failed_attempts):
#     failed_percentage = failed_attempts / total_attempts
#     # print(failed_percentage)
#     return failed_percentage 
# percentage = calculate_fails(4,2)   

# if (percentage >= .5):
#     print("Account is locked")



# print(type(78))
# alp = ['d','e','f','g']

# print(sorted(alp))

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup)