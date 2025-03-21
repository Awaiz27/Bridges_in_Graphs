import sys
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

def find_bridges(n, edges):
    def dfs(node, parent):
        nonlocal timer
        disc[node] = low[node] = timer
        timer += 1
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue  
            
            if disc[neighbor] == -1:  
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                
                if low[neighbor] > disc[node]:
                    bridges.append((min(node, neighbor), max(node, neighbor)))
            else:
                #If neighbor is already visited, it means we found a back edge (a cycle)
                low[node] = min(low[node], disc[neighbor])
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    disc = [-1] * (n + 1)
    low = [-1] * (n + 1)
    timer = 0
    bridges = []
    
    for i in range(1, n + 1):
        if disc[i] == -1:
            dfs(i, -1)
    
    bridges.sort()
    return bridges

def plot_graph(n, edges, bridges):
    G = nx.Graph()
    G.add_edges_from(edges)
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=10)
    
    bridge_edges = [(u, v) for u, v in bridges]
    nx.draw_networkx_edges(G, pos, edgelist=bridge_edges, edge_color='red', width=2)
    
    plt.title("Graph with Bridges")
    plt.show()

def main():
    sys.setrecursionlimit(10**6)
    print(" Input the no of vertices and edges in the graph(n (space) m)")
    try:
        first_line = sys.stdin.readline().strip()
        if not first_line:
            raise ValueError("Input is empty or incorrect format.")
        
        n, m = map(int, first_line.split())
        if not (1 <= n <= 10000 and 1 <= m <= 10**6):
            raise ValueError("n or m is out of bounds.")
        
        edges = []
        print(" Input the edges of the graph(u (space) v)")
        for _ in range(m):
            line = sys.stdin.readline().strip()
            if not line:
                raise ValueError("Edge input missing or incorrect format.")
            u, v = map(int, line.split())
            if not (1 <= u < v <= n):
                raise ValueError("Edge values out of bounds or incorrectly formatted.")
            edges.append((u, v))
        
        bridges = find_bridges(n, edges)
        
        print("There are {} bridges in the graphs".format(len(bridges)))
        for u, v in bridges:
            print(u, v)
        
        plot_graph(n, edges, bridges)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
