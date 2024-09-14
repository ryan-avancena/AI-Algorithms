from collections import deque

"""

Breadth First Search - Uninformed

"""

def add_edge(adj, s, t):
    adj[s].append(t)
    adj[t].append(s)

def bfs(adj, source):
    visited = [False] * len(adj)
    
    queue = deque([source])

    visited[source] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for neighbor in adj[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

def main():
    V = 5  

    adj = [[] for _ in range(V)]  

    edges = [
        [1, 2], 
        [1, 0], 
        [2, 0], 
        [2, 3], 
        [2, 4]
    ]

    for e in edges:
        add_edge(adj, e[0], e[1])

    print(f'Adjacency List: {adj}')

    source = 1
    print("BFS from source:", source)
    bfs(adj, source)

main()
