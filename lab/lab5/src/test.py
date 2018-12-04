import linecache
import queue
import time

Q = queue.Queue()
filename = "../twitter_large.txt"
file = open(filename, "r")
edges = {}
sides = []
line = file.readline()
signal = ' '
# create a index for u in file
begin_time = time.time()
def binary_search_loop(lst,value):
    low, high = 0, len(lst)-1
    value = int(value)
    while low <= high:
        mid = (low + high) // 2
        x = int(lst[mid][0])
        if x < value:
            low = mid + 1
        elif x > value:
            high = mid - 1
        else:
            return mid
    return None

if filename != '../twitter_large.txt':
    while(line != ''):
        line = line.strip('\n')
        line = line.split(signal)
        u = line[0]
        v = line[1]
        sides.append([u, v])
        line = file.readline()
    print(sides[0])

    sides = sorted(sides, key=lambda x: int(x[0]))
    sides_temp = []
    key = ''
    for i in range(len(sides)):
        if key != sides[i][0]:
            key = sides[i][0]
            sides_temp.append([key])
        sides_temp[-1].append(sides[i][1])
    sides = sides_temp

else:
    signal = ','
    key = ''
    while (line != ''):
        line = line.strip('\n')
        line = line.split(signal)
        u = line[0]
        v = line[1]
        if key != u:
            key = u
            sides.append([key])
        sides[-1].append(v)
        line = file.readline()
    print(sides[0])
    sides = sorted(sides, key=lambda x: int(x[0]))


def BFS(s):
    index = binary_search_loop(sides, s)
    Q.put((sides[index], '0'))
    del sides[index]
    visited = 1
    d = 0
    while not Q.empty():
        tuple = Q.get()
        u = tuple[0][0]
        ud = tuple[1]
        if int(ud) != d:
            print('')
            d = int(ud)
        list = tuple[0]
        del list[0]
        for v in list:
            visited += 1
            # if visited % 1000000 == 0:
            # print(visited)
            begin = time.time()
            index = binary_search_loop(sides, v) # not waste time
            end = time.time()
            print(end - begin, end=' ')
            if index != None:
                Q.put((sides[index], str(d+1)))
                begin = time.time()
                del sides[index]
                end = time.time()
                print(end - begin, end=' ')
            print('')
        print('Qsize: ', Q.qsize())
    print(visited)


print(sides[0])
BFS_begin_time = time.time()
BFS(sides[0][0])
end_time = time.time()

print('total time:', end_time-begin_time, '\nBFS time:', end_time-BFS_begin_time)