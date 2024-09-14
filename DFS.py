"""

Depth First Search - Uninformed

"""

def add_edge(adj, s, t):
    adj[s].append(t)
    adj[t].append(s)


def dfs_util(v, visited, adj):
    visited[v] = True
    print(v, end=' ')

    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfs_util(neighbor, visited, adj)

def dfs(adj, source):
    visited = [False] * len(adj)
    dfs_util(source, visited, adj)


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

    # populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    print(f'Adjacency List: {adj}')

    source = 1
    print("DFS from source:", source)
    dfs(adj, source)


main()