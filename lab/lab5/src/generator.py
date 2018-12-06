import random
l = [10, 100, 1000, 10000, 100000]
for num in l:
    with open('../'+ str(num) + 'scale.txt', 'w') as f:
        for i in range(num):
            n = 2
            if num >= 1000:
                n = 8
            f.write(str(int(random.random()*num/n)) + ' ' + str(int(random.random()*num/n)) + '\n')
