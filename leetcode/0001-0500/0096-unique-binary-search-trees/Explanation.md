# LeetCode 96: Unique Binary Search Trees

**LeetCode Problem #96 — Unique Binary Search Trees**
Solve LeetCode Unique Binary Search Trees using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unique Binary Search Trees |
| LeetCode | #96 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return *the number of structurally unique **BST'**s (binary search trees) which has exactly *`n`* nodes of unique values from* `1` *to* `n`.

## Constraints
- `1 <= n <= 19`

## Examples
### Example 1
- **Input:** `n = 3`
- **Output:** `5`

### Example 2
- **Input:** `n = 1`
- **Output:** `1`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Unique Binary Search Trees**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.

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
var numTrees = function(n) {
    const dp = new Array(n + 1).fill(0);

    dp[0] = 1;
    dp[1] = 1;

    for (let i = 2; i <= n; i++) {
        for (let root = 1; root <= i; root++) {
            dp[i] += dp[root - 1] * dp[i - root];
        }
    }

    return dp[n];
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
- [95. Unique Binary Search Trees II](../../0001-0500/0095-unique-binary-search-trees-ii/)
- [1305. All Elements in Two Binary Search Trees](../../1001-1500/1305-all-elements-in-two-binary-search-trees/)
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/unique-binary-search-trees/)
