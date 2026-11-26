# LeetCode 1719: Number Of Ways To Reconstruct A Tree

**LeetCode Problem #1719 — Number Of Ways To Reconstruct A Tree**
Solve LeetCode Number Of Ways To Reconstruct A Tree using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number Of Ways To Reconstruct A Tree |
| LeetCode | #1719 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `pairs`, where `pairs[i] = [x_i, y_i]`, and:

There are no duplicates. 
 `x_i < y_i`

Let `ways` be the number of rooted trees that satisfy the following conditions:

The tree consists of nodes whose values appeared in `pairs`. 
 A pair `[x_i, y_i]` exists in `pairs` **if and only if** `x_i` is an ancestor of `y_i` or `y_i` is an ancestor of `x_i`. 
 **Note:** the tree does not have to be a binary tree.

Two ways are considered to be different if there is at least one node that has different parents in both ways.

Return:

`0` if `ways == 0` 
 `1` if `ways == 1` 
 `2` if `ways > 1`

A **rooted tree** is a tree that has a single root node, and all edges are oriented to be outgoing from the root.

An **ancestor** of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.

## Constraints
- `1 <= pairs.length <= 10^5`
- `1 <= x_i < y_i <= 500`
- The elements in `pairs` are unique.

## Examples
### Example 1
- **Input:** `pairs = [[1,2],[2,3]]`
- **Output:** `1`
- **Explanation:** There is exactly one valid rooted tree, which is shown in the above figure.

### Example 2
- **Input:** `pairs = [[1,2],[2,3],[1,3]]`
- **Output:** `2`
- **Explanation:** There are multiple valid rooted trees. Three of them are shown in the above figures.

### Example 3
- **Input:** `pairs = [[1,2],[2,3],[2,4],[1,5]]`
- **Output:** `0`
- **Explanation:** There are no valid rooted trees.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number Of Ways To Reconstruct A Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `pairs = [[1,2],[2,3]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There is exactly one valid rooted tree, which is shown in the above figure.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var checkWays = function(pairs) {
    // Build the graph
    const graph = new Map();

    for (const [x, y] of pairs) {
        if (!graph.has(x)) graph.set(x, new Set());
        if (!graph.has(y)) graph.set(y, new Set());

        graph.get(x).add(y);
        graph.get(y).add(x);
    }

    const nodes = [...graph.keys()];
    const n = nodes.length;

    // Find a possible root:
    // The root must be connected to all other nodes.
    let root = -1;

    for (const node of nodes) {
        if (graph.get(node).size === n - 1) {
            root = node;
            break;
        }
    }

    // No possible root
    if (root === -1) return 0;

    let result = 1;

    // Process every node except the root
    for (const node of nodes) {
        if (node === root) continue;

        const neighbors = graph.get(node);
        const degree = neighbors.size;

        let parent = -1;
        let parentDegree = Infinity;

        // Find the neighbor with the smallest degree
        // that is greater than or equal to this node's degree.
        for (const neighbor of neighbors) {
            const neighborDegree = graph.get(neighbor).size;

            if (
                neighborDegree >= degree &&
                neighborDegree < parentDegree
            ) {
                parent = neighbor;
                parentDegree = neighborDegree;
            }
        }

        // Every non-root node must have a parent
        if (parent === -1) return 0;

        // All neighbors of this node must also be
        // neighbors of its parent.
        for (const neighbor of neighbors) {
            if (
                neighbor !== parent &&
                !graph.get(parent).has(neighbor)
            ) {
                return 0;
            }
        }

        // Equal degrees mean multiple valid parent choices
        if (parentDegree === degree) {
            result = 2;
        }
    }

    return result;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1519. Number of Nodes in the Sub-Tree With the Same Label](../../1501-2000/1519-number-of-nodes-in-the-sub-tree-with-the-same-label/)
- [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../../2001-2500/2471-minimum-number-of-operations-to-sort-a-binary-tree-by-level/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1001-1500/1434-number-of-ways-to-wear-different-hats-to-each-other/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/)
