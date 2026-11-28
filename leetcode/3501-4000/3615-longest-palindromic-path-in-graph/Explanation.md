# LeetCode 3615: Longest Palindromic Path in Graph

**LeetCode Problem #3615 — Longest Palindromic Path in Graph**
Solve LeetCode Longest Palindromic Path in Graph using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Palindromic Path in Graph |
| LeetCode | #3615 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` and an **undirected** graph with `n` nodes labeled from 0 to `n - 1` and a 2D array `edges`, where `edges[i] = [u_i, v_i]` indicates an edge between nodes `u_i` and `v_i`.

You are also given a string `label` of length `n`, where `label[i]` is the character associated with node `i`.

You may start at any node and move to any adjacent node, visiting each node **at most** once.

Return the **maximum** possible length of a ** palindrome ** that can be formed by visiting a set of **unique** nodes along a valid path.

## Constraints
- `1 <= n <= 14`
- `n - 1 <= edges.length <= n * (n - 1) / 2`
- `edges[i] == [u_i, v_i]`
- `0 <= u_i, v_i <= n - 1`
- `u_i != v_i`
- `label.length == n`
- `label` consists of lowercase English letters.
- There are no duplicate edges.

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1],[1,2]], label = "aba"`
- **Output:** `3`

### Example 2
- **Input:** `n = 3, edges = [[0,1],[0,2]], label = "abc"`
- **Output:** `1`
- **Explanation:** No path with more than one node forms a palindrome. 
 The best option is any single node, giving a palindrome of length 1.

### Example 3
- **Input:** `n = 4, edges = [[0,2],[0,3],[3,1]], label = "bbac"`
- **Output:** `3`
- **Explanation:** The longest palindromic path is from node 0 to node 1, following the path `0 &rarr; 3 &rarr; 1`, forming string `"bcb"`. 
 This is a valid palindrome of length 3.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Palindromic Path in Graph**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1],[1,2]], label = "aba"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxLen = function(n, edges, label) {
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const totalStates = (1 << n) * n * n;
    const visited = new Uint8Array(totalStates);

    let answer = 1;

    function dfs(mask, u, v, len) {
        const key = (mask * n + u) * n + v;

        if (visited[key]) return;
        visited[key] = 1;

        answer = Math.max(answer, len);

        // Expand both endpoints.
        for (const x of graph[u]) {
            if (mask & (1 << x)) continue;

            for (const y of graph[v]) {
                if (mask & (1 << y)) continue;
                if (x === y) continue;

                // Both new endpoints must have matching labels.
                if (label[x] !== label[y]) continue;

                const newMask = mask | (1 << x) | (1 << y);

                // Store endpoints in a canonical order.
                const a = Math.min(x, y);
                const b = Math.max(x, y);

                dfs(newMask, a, b, len + 2);
            }
        }
    }

    // Odd-length palindromes: start from one vertex.
    for (let i = 0; i < n; i++) {
        dfs(1 << i, i, i, 1);
    }

    // Even-length palindromes: start from an edge
    // whose endpoint labels are equal.
    for (const [u, v] of edges) {
        if (label[u] === label[v]) {
            const mask = (1 << u) | (1 << v);

            const a = Math.min(u, v);
            const b = Math.max(u, v);

            dfs(mask, a, b, 2);
        }
    }

    return answer;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [516. Longest Palindromic Subsequence](../../0501-1000/0516-longest-palindromic-subsequence/)
- [3841. Palindromic Path Queries in a Tree](../../3501-4000/3841-palindromic-path-queries-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-palindromic-path-in-graph/)
