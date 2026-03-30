'''4. Replace the double space from problem 3 with single spaces.'''

sentence = '''This is the sentence  with  double space'''

print("This is before the removal")
print(sentence)

whitespaced_removed_sentence = sentence.replace("  "," ")
print("This is after the removal")
print(whitespaced_removed_sentence)

'''output

This is before the removal
This is the sentence  with  double space
This is after the removal
This is the sentence with double space
'''