"""
Author: Citrine
Date: 17th November, 2018
Description: Sch2-2：最佳调度问题
设有n个任务由k个可并行工作的机器来完成，完成任务i需要时间为ti。试设计一个算法找出完成这n个任务的最佳调度，使完成全部任务的时间最早。（要求给出调度方案）
"""
MAX = 10000
import time

def pre_compute(current):
    global machine, t, n, k, min, min_sum, x, machinetime
    if current >= n:
        max_machinetime = max(machinetime)
        if max_machinetime < min_sum:
            min_sum = max_machinetime
            min = [key for key in x]
            print(min, min_sum)
        # print(x)
        return None
    # maxm = max(machinetime)
    # if maxm > min_sum:
    #     # print(current, maxm)
    #     return None
    L = sorted(enumerate(machinetime), key=lambda x: x[1])
    L = [x[0] for x in L]
    i = L[0]
    x[current] = i
    machine[i].append(t[current])
    machinetime[i] += t[current]
    pre_compute(current + 1)
    machinetime[i] -= t[current]
    machine[i].pop()
    x[current] = -1
    return None

def distribute(current):
    global machine, t, n, k, min, min_sum, x, machinetime
    if current >= n:
        max_machinetime = max(machinetime)
        if max_machinetime < min_sum:
            min_sum = max_machinetime
            min = [key for key in x]
            print(min, min_sum)
        # print(x)
        return None
    # maxm = max(machinetime)
    # if maxm > min_sum:
    #     # print(current, maxm)
    #     return None
    # L = sorted(enumerate(machinetime), key=lambda x: x[1])
    # L = [x[0] for x in L]
    # print(L)
    for i in range(k):
        # i = L[i]
        i = (i + current)%k
        if current==0:
            print('next:', i)
        x[current] = i
        machine[i].append(t[current])
        machinetime[i] += t[current]
        if machinetime[i] < min_sum:
            distribute(current + 1)
        machinetime[i] -= t[current]
        machine[i].pop()
        x[current] = -1
    return None

filename = "../in2_3.txt"
file = open(filename, "r")
n = file.readline().split("\n")[0].split(" ")
k = int(n[1])
n = int(n[0])
t = file.readline().split("\n")[0].split(" ")
t = [int(x) for x in t]
t = sorted(t, key=lambda x: x, reverse=True)
print(t)
# print(n, k, t)
x = [-1 for i in range(n)]
machine = [[] for i in range(k)]
machinetime = [0 for i in range(k)]
min = [-1 for i in range(n)]
min_sum = MAX
pre_compute(0)
begin_time = time.time()
flag = False
maxi = 0
for i in range(n):
    for j in range(i):
        if machinetime[j] + t[i] < min_sum:
            maxi = i
            flag = True
        if flag:
            break
    if flag:
        break
    x[i] = i
    machine[i].append(t[i])
    machinetime[i] += t[i]
print(maxi)
distribute(maxi)
end_time = time.time()
print(min, '\n', min_sum)
print(end_time-begin_time)

