"""

3. Can we have a set with 18 (int) and '18' (str) as a value in it?

Ans yes

"""


integers = {1,3,5,6,7,7,34,6}
strings = {"s","surf","shio","thing","thory"}


finalCombo = integers.union(strings)
print(finalCombo)                    # {1, 34, 3, 'thory', 5, 6, 7, 's', 'shio', 'surf', 'thing'}

