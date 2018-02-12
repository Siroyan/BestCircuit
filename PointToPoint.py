import math
import itertools

A = (0,0)
B = (3,4)

x = B[0] - A[0]
y = B[1] - A[1]

#[1,---,1,0,---,0]の形式
#1 <-> x方向
#0 <-> y方向
base_list = []
for i in range(0,x):
    base_list.append(1)
for i in range(0,y):
    base_list.append(0)

#base_listから全最短経路をall_waysに格納
all_ways = list(set(list(itertools.permutations(base_list))))
results_set = []
#全ルートに対し、直進,直角の回数を調べ,results_setに格納
for i in range(0,len(all_ways)):
    #[直進回数,直角回数]
    way_result = [0,0]
    for j in range(0,len(all_ways[i])-1):
        if all_ways[i][j] == all_ways[i][j+1]:#straight
            way_result[0] += 1
            #print('straight')
        else:#angle
            way_result[1] += 1
            #print('angle')
    results_set.append(way_result)
    print(way_result)
