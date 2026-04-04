"""
1. Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.
"""



with open("../poems.txt") as f:
# with open("../demo.txt") as f:
  text = f.read()
  if (("Twinkle" or "twinkle") in text):
    print("Twinkle is present")
  else:
    print("Twinkle is not present")




# with open("poems.txt","x") as f:    # i have given the wx argument in the open which is invalid we can write also in the create mode 
#   poem = '''
#   Twinkle, twinkle, little star,
#   How I wonder what you are!
#   Up above the world so high,
#   Like a diamond in the sky.

#   When the blazing sun is gone,
#   When he nothing shines upon,
#   Then you show your little light,
#   Twinkle, twinkle, all the night.

#   Then the traveler in the dark
#   Thanks you for your tiny spark,
#   How could he see where to go,
#   If you did not twinkle so?

#   In the dark blue sky you keep,
#   Often through my curtains peep
#   For you never shut your eye,
#   Till the sun is in the sky.

#   As your bright and tiny spark
#   Lights the traveler in the dark,
#   Though I know not what you are,
#   Twinkle, twinkle, little star.
#   '''

#   f.write(poem)









