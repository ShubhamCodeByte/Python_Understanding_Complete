"""
4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?


Ans : 2
"""


s = set()
s.add(20)
s.add(20.0)
s.add('20')

length = len(s)
print(length)       # 2