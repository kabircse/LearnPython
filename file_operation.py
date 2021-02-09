""" File operation mode:
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists
"""

# Read file
f = open('demo_file.txt', 'r')
print(f.read())

# Read a line
print(f.readline())
f.close()

# Write to a file
try:
    f = open('demo_file.txt', 'a')
    f.write(input('Enter your text: '))
except:
    print('File is not writeable.')
finally:
    f.close()
