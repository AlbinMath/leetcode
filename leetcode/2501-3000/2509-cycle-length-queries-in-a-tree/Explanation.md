# LeetCode 2509: Cycle Length Queries in a Tree

**LeetCode Problem #2509 — Cycle Length Queries in a Tree**
Solve LeetCode Cycle Length Queries in a Tree using JavaScript and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cycle Length Queries in a Tree |
| LeetCode | #2509 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`. There is a **complete binary tree** with `2^n - 1` nodes. The root of that tree is the node with the value `1`, and every node with a value `val` in the range `[1, 2^n - 1 - 1]` has two children where:

The left node has the value `2 * val`, and 
 The right node has the value `2 * val + 1`.

You are also given a 2D integer array `queries` of length `m`, where `queries[i] = [a_i, b_i]`. For each query, solve the following problem:

Add an edge between the nodes with values `a_i` and `b_i`. 
 Find the length of the cycle in the graph. 
 Remove the added edge between nodes with values `a_i` and `b_i`.

**Note** that:

A **cycle** is a path that starts and ends at the same node, and each edge in the path is visited only once. 
 The length of a cycle is the number of edges visited in the cycle. 
 There could be multiple edges between two nodes in the tree after adding the edge of the query.

Return *an array *`answer`* of length *`m`* where* `answer[i]` *is the answer to the* `i^th` *query.*

## Constraints
- `2 <= n <= 30`
- `m == queries.length`
- `1 <= m <= 10^5`
- `queries[i].length == 2`
- `1 <= a_i, b_i <= 2^n - 1`
- `a_i != b_i`

## Examples
### Example 1
- **Input:** `n = 3, queries = [[5,3],[4,7],[2,3]]`
- **Output:** `[4,5,3]`
- **Explanation:** The diagrams above show the tree of 2^3 - 1 nodes. Nodes colored in red describe the nodes in the cycle after adding the edge.
- After adding the edge between nodes 3 and 5, the graph contains a cycle of nodes [5,2,1,3]. Thus answer to the first query is 4. We delete the added edge and process the next query.
- After adding the edge between nodes 4 and 7, the graph contains a cycle of nodes [4,2,1,3,7]. Thus answer to the second query is 5. We delete the added edge and process the next query.
- After adding the edge between nodes 2 and 3, the graph contains a cycle of nodes [2,1,3]. Thus answer to the third query is 3. We delete the added edge.

### Example 2
- **Input:** `n = 2, queries = [[1,2]]`
- **Output:** `[2]`
- **Explanation:** The diagram above shows the tree of 2^2 - 1 nodes. Nodes colored in red describe the nodes in the cycle after adding the edge.
- After adding the edge between nodes 1 and 2, the graph contains a cycle of nodes [2,1]. Thus answer for the first query is 2. We delete the added edge.

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Cycle Length Queries in a Tree**, we observe the problem requirements and utilize the **Fast & Slow Pointers** technique. We iterate through the inputs using **Floyd Cycle Detection**, leveraging a **Linked List / Pointer** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Linked List / Pointer**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, queries = [[5,3],[4,7],[2,3]]`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,5,3]`.
4. **Verification:** The diagrams above show the tree of 2^3 - 1 nodes. Nodes colored in red describe the nodes in the cycle after adding the edge.
- After adding the edge between nodes 3 and 5, the graph contains a cycle of nodes [5,2,1,3]. Thus answer to the first query is 4. We delete the added edge and process the next query.
- After adding the edge between nodes 4 and 7, the graph contains a cycle of nodes [4,2,1,3,7]. Thus answer to the second query is 5. We delete the added edge and process the next query.
- After adding the edge between nodes 2 and 3, the graph contains a cycle of nodes [2,1,3]. Thus answer to the third query is 3. We delete the added edge.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List / Pointer.

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var cycleLengthQueries = function(n, queries) {
    const answer = [];

    for (const [a, b] of queries) {
        let x = a;
        let y = b;
        let length = 1;

        while (x !== y) {
            if (x > y) {
                x = Math.floor(x / 2);
            } else {
                y = Math.floor(y / 2);
            }

            length++;
        }

        answer.push(length);
    }

    return answer;
};
```

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3887. Incremental Even-Weighted Cycle Queries](../../3501-4000/3887-incremental-even-weighted-cycle-queries/)
- [2458. Height of Binary Tree After Subtree Removal Queries](../../2001-2500/2458-height-of-binary-tree-after-subtree-removal-queries/)
- [2476. Closest Nodes Queries in a Binary Search Tree](../../2001-2500/2476-closest-nodes-queries-in-a-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cycle-length-queries-in-a-tree/)
