# Python 101 sample code.
# Refer to this code for examples on python syntax

# This is a comment, python inline comments start with an '#'

# this is a python variable, notice that it is not declared with a type, it is simply initialized to any value
new_variable = 1
another_variable = "any data type can be assigned to python variables, this is a string for example"
exampleThree = 23.0103

# to print to terminal, simply use the print command
# you can print to the same line by separating values with a comma on the same print command.
# a new print command automatically goes to new line
print("Here are the previous variables, variable 1: ", new_variable)
print("Variable 2: ", another_variable)
print("Variable 3: ", exampleThree)

# now lets show an if statement
# notice how it uses a colon and indentation instead of curly bracket
if new_variable == 1:
    print("entered if statement")

else:
    print("Here is an example of an else statement")


# Now lets run a while loop
counter = 0
while counter < 5:
    print("counter: ", counter)
    counter += 1

# for loop
# for loop uses the in keyword and range to denote the range. This will take a little bit to get used to, but not a big deal
for i in range(5):
    print("i: ", i)


# last thing, lets define a function
# instead of using the return type to declare the function (like in c++), we just use the keyword 'def'
def new_function():
    print("function 1 fired")

# We dont need to declare the type of values we pass either
def function_two(passed_value):
    print("function two, passed a value of: ", passed_value)

# Now lets call our functions
new_function()

# Lets call function_two with different values
function_two(23)
function_two("you can pass any value")
