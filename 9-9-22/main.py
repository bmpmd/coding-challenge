def findGap(*arg0):
    list = []
    for i in arg0:
        list+= i
    list = sorted(list)
    print(list.pop() - list[0])

findGap([3, 10, 6, 7])
findGap([-3, -1, 6, 7, 0])
