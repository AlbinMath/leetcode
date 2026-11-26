# LeetCode 3331: Find Subtree Sizes After Changes

**LeetCode Problem #3331 — Find Subtree Sizes After Changes**
Solve LeetCode Find Subtree Sizes After Changes using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Subtree Sizes After Changes |
| LeetCode | #3331 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a tree rooted at node 0 that consists of `n` nodes numbered from `0` to `n - 1`. The tree is represented by an array `parent` of size `n`, where `parent[i]` is the parent of node `i`. Since node 0 is the root, `parent[0] == -1`.

You are also given a string `s` of length `n`, where `s[i]` is the character assigned to node `i`.

We make the following changes on the tree **one** time **simultaneously** for all nodes `x` from `1` to `n - 1`:

Find the **closest** node `y` to node `x` such that `y` is an ancestor of `x`, and `s[x] == s[y]`. 
 If node `y` does not exist, do nothing. 
 Otherwise, **remove** the edge between `x` and its current parent and make node `y` the new parent of `x` by adding an edge between them.

Return an array `answer` of size `n` where `answer[i]` is the **size** of the subtree rooted at node `i` in the **final** tree.

## Constraints
- `n == parent.length == s.length`
- `1 <= n <= 10^5`
- `0 <= parent[i] <= n - 1` for all `i >= 1`.
- `parent[0] == -1`
- `parent` represents a valid tree.
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `parent = [-1,0,0,1,1,1], s = "abaabc"`
- **Output:** `[6,3,1,1,1,1]`
- **Explanation:** The parent of node 3 will change from node 1 to node 0.

### Example 2
- **Input:** `parent = [-1,0,4,0,1], s = "abbba"`
- **Output:** `[5,2,1,1,1]`
- **Explanation:** The following changes will happen at the same time: 

 
 The parent of node 4 will change from node 1 to node 0. 
 The parent of node 2 will change from node 4 to node 1.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Subtree Sizes After Changes**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `parent = [-1,0,0,1,1,1], s = "abaabc"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,3,1,1,1,1]`.
4. **Verification:** The parent of node 3 will change from node 1 to node 0.

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
var findSubtreeSizes = function(parent, s) {
    const n = parent.length;
    const adj = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        adj[parent[i]].push(i);
    }

    const newParent = parent.slice();
    const lastSeen = new Int32Array(26).fill(-1);

    // Pass 1: Iterative pre-order DFS with explicit exit markers to avoid call-stack limits
    const stack = [[0, false]];
    while (stack.length > 0) {
        const frame = stack[stack.length - 1];
        const u = frame[0];
        const ch = s.charCodeAt(u) - 97;

        if (!frame[1]) {
            frame[1] = true;
            frame[2] = lastSeen[ch]; // Save previous ancestor on frame
            if (lastSeen[ch] !== -1) {
                newParent[u] = lastSeen[ch];
            }
            lastSeen[ch] = u;

            const children = adj[u];
            for (let i = children.length - 1; i >= 0; i--) {
                stack.push([children[i], false]);
            }
        } else {
            lastSeen[ch] = frame[2]; // Restore on exit
            stack.pop();
        }
    }

    // Build final tree adjacency list and compute subtree sizes bottom-up
    const finalAdj = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        finalAdj[newParent[i]].push(i);
    }

    const order = [];
    const dfsStack = [0];
    while (dfsStack.length > 0) {
        const u = dfsStack.pop();
        order.push(u);
        for (const v of finalAdj[u]) {
            dfsStack.push(v);
        }
    }

    const answer = new Array(n).fill(1);
    for (let i = order.length - 1; i >= 1; i--) {
        const u = order[i];
        answer[newParent[u]] += answer[u];
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
- [2089. Find Target Indices After Sorting Array](../../2001-2500/2089-find-target-indices-after-sorting-array/)
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2593-find-score-of-an-array-after-marking-all-elements/)
- [3178. Find the Child Who Has the Ball After K Seconds](../../3001-3500/3178-find-the-child-who-has-the-ball-after-k-seconds/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-subtree-sizes-after-changes/)
