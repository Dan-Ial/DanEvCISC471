def indices(N, d):
    list = [0 for x in range(d)]
    if d != 0:
        indices_recurse(N, d, list, 1)

def indices_recurse(N, d, list, index):
    if index == len(list):
        for i in range(N + 1):
            print(list)  # print a unit of output
            list[index-1] += 1
        list[index-1] = 0
    else:
        for i in range(N + 1):
            indices_recurse(N, d, list, index+1)
            list[index-1] += 1
        list[index-1] = 0

indices(2, 2)
