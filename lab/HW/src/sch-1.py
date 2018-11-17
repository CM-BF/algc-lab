"""
Author: Citrine
Date: 17th November , 2018
Description: Sch2-1：工作分配问题
设有n件工作要分配给n个人去完成，将工作i分配给第j个人所需费用为。试设计一个算法，为每个人分配1件不同的工作，并使总费用达到最小。
"""

MAX = 10000


def distribute(c, x, n, current):
    global min_sum
    global min
    if current >= n:
        # print(x)
        sum = 0
        for j in range(n):
            sum += c[j][x[j]]
        if sum < min_sum:
            min_sum = sum
            min = [y for y in x]
        return None
    for i in range(n):
        if i not in x:
            x[current] = i
            distribute(c, x, n, current+1)
            x[current] = -1
    return None

filename = "../in.txt"
file = open(filename, "r")
n = int(file.readline().split('\n')[0])
# print(n)
c = []
for i in range(n):
    L = file.readline().split('\n')[0]
    L = L.split(' ')
    L = [int(x) for x in L]
    c.append(L)
# print(c)
x = [-1 for i in range(n)]
min = [-1 for i in range(n)]
min_sum = 10000
distribute(c, x, n, 0)
print(min, "\n", min_sum)

