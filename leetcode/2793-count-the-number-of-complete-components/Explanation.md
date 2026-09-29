# Count The Number Of Complete Components

## Problem Explanation
Find the number of connected components where every pair of nodes is directly connected (i.e., the component is a complete graph).

## How the Code Works
Use **BFS/DFS or Union-Find** to find connected components. For each component with `v` vertices and `e` edges, it's complete if `e == v*(v-1)/2`.
