# Python Types:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

# without direct type
x = 'Hello World !'
print(x)
print(type(x))

# str type
x = str('Hello World !')
print(x)

# int type
x = int(25)
print(x)

# float type
x = float(20.5)
print(x)

# complex type
x = complex(1j)
print(x)

# list type
x = ["Apple", "Banana", "Grapes", "Mango"]
print(x)

# tuple type - A tuple is a collection which is ordered and unchangeable.
x = ("Apple", "Banana", "Grapes", "Mango")
print(x)

# range type
x = range(5)
print(x)

# dict type -A dictionary is a collection which is unordered, changeable and does not allow duplicates., dict type is similar to json stirng
x = {"id" : 1,"name" : "Kabir", "age" : 35}
print(x.get('id'))

# set type -A set is a collection which is both unordered and unindexed.
x = {"Apple", "Banana", "Grapes", "Mango"}
print(x)

# Boolean -Booleans represent one of two values: True or False.
x = True;
print(x)
# bool check exist or not
print(bool(x))