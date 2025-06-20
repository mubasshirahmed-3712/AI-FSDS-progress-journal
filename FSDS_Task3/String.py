# Author: Mubasshir Ahmed
# Topic: Strings and their methods in Python

# Single-line comment example
letter = 'P'  # a single character string
print(letter)               # P
print(len(letter))          # 1

greeting = 'Hello, World!'  # a common greeting string
print(greeting)             # Hello, World!
print(len(greeting))        # 13

sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline string examples
multiline_string = '''I am a student and love learning.
I didn't find anything as rewarding as solving problems with code.
That is why I'm following 30 Days of Python.'''
print(multiline_string)

multiline_string = """This is another example of a multiline string.
Used for documentation, messages, or poems."""
print(multiline_string)

# String Concatenation
first_name = 'Mubasshir'
last_name = 'Ahmed'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Mubasshir Ahmed

# Length comparison
print(len(first_name))              # 9
print(len(last_name))               # 5
print(len(first_name) > len(last_name))  # True
print(len(full_name))               # 15

# Unpacking characters
language = 'Python'
a, b, c, d, e, f = language
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Indexing
print(language[0])       # P
print(language[1])       # y
print(language[-1])      # n
print(language[-2])      # o

# Slicing
print(language[0:3])     # Pyt
print(language[3:6])     # hon
print(language[-3:])     # hon
print(language[3:])      # hon
print(language[0:6:2])   # Pto

# Escape sequences
print('Learning Python is fun.\nAre you enjoying it?')  # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('This is a backslash: (\\)')
print('First line starts with \"Hello, World!\"')

# String methods
challenge = 'thirty days of python'
print(challenge.capitalize())              # 'Thirty days of python'
print(challenge.count('y'))                # 3
print(challenge.count('y', 7, 14))         # 1
print(challenge.count('th'))               # 2
print(challenge.endswith('on'))            # True
print(challenge.endswith('tion'))          # False

# expandtabs
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())              # tabs replaced with spaces
print(challenge.expandtabs(10))

# find() method
challenge = 'thirty days of python'
print(challenge.find('y'))                 # 5
print(challenge.find('th'))                # 0

# format() example
first_name = 'Mubasshir'
last_name = 'Ahmed'
job = 'student'
country = 'India'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(radius, area)
print(result)

# index()
print(challenge.index('y'))                # 5
print(challenge.index('th'))               # 0

# isalnum()
print('ThirtyDaysPython'.isalnum())        # True
print('30DaysPython'.isalnum())            # True
print('thirty days of python'.isalnum())   # False
print('thirty days of python 2019'.isalnum())  # False

# isalpha()
print('thirtydays'.isalpha())              # True
print('123'.isalpha())                     # False

# isdigit()
print('30'.isdigit())                      # True
print('Thirty'.isdigit())                  # False

# isdecimal()
print('10'.isdecimal())                    # True
print('10.5'.isdecimal())                  # False

# isidentifier()
print('30DaysOfPython'.isidentifier())     # False
print('thirty_days_of_python'.isidentifier())  # True

# islower(), isupper()
print('python is cool'.islower())          # True
print('PYTHON IS COOL'.isupper())          # True

# isnumeric()
print('123'.isnumeric())                   # True
print('ten'.isnumeric())                   # False

# join()
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
print(' | '.join(web_tech))                # HTML | CSS | JavaScript | React

# strip()
challenge = '  thirty days of python  '
print(challenge.strip())                   # removes leading/trailing spaces

# replace()
print(challenge.replace('python', 'coding'))

# split()
print(challenge.split())                   # splits by spaces

# title()
print(challenge.title())                   # Thirty Days Of Python

# swapcase()
print('python is fun'.swapcase())          # PYTHON IS FUN
print('Python Is Fun'.swapcase())          # pYTHON iS fUN

# startswith()
print(challenge.startswith('thirty'))      # True
print('30 days of python'.startswith('thirty'))  # False
