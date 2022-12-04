nV = 4
INF = 999

def floyd(G):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))
    # print(dist)

    for r in range(nV):
        print("Iteration-",r)
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
                print(dist[p][q], end="  ")
            print(" ")
        print(" ")
    sol(dist)

def sol(dist):
    print("Final matrix: ")
    for p in range(nV):
        for q in range(nV):
            # if(dist[p][q] == INF):
            #     print("INF", end=" ")
            # else:
                
            print(dist[p][q], end="  ")
        print(" ")

G = [[0, 3, INF, 7],
         [8, 0, 2, INF],
         [5, INF, 0, 1],
         [2, INF, INF, 0]]
floyd(G)
