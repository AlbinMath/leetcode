# LeetCode 3486: Longest Special Path II

**LeetCode Problem #3486 — Longest Special Path II**
Solve LeetCode Longest Special Path II using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Special Path II |
| LeetCode | #3486 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an undirected tree rooted at node `0`, with `n` nodes numbered from `0` to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, length_i]` indicates an edge between nodes `u_i` and `v_i` with length `length_i`. You are also given an integer array `nums`, where `nums[i]` represents the value at node `i`.

A **special path** is defined as a **downward** path from an ancestor node to a descendant node in which all node values are **distinct**, except for **at most** one value that may appear twice.

Return an array result of size 2, where `result[0]` is the length of the **longest** special path, and `result[1]` is the minimum number of nodes in all possible **longest** special paths.

## Constraints
- `2 <= n <= 5 * 10^ 4 `
- `edges.length == n - 1`
- `edges[i].length == 3`
- `0 <= u_i, v_i < n`
- `1 <= length_i <= 10^3`
- `nums.length == n`
- `0 <= nums[i] <= 5 * 10^4`
- The input is generated such that `edges` represents a valid tree.

## Examples
### Example 1
- **Input:** `edges = [[0,1,1],[1,2,3],[1,3,1],[2,4,6],[4,7,2],[3,5,2],[3,6,5],[6,8,3]], nums = [1,1,0,3,1,2,1,1,0]`
- **Output:** `[9,3]`
- **Explanation:** In the image below, nodes are colored by their corresponding values in `nums`. 

 

 The longest special paths are `1 -> 2 -> 4` and `1 -> 3 -> 6 -> 8`, both having a length of 9. The minimum number of nodes across all longest special paths is 3.

### Example 2
- **Input:** `edges = [[1,0,3],[0,2,4],[0,3,5]], nums = [1,1,0,2]`
- **Output:** `[5,2]`
- **Explanation:** The longest path is `0 -> 3` consisting of 2 nodes with a length of 5.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Special Path II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [[0,1,1],[1,2,3],[1,3,1],[2,4,6],[4,7,2],[3,5,2],[3,6,5],[6,8,3]], nums = [1,1,0,3,1,2,1,1,0]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[9,3]`.
4. **Verification:** In the image below, nodes are colored by their corresponding values in `nums`. 

 

 The longest special paths are `1 -> 2 -> 4` and `1 -> 3 -> 6 -> 8`, both having a length of 9. The minimum number of nodes across all longest special paths is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var longestSpecialPath = function(edges, nums) {
    const n = nums.length;
    const MAX = 50001;

    const graph = Array.from({ length: n }, () => []);

    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }

    function add(bit, pos, delta) {
        for (let i = pos + 1; i <= n; i += i & -i) {
            bit[i] += delta;
        }
    }

    function query(bit, pos) {
        let result = 0;

        for (let i = pos; i > 0; i -= i & -i) {
            result += bit[i];
        }

        return result;
    }

    function kth(bit, k) {
        let index = 0;
        let step = 1;

        while (step * 2 <= n) step *= 2;

        for (; step > 0; step >>= 1) {
            const next = index + step;

            if (next <= n && bit[next] < k) {
                index = next;
                k -= bit[next];
            }
        }

        return index;
    }

    const duplicateBIT = new Array(n + 1).fill(0);
    const tripleBIT = new Array(n + 1).fill(0);

    const occurrences = Array.from(
        { length: MAX },
        () => []
    );

    const dist = new Array(n).fill(0);

    let bestLength = 0;
    let minNodes = 1;

    function update(value, depth, entering) {
        const arr = occurrences[value];
        const len = arr.length;

        if (entering) {
            if (len >= 2) {
                add(duplicateBIT, arr[len - 2], -1);
            }

            if (len >= 3) {
                add(tripleBIT, arr[len - 3], -1);
            }

            arr.push(depth);

            if (len >= 1) {
                add(duplicateBIT, arr[len - 1], 1);
            }

            if (len >= 2) {
                add(tripleBIT, arr[len - 2], 1);
            }
        } else {
            // Remove current markers
            if (len >= 2) {
                add(duplicateBIT, arr[len - 2], -1);
            }

            if (len >= 3) {
                add(tripleBIT, arr[len - 3], -1);
            }

            arr.pop();

            // Restore previous markers using corrected indices
            if (len - 1 >= 2) {
                add(duplicateBIT, arr[len - 3], 1);
            }

            if (len - 1 >= 3) {
                add(tripleBIT, arr[len - 4], 1);
            }
        }
    }

    const stack = [{
        node: 0,
        parent: -1,
        depth: 0,
        distance: 0,
        exit: false
    }];

    while (stack.length > 0) {
        const cur = stack.pop();

        const {
            node,
            parent,
            depth,
            distance
        } = cur;

        const value = nums[node];

        if (cur.exit) {
            update(value, depth, false);
            continue;
        }

        update(value, depth, true);

        dist[depth] = distance;

        let left = 0;

        // No value may occur three or more times.
        const tripleCount = query(tripleBIT, n);

        if (tripleCount > 0) {
            left = kth(tripleBIT, tripleCount) + 1;
        }

        // At most one value may occur twice.
        const duplicateCount = query(duplicateBIT, n);

        if (duplicateCount >= 2) {
            const position = kth(
                duplicateBIT,
                duplicateCount - 1
            );

            left = Math.max(left, position + 1);
        }

        const pathLength = distance - dist[left];
        const nodeCount = depth - left + 1;

        if (pathLength > bestLength) {
            bestLength = pathLength;
            minNodes = nodeCount;
        } else if (pathLength === bestLength) {
            minNodes = Math.min(minNodes, nodeCount);
        }

        // Backtracking event
        stack.push({
            node,
            depth,
            exit: true
        });

        for (const [v, w] of graph[node]) {
            if (v !== parent) {
                stack.push({
                    node: v,
                    parent: node,
                    depth: depth + 1,
                    distance: distance + w,
                    exit: false
                });
            }
        }
    }

    return [bestLength, minNodes];
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3425. Longest Special Path](../../3001-3500/3425-longest-special-path/)
- [2662. Minimum Cost of a Path With Special Roads](../../2501-3000/2662-minimum-cost-of-a-path-with-special-roads/)
- [2981. Find Longest Special Substring That Occurs Thrice I](../../2501-3000/2981-find-longest-special-substring-that-occurs-thrice-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-special-path-ii/)
