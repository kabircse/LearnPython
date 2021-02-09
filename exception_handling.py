# The try block will generate a NameError, because x is not defined:
try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("Something else went wrong")

# try, except, else
try:
    print(x)
except:
    print("Variable x is not defined")
else:
    print("Something else went wrong")

# try, except, finally
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished, we are in finally.")

# To throw (or raise) an exception, use the raise keyword.
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
