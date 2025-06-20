# Author: Mubasshir Ahmed
# Topic: Working with variables in Python

# Declaring and initializing variables
first_name = 'Mubasshir'
last_name = 'Ahmed'
country = 'India'
city = 'Hyderabad'
age = 21
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']

# Dictionary storing personal info
person_info = {
    'firstname': 'Mubasshir',
    'lastname': 'Ahmed',
    'country': 'India',
    'city': 'Hyderabad'
}

# Printing the values stored in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Person information:', person_info)

# Declaring multiple variables in one line (overwriting previous values)
first_name, last_name, country, age, is_married = 'Mubasshir', 'Ahmed', 'India', 21, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)
