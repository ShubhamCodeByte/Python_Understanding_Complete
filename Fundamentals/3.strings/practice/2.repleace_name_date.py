"""

2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
"""


initial_sentence = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

Name = input("Enter the name ")
Date = input("Enter the date ")

updated_name = initial_sentence.replace("<|Name|>",Name)
final = updated_name.replace("<|Date|>",Date)


print(final)


"""

Output:

Enter the nameShubham Singh
Enter the date23/03/2026

Dear Shubham Singh,
You are selected!
23/03/2026

"""