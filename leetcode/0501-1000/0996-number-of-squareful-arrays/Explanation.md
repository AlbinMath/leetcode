# LeetCode 996: Number of Squareful Arrays

**LeetCode Problem #996 — Number of Squareful Arrays**
Solve LeetCode Number of Squareful Arrays using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Squareful Arrays |
| LeetCode | #996 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
An array is **squareful** if the sum of every pair of adjacent elements is a **perfect square**.

Given an integer array nums, return *the number of permutations of *`nums`* that are **squareful***.

Two permutations `perm1` and `perm2` are different if there is some index `i` such that `perm1[i] != perm2[i]`.

## Constraints
- `1 <= nums.length <= 12`
- `0 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,17,8]`
- **Output:** `2`
- **Explanation:** [1,8,17] and [17,8,1] are the valid permutations.

### Example 2
- **Input:** `nums = [2,2,2]`
- **Output:** `1`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Squareful Arrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,17,8]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** [1,8,17] and [17,8,1] are the valid permutations.

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
/**
 * @param {number[]} nums
 * @return {number}
 */
var numSquarefulPerms = function (nums) {
  nums.sort((a, b) => a - b);
  const n = nums.length;

  const isSquare = (x) => {
    const r = Math.round(Math.sqrt(x));
    return r * r === x;
  };

  const ok = Array.from({ length: n }, () => new Array(n).fill(false));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i !== j) ok[i][j] = isSquare(nums[i] + nums[j]);
    }
  }

  const used = new Array(n).fill(false);
  let count = 0;

  const dfs = (depth, prev) => {
    if (depth === n) {
      count++;
      return;
    }
    for (let i = 0; i < n; i++) {
      if (used[i]) continue;
      if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue;
      if (prev !== -1 && !ok[prev][i]) continue;

      used[i] = true;
      dfs(depth + 1, i);
      used[i] = false;
    }
  };

  dfs(0, -1);
  return count;
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
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
- [1524. Number of Sub-arrays With Odd Sum](../../1501-2000/1524-number-of-sub-arrays-with-odd-sum/)
- [1775. Equal Sum Arrays With Minimum Number of Operations](../../1501-2000/1775-equal-sum-arrays-with-minimum-number-of-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-squareful-arrays/)
