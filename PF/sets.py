'''
set is a collection of non-repeate elements
it doesnot maintain order
unordered
unindexed
don't change items in sets
'''

e=set() # empty set

s={2,4,5,8}


# print(s)
# ss={3,4,6,3,5,2,1,3}
# print(ss) # {1, 2, 3, 4, 5, 6}

# ------------------------------------Methods of Sets------------------------------------------------------------------

s={2,4,5,8,"Shah"}
s.add(4567)
# print(s)
# print(len(s))
# s.remove(5)
# print(s)
# --------------------------------------------------------
# union
s1={2,4,6,7}
s2={3,5,6,89,1}

print("Union of 2 sets",s1.union(s2))
print("Intersection of 2 sets",s1.intersection(s2))



