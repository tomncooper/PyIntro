""" Example of Python Syntax """

#pylint: disable=invalid-name,simplifiable-if-statement

print("Hello World!")

x = 10
y = 15

print(x + y)


# Creating lists (arrays) of things is easy
list_of_things = [1, 2, 3, 4, 5]

# Python (unlike other, lesser languages) indexes from zero
print(list_of_things[0])

# For loops are a thing of beauty
for thing in list_of_things:
    print(thing)

####

# If statements are easy to understand
if x is not y:
    print("10 is not 15!")
else:
    print("10 is 15!!!")

if 1 in list_of_things:
    one_is_in_things = True
else:
    one_is_in_things = False

# And can often be simplified easily
one_is_in_things = 1 in list_of_things

print_answer = True

if one_is_in_things and print_answer:
    print("One is in things")

####

# Everything in python is an object and has methods
for method in dir(list_of_things):
    print(method)

list_of_things.append(0)
list_of_things.append("")
list_of_things.append("six")
print(list_of_things)

# Adding a list to another list returns a new list
list_of_things = list_of_things + [7, 8, 9, 10]

# Python has a concept of truthyness so 0 and empty strings are False
for a_thing in list_of_things:
    if a_thing:
        print(a_thing)


####

# Dictionaries provide key:value storage for quick access (like a HashMap in
# Java)

dict_of_things = {"a":1, "b":2, "c":"three", "d":4.0}

# Accessing the value by name is easy
print(dict_of_things["a"])
print(dict_of_things.get("c"))

# Adding keys and values
dict_of_things["e"] = [5, 6, 7]
dict_of_things["e"].append(8)
print(dict_of_things)

for key_thing, value_thing in dict_of_things.items():
    print("Key: {}".format(key_thing))
    print("Value: {}".format(value_thing))

# The above is an example of unpacking - Python can do multiple assignments on
# one line

a, b = 1, 2
print(a)
print(b)

a, b = b, a
print(a)
print(b)
