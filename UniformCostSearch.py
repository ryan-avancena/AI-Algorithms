"""

Uniform Cost Search - Uninformed

"""
import heapq            # priority queue/heap

# intializing graph
graph,cost = [[] for i in range(8)],{}
graph[0].append(1)
graph[0].append(3)
graph[3].append(1)
graph[3].append(6)
graph[3].append(4)
graph[1].append(6)
graph[4].append(2)
graph[4].append(5)
graph[2].append(1)
graph[5].append(2)
graph[5].append(6)
graph[6].append(4)
cost[(0, 1)] = 2
cost[(0, 3)] = 5
cost[(1, 6)] = 1
cost[(3, 1)] = 5
cost[(3, 6)] = 6
cost[(3, 4)] = 2
cost[(2, 1)] = 4
cost[(4, 2)] = 4
cost[(4, 5)] = 3
cost[(5, 2)] = 6
cost[(5, 6)] = 3
cost[(6, 4)] = 7

def uniform_cost_search(goal, start):
    # priority queue (min heap) for the frontier
    frontier = [(0, start)]  # (cumulative cost, node)
    
    # explored set
    explored = set()

    while frontier:
        # pop node with the smallest cost
        current_cost, current_node = heapq.heappop(frontier)
        
        # if the goal node is reached, return the cost
        if current_node in goal:
            return current_cost
        
        if current_node not in explored:
            explored.add(current_node)
            
            for neighbor in graph[current_node]:
                if neighbor not in explored:
                    total_cost = current_cost + cost[(current_node, neighbor)]
                    heapq.heappush(frontier, (total_cost, neighbor))
    
    return 

def main():
    start = 0
    goal = [6]

    answer = uniform_cost_search(goal, start)
    
    print(f'minimum cost from {start} to {goal} is {answer}')

main()