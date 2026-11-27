# LeetCode 2374: Node With Highest Edge Score

**LeetCode Problem #2374 — Node With Highest Edge Score**
Solve LeetCode Node With Highest Edge Score using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Node With Highest Edge Score |
| LeetCode | #2374 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a directed graph with `n` nodes labeled from `0` to `n - 1`, where each node has **exactly one** outgoing edge.

The graph is represented by a given **0-indexed** integer array `edges` of length `n`, where `edges[i]` indicates that there is a **directed** edge from node `i` to node `edges[i]`.

The **edge score** of a node `i` is defined as the sum of the **labels** of all the nodes that have an edge pointing to `i`.

Return *the node with the highest **edge score***. If multiple nodes have the same **edge score**, return the node with the **smallest** index.

## Constraints
- `n == edges.length`
- `2 <= n <= 10^5`
- `0 <= edges[i] < n`
- `edges[i] != i`

## Examples
### Example 1
- **Input:** `edges = [1,0,0,0,0,7,7,5]`
- **Output:** `7`
- **Explanation:** - The nodes 1, 2, 3 and 4 have an edge pointing to node 0. The edge score of node 0 is 1 + 2 + 3 + 4 = 10.
- The node 0 has an edge pointing to node 1. The edge score of node 1 is 0.
- The node 7 has an edge pointing to node 5. The edge score of node 5 is 7.
- The nodes 5 and 6 have an edge pointing to node 7. The edge score of node 7 is 5 + 6 = 11.
Node 7 has the highest edge score so return 7.

### Example 2
- **Input:** `edges = [2,0,0,2]`
- **Output:** `0`
- **Explanation:** - The nodes 1 and 2 have an edge pointing to node 0. The edge score of node 0 is 1 + 2 = 3.
- The nodes 0 and 3 have an edge pointing to node 2. The edge score of node 2 is 0 + 3 = 3.
Nodes 0 and 2 both have an edge score of 3. Since node 0 has a smaller index, we return 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Node With Highest Edge Score**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `edges = [1,0,0,0,0,7,7,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** - The nodes 1, 2, 3 and 4 have an edge pointing to node 0. The edge score of node 0 is 1 + 2 + 3 + 4 = 10.
- The node 0 has an edge pointing to node 1. The edge score of node 1 is 0.
- The node 7 has an edge pointing to node 5. The edge score of node 5 is 7.
- The nodes 5 and 6 have an edge pointing to node 7. The edge score of node 7 is 5 + 6 = 11.
Node 7 has the highest edge score so return 7.

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
var edgeScore = function(edges) {
    const n = edges.length;

    // Store the edge score of each node
    const score = new Array(n).fill(0);

    // Calculate edge scores
    for (let i = 0; i < n; i++) {
        score[edges[i]] += i;
    }

    let maxScore = -1;
    let answer = 0;

    // Find the node with the highest score
    for (let i = 0; i < n; i++) {
        if (score[i] > maxScore) {
            maxScore = score[i];
            answer = i;
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
- [798. Smallest Rotation with Highest Score](../../0501-1000/0798-smallest-rotation-with-highest-score/)
- [2049. Count Nodes With the Highest Score](../../2001-2500/2049-count-nodes-with-the-highest-score/)
- [2858. Minimum Edge Reversals So Every Node Is Reachable](../../2501-3000/2858-minimum-edge-reversals-so-every-node-is-reachable/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/node-with-highest-edge-score/)
