import random

r = random.seed(1000)

q = []



def prob(num):
    i = 0
    m = 0
    g = 0
    for i in range(num):



        q.append(f"{random.random()}-{random.random()}*{random.random()}")
        i+=1
        g+=1
        m+=1

prob(100)

for i in range(100):
    print(q[i])