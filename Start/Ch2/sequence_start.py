# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
# print(len(mylist))

# to access a member of a sequence type, use []
# print(mylist[0])
# print(mylist[-3])
# mylist[0] = 10
# print(mylist)
# print(mylist[0])
# add a list to another list
another_list = [6,7,8]
mylist = another_list + mylist
print(mylist)

# use slices to get parts of a sequence


# you can use slices to reverse a sequence


# Tuples are like lists, but they are immutable


# Sets are also sequences, but they contain unique values

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
