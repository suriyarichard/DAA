check = 9999999
N = 5
Graph = [[0, 2, 0, 6, 0],
         [0, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]
print("prims algorithm:")
selected_node = [0, 0, 0, 0, 0]
no_edge = 0
cost = 0
selected_node[0] = True
# printing for edge and weight
print("Edge : Weight\n")
while no_edge < N - 1:
    minimum = check
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if (not selected_node[n]) and Graph[m][n]:
                    # not in selected and there is an edge
                    if minimum > Graph[m][n]:
                        minimum = Graph[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + " " + str(Graph[a][b]))
    selected_node[b] = True
    cost = cost + Graph[a][b]
    no_edge += 1
print("The cost is : ", cost)