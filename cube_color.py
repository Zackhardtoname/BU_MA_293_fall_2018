# bottom front left back right top
res = []

def rotate(i):  # counterclockwise
    return [i[0]] + i[2:5] + [i[1]] + [i[5]]

def flip_back(i):  # towards the back
    return [i[3], i[0], i[2], i[5], i[4], i[1]]

def flip_left(i):  # towards the left
    return [i[2], i[1], i[5], i[3], i[0], i[4]]

import itertools

everything = list(itertools.permutations(range(1, 7)))


def check(li):
    li = list(li)
    for i in range(4):
        li = rotate(li)
        if li in res:
            return False
    for i in range(4):
        li = flip_back(li)
        if li in res:
            return False
        for i in range(4):
            li = rotate(li)
            if li in res:
                return False
    for i in range(4):
        li = flip_left(li)
        if li in res:
            return False
        for i in range(4):
            li = rotate(li)
            if li in res:
                return False
    return True


for li in everything:
    if check(li):
        res.append(list(li))
print(len(res))