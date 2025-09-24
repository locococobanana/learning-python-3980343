# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def hello_func():
#   print("Hello World!")
#   name = input("What is your name? ")
#   print("Nice to meet you,",name+"!")

# hello_func()

# function that takes parameters (allows you to customize the action)
# def hello_func(greeting):
#   print("Hello World!")
#   name = input("What is your name? ")
#   print(greeting,name)

# hello_func("How are you doing")
# hello_func("Hey, what's up")

# function that returns a value
# def cube(x):
#   return x * x * x

# result = cube(3)
# print(result)

# function with default value for an parameter
# def hello_func(greeting, name=None):
#   print("Hello, World!")
#   if name == None:
#     name = input("What is your name? ")
#   print(greeting,name+"!")

# hello_func("Nice to meet you,")

# can change the order by explicitly assigning the variable
# hello_func(name="Joe", greeting="nice to meet you")

# function with variable number of parameters
def multi_add(start, *args):
    result = start
    for x in args:
        result = result + x
    return result
print(multi_add(0,4,5,10,4,10))