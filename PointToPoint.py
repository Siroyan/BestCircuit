import math
import itertools

A = (0,0)
B = (3,4)

x = B[0] - A[0]
y = B[1] - A[1]

#[x,---,x,y,---,y]の形式
base_list = []
for i in range(0,x):
    base_list.append(1)
for i in range(0,y):
    base_list.append(0)

#base_listから全最短経路をlistで格納
all_ways = list(set(list(itertools.permutations(base_list))))
