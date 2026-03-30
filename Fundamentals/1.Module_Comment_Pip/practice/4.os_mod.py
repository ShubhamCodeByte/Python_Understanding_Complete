# 4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 


import os

# Define the path
path = '.'

# Get and print the contents
files_and_folders = os.listdir(path)

for item in files_and_folders:
    print(item)


"""
output :

PS E:\Professional\Technical\AiEngineering\Python_Understanding_Complete\Fundamentals\1.Module_Comment_Pip\practice> python -u "e:\Professional\Technical\AiEngineering\Python_Understanding_Complete\Fundamentals\1.Module_Comment_Pip\practice\4.os_mod.py"
1.print_twinkle_poem.py
2.repl_print_table.py
3.external_mod.py
4.os_mod.py
5.comment.py
"""