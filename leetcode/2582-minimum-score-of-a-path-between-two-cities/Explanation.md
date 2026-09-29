# Minimum Score Of A Path Between Two Cities

## Problem Explanation
Find the minimum edge weight on any path between city 1 and city n. You can revisit nodes and edges.

## How the Code Works
Since you can traverse any edge multiple times, the answer is the minimum edge weight in the connected component containing cities 1 and n. Use **BFS/DFS** or **Union-Find** to find all reachable nodes from city 1 and track the minimum edge weight.
