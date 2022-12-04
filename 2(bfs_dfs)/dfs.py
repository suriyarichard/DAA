graph = {
  '5' : ['13','7'],
  '13' : ['2', '4','5'],
  '7' : ['11'],
  '2' : [],
  '4' : ['13'],
  '11' : ['4','35','7'],
  '45':['11'],
  '35':['11']
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node,end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, '11')
