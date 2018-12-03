import linecache
import queue

Q = queue.Queue()
filename = "../twitter_large.txt"
file = open(filename, "r")
edges = {}
sides = []
line = file.readline()
# create a index for u in file
count = 0
while(line != ''):
    count += 1
    line = line.strip('\n')
    line = line.split(',')
    u = line[0]
    if not(u in edges.keys()):
        edges[u] = count
    line = file.readline()


def BFS(s):
    Q.put((s, 0))
    visited = 1
    d = 0
    while not Q.empty():
        tuple = Q.get()
        u = tuple[0]
        ud = tuple[1]
        if ud != d:
            print('')
            d = ud
        list = []
        if not(u in edges.keys()):
            continue
        count = edges[u]
        line = linecache.getline(filename, count)
        line = line.strip('\n')
        line = line.split(',')
        while u == line[0]:
            list.append(line[1])
            count += 1
            line = linecache.getline(filename, count)
            line = line.strip('\n')
            line = line.split(',')
        for v in list:
            visited += 1
            print(visited)
            Q.put((v, d+1))
        linecache.clearcache()
        edges.pop(u)


line = linecache.getline(filename, 1)
line = line.strip('\n').split(',')
BFS(line[0])