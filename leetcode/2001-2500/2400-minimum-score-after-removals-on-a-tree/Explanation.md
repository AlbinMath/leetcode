# LeetCode 2322: Minimum Score After Removals on a Tree

**LeetCode Problem #2322 — Minimum Score After Removals on a Tree**
Solve LeetCode Minimum Score After Removals on a Tree using Java and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Score After Removals on a Tree |
| LeetCode | #2322 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

You are given a **0-indexed** integer array `nums` of length `n` where `nums[i]` represents the value of the `i^th` node. You are also given a 2D integer array `edges` of length `n - 1` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

Remove two **distinct** edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:

Get the XOR of all the values of the nodes for **each** of the three components respectively. 
 The **difference** between the **largest** XOR value and the **smallest** XOR value is the **score** of the pair.

For example, say the three components have the node values: `[4,5,7]`, `[1,9]`, and `[3,3,3]`. The three XOR values are `4 ^ 5 ^ 7 = **6** `, `1 ^ 9 = **8** `, and `3 ^ 3 ^ 3 = **3** `. The largest XOR value is `8` and the smallest XOR value is `3`. The score is then `8 - 3 = 5`.

Return *the **minimum** score of any possible pair of edge removals on the given tree*.

## Constraints
- `n == nums.length`
- `3 <= n <= 1000`
- `1 <= nums[i] <= 10^8`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]`
- **Output:** `9`
- **Explanation:** The diagram above shows a way to make a pair of removals.
- The 1^st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
- The 2^nd component has node [0] with value [1]. Its XOR value is 1 = 1.
- The 3^rd component has node [2] with value [5]. Its XOR value is 5 = 5.
The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
It can be shown that no other pair of removals will obtain a smaller score than 9.

### Example 2
- **Input:** `nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]`
- **Output:** `0`
- **Explanation:** The diagram above shows a way to make a pair of removals.
- The 1^st component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0.
- The 2^nd component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0.
- The 3^rd component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0.
The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0.
We cannot obtain a smaller score than 0.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Score After Removals on a Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** The diagram above shows a way to make a pair of removals.
- The 1^st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
- The 2^nd component has node [0] with value [1]. Its XOR value is 1 = 1.
- The 3^rd component has node [2] with value [5]. Its XOR value is 5 = 5.
The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
It can be shown that no other pair of removals will obtain a smaller score than 9.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<List<Integer>> adj;
    private int[] subXor, tin, tout;
    private int timer = 0;

    public int minimumScore(int[] nums, int[][] edges) {
        int n = nums.length;
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        subXor = new int[n];
        tin = new int[n];
        tout = new int[n];

        dfs(0, -1, nums);
        int totalXor = subXor[0];
        int ans = Integer.MAX_VALUE;

        for (int u = 1; u < n; u++) {
            for (int v = u + 1; v < n; v++) {
                int a, b, c;
                if (tin[u] < tin[v] && tout[v] <= tout[u]) {
                    a = subXor[v];
                    b = subXor[u] ^ subXor[v];
                    c = totalXor ^ subXor[u];
                } else if (tin[v] < tin[u] && tout[u] <= tout[v]) {
                    a = subXor[u];
                    b = subXor[v] ^ subXor[u];
                    c = totalXor ^ subXor[v];
                } else {
                    a = subXor[u];
                    b = subXor[v];
                    c = totalXor ^ subXor[u] ^ subXor[v];
                }
                int mx = Math.max(a, Math.max(b, c));
                int mn = Math.min(a, Math.min(b, c));
                ans = Math.min(ans, mx - mn);
            }
        }
        return ans;
    }

    private void dfs(int u, int parent, int[] nums) {
        tin[u] = ++timer;
        int val = nums[u];
        for (int v : adj.get(u)) {
            if (v != parent) {
                dfs(v, u, nums);
                val ^= subXor[v];
            }
        }
        subXor[u] = val;
        tout[u] = timer;
    }
}
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
- [3746. Minimum String Length After Balanced Removals](../../4001-4500/4090-minimum-string-length-after-balanced-removals/)
- [861. Score After Flipping Matrix](../../0501-1000/0891-score-after-flipping-matrix/)
- [1422. Maximum Score After Splitting a String](../../1501-2000/1537-maximum-score-after-splitting-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/)
