# LeetCode 2867: Count Valid Paths in a Tree

**LeetCode Problem #2867 — Count Valid Paths in a Tree**
Solve LeetCode Count Valid Paths in a Tree using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Valid Paths in a Tree |
| LeetCode | #2867 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is an undirected tree with `n` nodes labeled from `1` to `n`. You are given the integer `n` and a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i` in the tree.

Return *the **number of valid paths** in the tree*.

A path `(a, b)` is **valid** if there exists **exactly one** prime number among the node labels in the path from `a` to `b`.

**Note** that:

The path `(a, b)` is a sequence of **distinct** nodes starting with node `a` and ending with node `b` such that every two adjacent nodes in the sequence share an edge in the tree. 
 Path `(a, b)` and path `(b, a)` are considered the **same** and counted only **once**.

## Constraints
- `1 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `1 <= u_i, v_i <= n`
- The input is generated such that `edges` represent a valid tree.

## Examples
### Example 1
- **Input:** `n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]`
- **Output:** `4`
- **Explanation:** The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2. 
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (2, 4) since the path from 2 to 4 contains prime number 2.
It can be shown that there are only 4 valid paths.

### Example 2
- **Input:** `n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]`
- **Output:** `6`
- **Explanation:** The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2.
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (1, 6) since the path from 1 to 6 contains prime number 3.
- (2, 4) since the path from 2 to 4 contains prime number 2.
- (3, 6) since the path from 3 to 6 contains prime number 3.
It can be shown that there are only 6 valid paths.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Valid Paths in a Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2. 
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (2, 4) since the path from 2 to 4 contains prime number 2.
It can be shown that there are only 4 valid paths.

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
var countPaths = function(n, edges) {
    // Step 1: Sieve of Eratosthenes
    const isPrime = new Uint8Array(n + 1).fill(1);
    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= n; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // Step 2: Build adjacency list
    const graph = Array.from({ length: n + 1 }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Step 3: Find sizes of non-prime components
    const componentSize = new Int32Array(n + 1);
    const visited = new Uint8Array(n + 1);

    for (let node = 1; node <= n; node++) {
        if (isPrime[node] || visited[node]) continue;

        let size = 0;
        const stack = [node];
        visited[node] = 1;

        while (stack.length > 0) {
            const curr = stack.pop();
            size++;

            for (const next of graph[curr]) {
                if (!isPrime[next] && !visited[next]) {
                    visited[next] = 1;
                    stack.push(next);
                }
            }
        }

        // Assign the component size to its nodes
        const nodes = [node];
        const seen = new Set(nodes);

        while (nodes.length > 0) {
            const curr = nodes.pop();
            componentSize[curr] = size;

            for (const next of graph[curr]) {
                if (!isPrime[next] && !seen.has(next)) {
                    seen.add(next);
                    nodes.push(next);
                }
            }
        }
    }

    // Step 4: Count paths containing exactly one prime
    let answer = 0;

    for (let prime = 2; prime <= n; prime++) {
        if (!isPrime[prime]) continue;

        let total = 0;

        for (const neighbor of graph[prime]) {
            if (isPrime[neighbor]) continue;

            const size = componentSize[neighbor];

            // Paths from this prime to this component
            answer += size;

            // Paths connecting two different components
            answer += total * size;

            total += size;
        }
    }

    return answer;
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
- [2791. Count Paths That Can Form a Palindrome in a Tree](../../2501-3000/2905-count-paths-that-can-form-a-palindrome-in-a-tree/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)
- [257. Binary Tree Paths](../../0001-0500/0257-binary-tree-paths/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-valid-paths-in-a-tree/)
