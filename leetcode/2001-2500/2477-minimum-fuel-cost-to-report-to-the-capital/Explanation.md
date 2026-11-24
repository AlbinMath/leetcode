# LeetCode 2477: Minimum Fuel Cost to Report to the Capital

**LeetCode Problem #2477 — Minimum Fuel Cost to Report to the Capital**
Solve LeetCode Minimum Fuel Cost to Report to the Capital using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Fuel Cost to Report to the Capital |
| LeetCode | #2477 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of `n` cities numbered from `0` to `n - 1` and exactly `n - 1` roads. The capital city is city `0`. You are given a 2D integer array `roads` where `roads[i] = [a_i, b_i]` denotes that there exists a **bidirectional road** connecting cities `a_i` and `b_i`.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer `seats` that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return *the minimum number of liters of fuel to reach the capital city*.

## Constraints
- `1 <= n <= 10^5`
- `roads.length == n - 1`
- `roads[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- `roads` represents a valid tree.
- `1 <= seats <= 10^5`

## Examples
### Example 1
- **Input:** `roads = [[0,1],[0,2],[0,3]], seats = 5`
- **Output:** `3`
- **Explanation:** - Representative_1 goes directly to the capital with 1 liter of fuel.
- Representative_2 goes directly to the capital with 1 liter of fuel.
- Representative_3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum. 
It can be proven that 3 is the minimum number of liters of fuel needed.

### Example 2
- **Input:** `roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2`
- **Output:** `7`
- **Explanation:** - Representative_2 goes directly to city 3 with 1 liter of fuel.
- Representative_2 and representative_3 go together to city 1 with 1 liter of fuel.
- Representative_2 and representative_3 go together to the capital with 1 liter of fuel.
- Representative_1 goes directly to the capital with 1 liter of fuel.
- Representative_5 goes directly to the capital with 1 liter of fuel.
- Representative_6 goes directly to city 4 with 1 liter of fuel.
- Representative_4 and representative_6 go together to the capital with 1 liter of fuel.
It costs 7 liters of fuel at minimum. 
It can be proven that 7 is the minimum number of liters of fuel needed.

### Example 3
- **Input:** `roads = [], seats = 1`
- **Output:** `0`
- **Explanation:** No representatives need to travel to the capital city.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Fuel Cost to Report to the Capital**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `roads = [[0,1],[0,2],[0,3]], seats = 5`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** - Representative_1 goes directly to the capital with 1 liter of fuel.
- Representative_2 goes directly to the capital with 1 liter of fuel.
- Representative_3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum. 
It can be proven that 3 is the minimum number of liters of fuel needed.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minimumFuelCost = function(roads, seats) {
    const n = roads.length + 1;

    if (n === 1) return 0;

    // Build adjacency list.
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of roads) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Step 1: Build parent relationships and DFS order.
    const parent = new Array(n).fill(-1);
    const order = [0];

    parent[0] = -2;

    for (let i = 0; i < order.length; i++) {
        const u = order[i];

        for (const v of graph[u]) {
            if (v === parent[u]) continue;

            parent[v] = u;
            order.push(v);
        }
    }

    // Each city initially has one representative.
    const people = new Array(n).fill(1);

    let fuel = 0;

    // Step 2: Process nodes from leaves to root.
    for (let i = order.length - 1; i > 0; i--) {
        const u = order[i];
        const p = parent[u];

        // Cars needed to move people from u to its parent.
        fuel += Math.ceil(people[u] / seats);

        // Add subtree representatives to the parent.
        people[p] += people[u];
    }

    return fuel;
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1130-minimum-cost-tree-from-leaf-values/)
- [1217. Minimum Cost to Move Chips to The Same Position](../../1001-1500/1217-minimum-cost-to-move-chips-to-the-same-position/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/)
