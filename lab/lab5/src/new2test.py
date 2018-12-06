import linecache
import queue
import time
import sys
import bintrees

Q = queue.Queue()
name = ['10scale', '100scale', '1000scale', '10000scale', '100000scale', 'twitter_small', 'twitter_large']
filename = "../"+ name[6] +".txt"
file = open(filename, "r")
edges = {}
# sides = bintrees.FastRBTree()
sides = {}
line = file.readline()
signal = ' '
visited = 0
# create a index for u in file
begin_time = time.time()


if True:
    if filename == "../twitter_large.txt":
        signal = ','
    # lines = file.readlines()
    print('begin deal')
    while line != '':
        line = line.strip('\n')
        line = line.split(signal)
        u = line[0]
        v = line[1]
        if sides.__contains__(u):
            sides[u].append(v)
        else:
            sides[u] = [v]
        line = file.readline()
file.close()
    # del lines

    # sides = sorted(sides, key=lambda x: int(x[0]))
    # sides_temp = []
    # key = ''
    # for i in range(len(sides)):
    #     if key != sides[i][0]:
    #         key = sides[i][0]
    #         sides_temp.append([key])
    #     sides_temp[-1].append(sides[i][1])
    # s = sides_temp[0][0]
    # sides = bintrees.FastRBTree()
    # for side in sides_temp:
    #     sides.insert(side[0], side[1:])

# else:
#     signal = ','
#     key = ''
#     while (line != ''):
#         line = line.strip('\n')
#         line = line.split(signal)
#         u = line[0]
#         v = line[1]
#         if key != u:
#             key = u
#             sides.append([key])
#         sides[-1].append(v)
#         line = file.readline()
#     print(sides[0])
#     sides = sorted(sides, key=lambda x: int(x[0]))
#     s = sides[0][0]
#     sides_temp = bintrees.FastRBTree()
#     for side in sides:
#         sides_temp.insert(side[0], side[1:])
#     sides = sides_temp


def BFS(s):
    global visited
    Q.put((s, sides[s], 0))
    del sides[s]
    print('d: ', 0)
    d = 0
    while not Q.empty():
        tuple = Q.get()
        u = tuple[0]
        ud = tuple[2]
        if ud != d:
            print('d: ', ud)
            d = ud
        list = tuple[1]
        for v in list:
            visited += 1
            # if visited % 1000000 == 0:
            # print(visited)
            if sides.__contains__(v):
                Q.put((v, sides[v], d+1))
                begin = time.time()
                del sides[v]
                end = time.time()
                # print(end - begin, end=' ')
            # print('')
        # print('Qsize: ', Q.qsize())
    print(visited)

print(sys.getsizeof(sides))
BFS_begin_time = time.time()
for s in sides.keys():
    BFS(s)
    break
if filename != "../twitter_large.txt":
    while not (not sides):
        for s in sides.keys():
            BFS(s)
            break

# c = 0
# l = 0
# for key in sides.keys():
#     import sys
#     c += 1
#     l += sys.getsizeof(sides[key])
# print("key num:", c, "  average size: ", l/c, "sides size: ", sys.getsizeof(sides))
end_time = time.time()
import sys
print('total time:', end_time-begin_time, '\nBFS time:', end_time-BFS_begin_time)
print('visited: ', visited)