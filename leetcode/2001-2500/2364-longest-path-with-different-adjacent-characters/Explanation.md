# LeetCode 2246: Longest Path With Different Adjacent Characters

**LeetCode Problem #2246 — Longest Path With Different Adjacent Characters**
Solve LeetCode Longest Path With Different Adjacent Characters using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Path With Different Adjacent Characters |
| LeetCode | #2246 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **tree** (i.e. a connected, undirected graph that has no cycles) **rooted** at node `0` consisting of `n` nodes numbered from `0` to `n - 1`. The tree is represented by a **0-indexed** array `parent` of size `n`, where `parent[i]` is the parent of node `i`. Since node `0` is the root, `parent[0] == -1`.

You are also given a string `s` of length `n`, where `s[i]` is the character assigned to node `i`.

Return *the length of the **longest path** in the tree such that no pair of **adjacent** nodes on the path have the same character assigned to them.*

## Constraints
- `n == parent.length == s.length`
- `1 <= n <= 10^5`
- `0 <= parent[i] <= n - 1` for all `i >= 1`
- `parent[0] == -1`
- `parent` represents a valid tree.
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `parent = [-1,0,0,1,1,2], s = "abacbe"`
- **Output:** `3`
- **Explanation:** The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions.

### Example 2
- **Input:** `parent = [-1,0,0,0], s = "aabc"`
- **Output:** `3`
- **Explanation:** The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Path With Different Adjacent Characters**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `parent = [-1,0,0,1,1,2], s = "abacbe"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions.

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
/**
 * @param {number[]} parent
 * @param {string} s
 * @return {number}
 */
var longestPath = function (parent, s) {
    const n = parent.length;
    const childCnt = new Int32Array(n);
    for (let i = 1; i < n; i++) childCnt[parent[i]]++;

    const top1 = new Int32Array(n);
    const top2 = new Int32Array(n);

    const queue = [];
    for (let i = 0; i < n; i++) if (childCnt[i] === 0) queue.push(i);

    let ans = 1, head = 0;
    while (head < queue.length) {
        const u = queue[head++];
        const best = 1 + top1[u];
        const through = 1 + top1[u] + top2[u];
        if (through > ans) ans = through;

        const p = parent[u];
        if (p === -1) continue;

        if (s.charCodeAt(u) !== s.charCodeAt(p)) {
            if (best > top1[p]) {
                top2[p] = top1[p];
                top1[p] = best;
            } else if (best > top2[p]) {
                top2[p] = best;
            }
        }
        if (--childCnt[p] === 0) queue.push(p);
    }
    return ans;
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
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [395. Longest Substring with At Least K Repeating Characters](../../0001-0500/0395-longest-substring-with-at-least-k-repeating-characters/)
- [3970. Shortest Path With At Most K Consecutive Identical Characters](../../4001-4500/4104-shortest-path-with-at-most-k-consecutive-identical-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-path-with-different-adjacent-characters/)
