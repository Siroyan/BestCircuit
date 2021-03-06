import math
import itertools

bestRoute = []
coordinates = []
Ax = 0
Ay = 0
Bx = 3
By = 4

def getCoordinates(Ax,Ay,Bx,By):
    A = (Ax,Ay)
    B = (Bx,By)

    x = abs(B[0] - A[0])
    y = abs(B[1] - A[1])

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
            else:#angle
                way_result[1] += 1
        results_set.append(way_result)

    point = []
    point_str = 1 #直進ポイント
    point_ang = -1 #直角ポイント
    #全ルートに対しポイントをつけ、評価
    for i in range(0,len(all_ways)):
        point.append( results_set[i][0]*point_str + results_set[i][1]*point_ang )
    #ポイントが最大のものを抽出
    best_route_index = [i for i, x in enumerate(point) if x == max(point)]
    #ポイント最大のルートを表示
    for i in best_route_index:
        bestRoute.append(all_ways[i])
#移動の1,0を座標に変換
    for i in range (0,7):#TODO
        if bestRoute[0][i] == 1:
            Ax += 1
        else:
            Ay += 1
        coordinates.append([Ax,Ay])
    return coordinates
