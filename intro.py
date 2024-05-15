


# comments


# Syntax
# CASE SENSITIVE
# Indentations and white space matter


# Variables and Strings

# Variable Names
# only alpha numeric characters and underscores
# cannot start with a number
# cannot have any spaces
# are case sensitive
# Cannot contain any python keywords


# Built in Data Types
# Text Type
#   String

# Can be assigned with single or double quotes
# multi line strings with three quotes
# String slicing with indexes
# Modifying strings with built in methods
#   .upper()
#   .lower()
#   .capitalize()
#   .count()
#   .strip() removes leading and trailing whitespaces
#   .replace() replaces a string with another string
#   .split() splits the string into multiple strings if the separator is found
# Concatenate strings by adding them together
# escape character \ 



# Numbers
# integers and floats
# Integers are non-decimal numbers, positive or negative
# Floats are decimal numbers and can have any level of precision
# complex numbers exist, but lets not worry about them
# booleans are a special type of integers


# Operators
# Addition +
# Subtraction -
# Multiplication *
# Division / 
#   Always returns a float
# modulus %
#   returns the remainder after division
# Floor Division //
# Exponentiation **

# Comparison Operators
#   All return booleans
# ==
# !=
# >
# <
# >=
# <=
# is


# Logical Operators
# and
#   returns True if both statements are True
# or
#   Returns True if one or both of the statements are True
# not
#   Reverses the result


# Membership Operators
# in
#   returns true if the value is present in the object
# not in
#   returns true if the value is not present in the object


# Order of Operations
# PEMDAS
# Logical Not
# Logicals



# Sequences
# lists [1,2,3]
#   ordered, mutable (they can be changed in place)

cars = ['ford','jeep','tesla','volkswagen']
other_cars = ['chevy','lexus','bmw']


cars.append(other_cars)
cars

cars.extend(other_cars)
cars

# tuples (1,2,3)
#   ordered, immutable (they cannot be changed in place)

cars = ('ford','jeep','tesla','volkswagen')


#dictionaries

car = {
   'color':'blue'
   , 'make':'ford'
   , 'year':'2022'
}


car.get('year')

car['model'] = 'mustang'

car.get('model')


car['year'] = 1971

car.get('year')

car.values()









#strings
print("hello world")


a = "hello"
b = "world"

print(a)
print(b)

print(a+" "+b)

c = 'it\'s hot in here'
c = "it's hot in here"


a, b = b, a + b

a
b


a + b


a * b

a**b

b / a

b % a

11 % 3


12 // 4


#This is a comment
#
#this is more comment
#Booleans

x =  4
x != 4
True or False


#lists
####ordered mutable object



#tuples
######ordered immutable object
cars = ('ford','jeep','tesla','volkswagen')


#dictionaries

car = {
   'color':'blue'
   , 'make':'ford'
   , 'year':'2022'
}


car.get('year')

car['model'] = 'mustang'

car.get('model')


car['year'] = 1971

car.get('year')

car.values()

##
for i in car.keys():
    print(f"My Cars {i} is {car.get(i)}")



cars[::-1]

second_cars = cars

second_cars

cars == second_cars

cars is second_cars

second_cars[0] = 'Oh no I wrecked my car'

second_cars

cars


cars
cars[0] = 'chevy'
cars

a[0] = 'a'

cars

a = cars.copy()



second_cars


#if Statements
a = 11
b = 10






if a > b:
    print("a is greater than BEEEEEEE")
    print("and this")
    print("and that")
elif b > a:
    print("b is greater than a")
else:
    print("Then B and A must be equal")


#While Loops
i = 1
while i < 11:
    if i == 1:
        print(f"Hello Derek for the {i}st time")
    elif i == 2:
        print(f"Hello Derek for the {i}nd time")
    elif i == 3:
        print(f"Hello Dave for the {i}rd time")
    else:
        print(f"Hello Derek for the {i}th time")
    i = i +1


#For Loops
cars = ('ford','jeep','tesla','volkswagen')

type(cars)

i=1
for item in cars:
    if item == 'volkswagen':
        while i < 5:
            print(f"Derek drives a {item}")
            i += 1
    else:
        print(f"Derek does not drive a {item}")

for letter in "Derek":
    print(letter)


#Functions
def say_hello(name='Dave'): 
    print(f"Hello {name}")
    return



def add_nums(a,b):
    value = a+b
    return value



x = add_nums(a=4,b=7)

print(x)

say_hello(name = x)





print()

























































