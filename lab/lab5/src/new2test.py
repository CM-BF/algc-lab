import bintrees
t = bintrees.FastRBTree()
t[1] = [2, 3, 4]
try:
    t[2]
print(t)