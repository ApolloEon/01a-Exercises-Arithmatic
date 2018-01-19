'''

01a Exercises
These exercises should help you get the flavor of how to perform arithmetic and string operations in Python. 
You will also get to play with (pseudo-)random generators and the range operator.
These skills will all be used in assignment 2.

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening. 


'''
# Math in Python is what you would expect. Add comments with the answers the IDLE returns. I'll do the first one for you.
10 + 15 
# 25
8 - 1
# 7
10 * 2
# 80
35 / 5
# 7.0

35 / 4
# 8.75
35 // 4
# 8
# What is the difference between the / operator and the // operator?
# One is more weighted than the other. / just divides while // gives you a whole number.

2 ** 5
#
# What does the ** operator do?
# Raises the the number to the left to the power of the **
5 % 3
# 2
5 % 2
# 1
5 % 4
# 1
# What does the % operator do?
# It gives the remainder of the operation.

(1 + 3) * 2
# 8
# What effect do the parenthesis have on this statement?
# It acts just like PEMDAS and separates what arithmetic should be done first.

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
# <class 'int'>
type(3.0)
# <class 'float'>
type("word")
# <class 'str'>
type(True)
# <class 'bool'>
type(False)
# <class 'bool'>
type(None)
# <class 'NoneType'>
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another.
int(3.0)
# 3
float(7)
# 7.0
str(55)
# '55'
bool(1)
# True
# How can you tell the difference between these four different types?
#

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
# It combined the two words, or strings

"This is a string"[0]
# 'T'
"This is a string"[5]
# 'i'
"This is a string"[8]
# 'a'
# What is happening as you change the number?
# As I change the number, the strings are turning into letters. Though I do not know what is going on internally.

"This is a string"[-1]
# '.'
# What happens when you use a negative number?
# It turns the string into a punctuation. A period in this case.

"%s can be %s" % ("strings", "interpolated")
# What is happening here?
# It looks very confusing and hard to tell, but for the most part it seems as if it removed the reduant things and combined the strings.

# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
# 'strings cn be formatted.'

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
# 'Bob wants to eat lasagna'

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
# Hello, Apollo
# What just happened?
# After putting in what "n" represented, IDLE implicated it's new instructions.

# For your next assignment, you will need to use random numbers
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
#

randint(1,100)
# How is this different?
#

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
# It did what you programmed it to do and shuffled the numbers around.

print(sample(items, 1))
# What does this do?
#

print(sample(items, 5))
# What does the second parameter control?
# I'm not too sure, but it looks as though it still shuffled the items while making 5 the number of items being showcased.

for i in range(0,5):
	print(i)
# 
# What is happening here? What happens if you change the two range parameters?
#
'''

01a Exercises
These exercises should help you get the flavor of how to perform arithmetic and string operations in Python. 
You will also get to play with (pseudo-)random generators and the range operator.
These skills will all be used in assignment 2.

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening. 


'''
# Math in Python is what you would expect. Add comments with the answers the IDLE returns. I'll do the first one for you.
10 + 15
# 25
8 - 1
# 7
10 * 2
# 80
35 / 5
# 7.0

35 / 4
# 8.75
35 // 4
# 8
# What is the difference between the / operator and the // operator?
# One is more weighted than the other. / just divides while // gives you a whole number.

2 ** 5
#
# What does the ** operator do?
# Raises the the number to the left to the power of the **
5 % 3
# 2
5 % 2
# 1
5 % 4
# 1
# What does the % operator do?
# It gives the remainder of the operation.

(1 + 3) * 2
# 8
# What effect do the parenthesis have on this statement?
# It acts just like PEMDAS and separates what arithmetic should be done first.

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
# <class 'int'>
type(3.0)
# <class 'float'>
type("word")
# <class 'str'>
type(True)
# <class 'bool'>
type(False)
# <class 'bool'>
type(None)
# <class 'NoneType'>
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another.
int(3.0)
# 3
float(7)
# 7.0
str(55)
# '55'
bool(1)
# True
# How can you tell the difference between these four different types?
#

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
# It combined the two words, or strings

"This is a string"[0]
# 'T'
"This is a string"[5]
# 'i'
"This is a string"[8]
# 'a'
# What is happening as you change the number?
# As I change the number, the strings are turning into letters. Though I do not know what is going on internally.

"This is a string"[-1]
# '.'
# What happens when you use a negative number?
# It turns the string into a punctuation. A period in this case.

"%s can be %s" % ("strings", "interpolated")
# What is happening here?
# It looks very confusing and hard to tell, but for the most part it seems as if it removed the reduant things and combined the strings.

# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
# 'strings cn be formatted.'

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
# 'Bob wants to eat lasagna'

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
# Hello, Apollo
# What just happened?
# After putting in what "n" represented, IDLE implicated it's new instructions.

# For your next assignment, you will need to use random numbers
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
#

randint(1,100)
# How is this different?
#

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
# It did what you programmed it to do and shuffled the numbers around.

print(sample(items, 1))
# What does this do?
#

print(sample(items, 5))
# What does the second parameter control?
# I'm not too sure, but it looks as though it still shuffled the items while making 5 the number of items being showcased.

for i in range(0,5):
	print(i)
#
# What is happening here? What happens if you change the two range parameters?
#
