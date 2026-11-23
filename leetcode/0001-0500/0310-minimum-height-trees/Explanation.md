# LeetCode 310: Minimum Height Trees

**LeetCode Problem #310 — Minimum Height Trees**
Solve LeetCode Minimum Height Trees using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Height Trees |
| LeetCode | #310 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of `n` nodes labelled from `0` to `n - 1`, and an array of `n - 1` `edges` where `edges[i] = [a_i, b_i]` indicates that there is an undirected edge between the two nodes `a_i` and `b_i` in the tree, you can choose any node of the tree as the root. When you select a node `x` as the root, the result tree has height `h`. Among all possible rooted trees, those with minimum height (i.e. `min(h)`) are called **minimum height trees** (MHTs).

Return *a list of all **MHTs'** root labels*. You can return the answer in **any order**.

The **height** of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

## Constraints
- `1 <= n <= 2 * 10^4`
- `edges.length == n - 1`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- All the pairs `(a_i, b_i)` are distinct.
- The given input is **guaranteed** to be a tree and there will be **no repeated** edges.

## Examples
### Example 1
- **Input:** `n = 4, edges = [[1,0],[1,2],[1,3]]`
- **Output:** `[1]`
- **Explanation:** As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

### Example 2
- **Input:** `n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]`
- **Output:** `[3,4]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Minimum Height Trees**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, edges = [[1,0],[1,2],[1,3]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1]`.
4. **Verification:** As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees = function (n, edges) {
    if (n === 1) return [0];

    const adj = Array.from({ length: n }, () => []);
    const deg = new Array(n).fill(0);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
        deg[a]++;
        deg[b]++;
    }

    let leaves = [];
    for (let i = 0; i < n; i++) if (deg[i] === 1) leaves.push(i);

    let remaining = n;
    while (remaining > 2) {
        remaining -= leaves.length;
        const next = [];
        for (const leaf of leaves) {
            for (const nb of adj[leaf]) {
                if (--deg[nb] === 1) next.push(nb);
            }
        }
        leaves = next;
    }
    return leaves;
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3203. Find Minimum Diameter After Merging Two Trees](../../3001-3500/3439-find-minimum-diameter-after-merging-two-trees/)
- [95. Unique Binary Search Trees II](../../0001-0500/0095-unique-binary-search-trees-ii/)
- [96. Unique Binary Search Trees](../../0001-0500/0096-unique-binary-search-trees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-height-trees/)
