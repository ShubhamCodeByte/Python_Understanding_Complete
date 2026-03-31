""" Dictonaries """

""" 
Theory

Dictionary is a collection of keys-value pairs.

PROPERTIES OF PYTHON DICTIONARIES
1. It is unordered.
2. It is mutable.
3. It is indexed.
4. Cannot contain duplicate keys.



"""

# Syntax

# Empty Dictionary
empty = {}

new = {
  "age": 21,
  "status": "single",
  "marks": 90,
  "list": [1,3,6],
  45: "Number",
}

print(new)                  # {'age': 21, 'status': 'single', 'marks': 90, 'list': [1, 3, 6], 45: 'Number'}

# print(new[2]) # we cannot use like this as 2 is not present in the key
# dictionaries do not have numerical indexes by default

print(new["age"])           # 21

print(new.get("marks"))     # 90

""" Methods of the dictionaries """

print(new.items())         # dict_items([('age', 21), ('status', 'single'), ('marks', 90), ('list', [1, 3, 6]), (45, 'Number')])
print(new.keys())          # dict_keys(['age', 'status', 'marks', 'list', 45])
print(new.values())        # dict_values([21, 'single', 90, [1, 3, 6], 'Number'])


new.update({"subject": "Python"})

print(new)                 # {'age': 21, 'status': 'single', 'marks': 90, 'list': [1, 3, 6], 45: 'Number', 'subject': 'Python'}

