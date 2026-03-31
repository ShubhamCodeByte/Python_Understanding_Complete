"""
1. Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!

"""

hindiToEnglish = {
    "namaste": "hello",
    "shukriya": "thank you",
    "paani": "water",
    "khana": "food",
    "dost": "friend"
}

search = input("Enter the hindi word to search : ")

print(hindiToEnglish[search])  # Enter the hindi word to search : namaste
                               # hello

