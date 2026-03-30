"""3. Write a program to detect double space in a string."""


sentence = '''This is the sentence  with  double space'''

# print(f"If the double space is present inside this it will return an index : {sentence.find("  ")}")
# This was failing because of the quotes nesting so need to use the things wisely 

print(f'If the double space is present inside this it will return an index : {sentence.find("  ")}')