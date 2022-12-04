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

visited = [] 
queue = []    

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:         
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, '11')   
