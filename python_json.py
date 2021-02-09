""" Python objects are converted into the JSON equivalent:
    Python	    JSON
    -----------------
    dict	    Object
    list	    Array
    tuple	    Array
    str	        String
    int	        Number
    float	    Number
    True	    true
    False	    false
    None	    null
"""
import json

# Parse JSON - Convert from JSON to Python
student = '{ "name":"Abdullah","age":27, "city":"Dhaka","is_regular":true }'
parse_student = json.loads(student)
print("{}, {}, {}".format(parse_student["name"], parse_student["age"], parse_student["is_regular"]))

# Python object(dict) to json string
student = {"name": "Abdullah", "age": 27, "city": "Dhaka", "is_regular": True}
# sort the result alphabetically by keys with indent 4:
student_json = json.dumps(student, indent=4, sort_keys=True)
print(student_json)
