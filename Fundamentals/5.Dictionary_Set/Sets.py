""" Sets Theory """

"""
Set is a collection of non-repetitive elements.

data types containing unique values.

Sets can only contain hashable objects.

PROPERTIES OF SETS
1. Sets are unordered => Element’s order doesn’t matter
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.

OPERATIONS ON SETS
Consider the following set:
s = {1,8,2,3}
• len(s): Returns 4, the length of the set
• s.remove(8): Updates the set s and removes 8 from s.
• s.pop(): Removes an arbitrary element from the set and return the element
removed.
• s.clear():empties the set s.
• s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}.
• s.intersection({8,11}): Return a set which contains only item in both sets {8}.

"""

s = {1,5,2,6}

# Checking the properties
# print(s[1])   # we cannot index the set 

# Empty Set 

e = set() # don't use the {} to create as it create the empty dictionary

repeat = {34,34,2,1,3,2,1,6,7,3,2}

print(repeat)  # output {1, 2, 34, 3, 6, 7}   #this is unordered

# we can use different data types

new_set = {"name",1,54,"shubham"}


r = {34,2,1,3,2,1,7,3,2}

""" Methods of set """

length = len(r)
print(length)        # Output: 5

r.add(567)
print(r)             # {1, 2, 34, 3, 567, 7}

r.remove(567)
print(r)             # {1, 2, 34, 3, 7}


# r.pop(2)           # this will fail as it dont take any argument
r.pop()              # this will remove the random value  
print(r)             # {2, 34, 3, 7}


rUnion = r.union(s)
print(rUnion)        # {1, 2, 3, 34, 5, 6, 7}

rIntersection = r.intersection(s)
print(rIntersection) # {2}


""" 
Theory :

Subset of the set 
we can do - and +

"""
# repeat = {34,34,2,1,3,2,1,6,7,3,2}
# r = {34,2,1,3,2,1,7,3,2}

print(r-repeat)          # set()  empty 
print(repeat-r)          # {1, 6}
# print(r+repeat)   this is not pssible to do + for the sets




