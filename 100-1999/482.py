#Run Time: 0.040
from collections import OrderedDict

numOfcases = int(input())

for n in range(numOfcases):
    input()
    index_array = input().split()
    value_array = input().split()

    index_dict = {}
    for i in range(len(index_array)):
        index_dict[i] = int(index_array[i])
    sort_index_dict = OrderedDict(sorted(index_dict.items(), key=lambda t: t[1]))

    for k in sort_index_dict.keys():
        print(value_array[k])

    if n != numOfcases - 1:
        print()
