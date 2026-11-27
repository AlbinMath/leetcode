# LeetCode 2242: Maximum Score of a Node Sequence

**LeetCode Problem #2242 — Maximum Score of a Node Sequence**
Solve LeetCode Maximum Score of a Node Sequence using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score of a Node Sequence |
| LeetCode | #2242 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an **undirected** graph with `n` nodes, numbered from `0` to `n - 1`.

You are given a **0-indexed** integer array `scores` of length `n` where `scores[i]` denotes the score of node `i`. You are also given a 2D integer array `edges` where `edges[i] = [a_i, b_i]` denotes that there exists an **undirected** edge connecting nodes `a_i` and `b_i`.

A node sequence is valid if it meets the following conditions:

There is an edge connecting every pair of **adjacent** nodes in the sequence. 
 No node appears more than once in the sequence.

The score of a node sequence is defined as the **sum** of the scores of the nodes in the sequence.

Return *the **maximum score** of a valid node sequence with a length of *`4`*. *If no such sequence exists, return* *`-1`.

## Constraints
- `n == scores.length`
- `4 <= n <= 5 * 10^4`
- `1 <= scores[i] <= 10^8`
- `0 <= edges.length <= 5 * 10^4`
- `edges[i].length == 2`
- `0 <= a_i, b_i <= n - 1`
- `a_i != b_i`
- There are no duplicate edges.

## Examples
### Example 1
- **Input:** `scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]`
- **Output:** `24`
- **Explanation:** The figure above shows the graph and the chosen node sequence [0,1,2,3].
The score of the node sequence is 5 + 2 + 9 + 8 = 24.
It can be shown that no other node sequence has a score of more than 24.
Note that the sequences [3,1,2,0] and [1,0,2,3] are also valid and have a score of 24.
The sequence [0,3,2,4] is not valid since no edge connects nodes 0 and 3.

### Example 2
- **Input:** `scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]]`
- **Output:** `-1`
- **Explanation:** The figure above shows the graph.
There are no valid node sequences of length 4, so we return -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Score of a Node Sequence**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `24`.
4. **Verification:** The figure above shows the graph and the chosen node sequence [0,1,2,3].
The score of the node sequence is 5 + 2 + 9 + 8 = 24.
It can be shown that no other node sequence has a score of more than 24.
Note that the sequences [3,1,2,0] and [1,0,2,3] are also valid and have a score of 24.
The sequence [0,3,2,4] is not valid since no edge connects nodes 0 and 3.

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
var maximumScore = function(scores, edges) {
    const n = scores.length;

    // Store the top 3 neighbors of every node
    const graph = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    // Sort neighbors by their scores in descending order
    for (let i = 0; i < n; i++) {
        graph[i].sort((a, b) => scores[b] - scores[a]);

        // Only the top 3 neighbors are needed
        graph[i] = graph[i].slice(0, 3);
    }

    let answer = -1;

    // Consider every edge as the middle edge
    for (const [b, c] of edges) {

        // Choose a neighbor of b
        for (const a of graph[b]) {

            // Choose a neighbor of c
            for (const d of graph[c]) {

                // All four nodes must be distinct
                if (
                    a === c ||
                    d === b ||
                    a === d
                ) {
                    continue;
                }

                const total =
                    scores[a] +
                    scores[b] +
                    scores[c] +
                    scores[d];

                answer = Math.max(answer, total);
            }
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
- [3287. Find the Maximum Sequence Value of Array](../../3001-3500/3287-find-the-maximum-sequence-value-of-array/)
- [3796. Find Maximum Value in a Constrained Sequence](../../3501-4000/3796-find-maximum-value-in-a-constrained-sequence/)
- [3993. Maximum Value of an Alternating Sequence](../../3501-4000/3993-maximum-value-of-an-alternating-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-of-a-node-sequence/)
