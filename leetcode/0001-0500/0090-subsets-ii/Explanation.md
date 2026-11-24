# LeetCode 90: Subsets II

**LeetCode Problem #90 — Subsets II**
Solve LeetCode Subsets II using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subsets II |
| LeetCode | #90 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` that may contain duplicates, return *all possible* *subsets* * (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

## Constraints
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Examples
### Example 1
- **Input:** `nums = [1,2,2]`
- **Output:** `[[],[1],[1,2],[1,2,2],[2],[2,2]]`

### Example 2
- **Input:** `nums = [0]`
- **Output:** `[[],[0]]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Subsets II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[],[1],[1,2],[1,2,2],[2],[2,2]]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var subsetsWithDup = function(nums) {
    nums.sort((a, b) => a - b);

    const result = [];
    const subset = [];

    function backtrack(start) {
        result.push([...subset]);

        for (let i = start; i < nums.length; i++) {
            // Skip duplicates at the same recursion level
            if (i > start && nums[i] === nums[i - 1]) {
                continue;
            }

            subset.push(nums[i]);
            backtrack(i + 1);
            subset.pop();
        }
    }

    backtrack(0);
    return result;
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [78. Subsets](../../0001-0500/0078-subsets/)
- [698. Partition to K Equal Sum Subsets](../../0501-1000/0698-partition-to-k-equal-sum-subsets/)
- [916. Word Subsets](../../0501-1000/0916-word-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subsets-ii/)
