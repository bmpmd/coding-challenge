import statistics as st

def medianOfArr(*arg0):
    list = []
    for i in arg0:
        list+= i
    print(st.median(list))

medianOfArr([1,3], [2])
medianOfArr([1, 2], [3, 4] )

def mergeLists(*arg0):
    list = []
    for i in arg0:
        list.extend(i)
    list = sorted(list)
    print(list)

mergeLists([1,4,5],[1,3,4],[2,6])
mergeLists()
mergeLists([])

