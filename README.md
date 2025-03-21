# Finding Bridges in an Undirected Graph

## 📌 Introduction
This repository contains an implementation of **Tarjan's Algorithm** to efficiently find **bridges** (articulation edges) in an **undirected graph** using **Depth-First Search (DFS)**.

A **bridge** in a graph is an edge that, when removed, increases the number of connected components.

## 🖥️ Algorithm Explanation
We use **Tarjan’s Algorithm** to compute **discovery times** and **low-link values** for each node during a **DFS traversal**. An edge **(u, v)** is identified as a **bridge** if:

                low[v] > disc[u]

This means node v cannot reach an ancestor of u, indicating that **removing (u, v) disconnects the graph**.

### **Time Complexity:**  
- **DFS Traversal:** \( O(V + E) \)
- **Sorting Bridges:** \( O(m' \log m') \)
- **Total Complexity:** \( O(V + E + m' \log m') \)

---

## 📜 Pseudocode
```python
def findBridges(graph, n):
    time = 0
    bridges = []
    disc = [-1] * n  # Discovery time
    low = [-1] * n   # Lowest discovery time reachable
    visited = set()

    def DFS(u, parent):
        nonlocal time
        disc[u] = low[u] = time
        time += 1
        visited.add(u)

        for v in graph[u]:  
            if disc[v] == -1:  # If v is unvisited
                DFS(v, u)
                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:  
                    bridges.append((min(u, v), max(u, v)))

            elif v != parent:  
                low[u] = min(low[u], disc[v])  

    for u in range(n):
        if disc[u] == -1:
            DFS(u, -1)

    bridges.sort()  
    return bridges

## Figures

### Figure 1: Test Case 1
![Figure 1](images/figure1.png)

### Figure 2: Tese Case 2
![Figure 2](images/figure2.png)

### Figure 3: Test Case 3
![Figure 3](images/figure3.png)

