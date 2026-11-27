# LeetCode 3796: Find Maximum Value in a Constrained Sequence

**LeetCode Problem #3796 — Find Maximum Value in a Constrained Sequence**
Solve LeetCode Find Maximum Value in a Constrained Sequence using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Maximum Value in a Constrained Sequence |
| LeetCode | #3796 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n`, a 2D integer array `restrictions`, and an integer array `diff` of length `n - 1`. Your task is to construct a sequence of length `n`, denoted by `a[0], a[1], ..., a[n - 1]`, such that it satisfies the following conditions:

`a[0]` is 0. 
 All elements in the sequence are **non-negative**. 
 For every index `i` (`0 <= i <= n - 2`), `abs(a[i] - a[i + 1]) <= diff[i]`. 
 For each `restrictions[i] = [idx, maxVal]`, the value at position `idx` in the sequence must not exceed `maxVal` (i.e., `a[idx] <= maxVal`).

Your goal is to construct a valid sequence that **maximizes** the **largest** value within the sequence while satisfying all the above conditions.

Return an integer denoting the **largest** value present in such an optimal sequence.

## Constraints
- `2 <= n <= 10^5`
- `1 <= restrictions.length <= n - 1`
- `restrictions[i].length == 2`
- `restrictions[i] = [idx, maxVal]`
- `1 <= idx < n`
- `1 <= maxVal <= 10^6`
- `diff.length == n - 1`
- `1 <= diff[i] <= 10`
- The values of `restrictions[i][0]` are unique.

## Examples
### Example 1
- **Input:** `n = 10, restrictions = [[3,1],[8,1]], diff = [2,2,3,1,4,5,1,1,2]`
- **Output:** `6`
- **Explanation:** The sequence `a = [0, 2, 4, 1, 2, 6, 2, 1, 1, 3]` satisfies the given

### Example 2
- **Input:** `n = 8, restrictions = [[3,2]], diff = [3,5,2,4,2,3,1]`
- **Output:** `12`
- **Explanation:** The sequence `a = [0, 3, 3, 2, 6, 8, 11, 12]` satisfies the given

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Maximum Value in a Constrained Sequence**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10, restrictions = [[3,1],[8,1]], diff = [2,2,3,1,4,5,1,1,2]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The sequence `a = [0, 2, 4, 1, 2, 6, 2, 1, 1, 3]` satisfies the given

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
var findMaxVal = function(n, restrictions, diff) {
    const limit = new Array(n).fill(Infinity);

    limit[0] = 0;

    for (const [idx, maxVal] of restrictions) {
        limit[idx] = Math.min(limit[idx], maxVal);
    }

    for (let i = 1; i < n; i++) {
        limit[i] = Math.min(
            limit[i],
            limit[i - 1] + diff[i - 1]
        );
    }

    for (let i = n - 2; i >= 0; i--) {
        limit[i] = Math.min(
            limit[i],
            limit[i + 1] + diff[i]
        );
    }

    let ans = 0;

    for (let i = 0; i < n; i++) {
        ans = Math.max(ans, limit[i]);
    }

    return ans;
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
- [3287. Find the Maximum Sequence Value of Array](../../3001-3500/3287-find-the-maximum-sequence-value-of-array/)
- [3993. Maximum Value of an Alternating Sequence](../../3501-4000/3993-maximum-value-of-an-alternating-sequence/)
- [2242. Maximum Score of a Node Sequence](../../2001-2500/2242-maximum-score-of-a-node-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/)
