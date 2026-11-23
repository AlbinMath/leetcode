# LeetCode 1782: Count Pairs Of Nodes

**LeetCode Problem #1782 — Count Pairs Of Nodes**
Solve LeetCode Count Pairs Of Nodes using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Pairs Of Nodes |
| LeetCode | #1782 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an undirected graph defined by an integer `n`, the number of nodes, and a 2D integer array `edges`, the edges in the graph, where `edges[i] = [u_i, v_i]` indicates that there is an **undirected** edge between `u_i` and `v_i`. You are also given an integer array `queries`.

Let `incident(a, b)` be defined as the **number of edges** that are connected to **either** node `a` or `b`.

The answer to the `j^th` query is the **number of pairs** of nodes `(a, b)` that satisfy **both** of the following conditions:

`a < b` 
 `incident(a, b) > queries[j]`

Return *an array *`answers`* such that *`answers.length == queries.length`* and *`answers[j]`* is the answer of the *`j^th`* query*.

Note that there can be **multiple edges** between the same two nodes.

## Constraints
- `2 <= n <= 2 * 10^4`
- `1 <= edges.length <= 10^5`
- `1 <= u_i, v_i <= n`
- `u_i != v_i`
- `1 <= queries.length <= 20`
- `0 <= queries[j] < edges.length`

## Examples
### Example 1
- **Input:** `n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]`
- **Output:** `[6,5]`
- **Explanation:** The calculations for incident(a, b) are shown in the table above.
The answers for each of the queries are as follows:
- answers[0] = 6. All the pairs have an incident(a, b) value greater than 2.
- answers[1] = 5. All the pairs except (3, 4) have an incident(a, b) value greater than 3.

### Example 2
- **Input:** `n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]`
- **Output:** `[10,10,9,8,6]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Pairs Of Nodes**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,5]`.
4. **Verification:** The calculations for incident(a, b) are shown in the table above.
The answers for each of the queries are as follows:
- answers[0] = 6. All the pairs have an incident(a, b) value greater than 2.
- answers[1] = 5. All the pairs except (3, 4) have an incident(a, b) value greater than 3.

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
var countPairs = function(n, edges, queries) {
    const degree = new Array(n + 1).fill(0);

    // Count edges between each pair of nodes
    const common = new Map();

    for (const [u, v] of edges) {
        degree[u]++;
        degree[v]++;

        const a = Math.min(u, v);
        const b = Math.max(u, v);

        const key = a * (n + 1) + b;

        common.set(key, (common.get(key) || 0) + 1);
    }

    // Sort node degrees
    const sorted = degree.slice(1).sort((a, b) => a - b);

    const answers = [];

    for (const query of queries) {
        let left = 0;
        let right = n - 1;
        let count = 0;

        // Count pairs using two pointers
        while (left < right) {
            if (sorted[left] + sorted[right] > query) {
                count += right - left;
                right--;
            } else {
                left++;
            }
        }

        // Correct pairs that were overcounted
        // because of multiple edges between two nodes
        for (const [key, shared] of common) {
            const a = Math.floor(key / (n + 1));
            const b = key % (n + 1);

            const sum = degree[a] + degree[b];

            if (sum > query && sum - shared <= query) {
                count--;
            }
        }

        answers.push(count);
    }

    return answers;
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
- [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](../../2001-2500/2403-count-unreachable-pairs-of-nodes-in-an-undirected-graph/)
- [24. Swap Nodes in Pairs](../../0001-0500/0024-swap-nodes-in-pairs/)
- [1530. Number of Good Leaf Nodes Pairs](../../1501-2000/1653-number-of-good-leaf-nodes-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-pairs-of-nodes/)
