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
# another_list = [6,7,8]
# mylist = another_list + mylist
# print(mylist)

# use slices to get parts of a sequence
# print(mylist[1:4:2])
# print(mylist[::2])

# you can use slices to reverse a sequence
# print(mylist[::-1])
# mystr = "Hi, my name is Colleen."
# print(mystr[::])

# Tuples are like lists, but they are immutable (meaning they can't be changed)
mytuple = (0, 1, 2, "three")
# print(mytuple[1])

# Sets are also sequences, but they contain unique values (there can't be 2 or more of the same value because only 1 will print)
# Can't be indexed
myset = {1, 2, 3, 2, 4, "hey"}
#print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in mylist)
print(3 in mytuple)
print(5 in myset)