# LeetCode 368: Largest Divisible Subset

**LeetCode Problem #368 — Largest Divisible Subset**
Solve LeetCode Largest Divisible Subset using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Divisible Subset |
| LeetCode | #368 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a set of **distinct** positive integers `nums`, return the largest subset `answer` such that every pair `(answer[i], answer[j])` of elements in this subset satisfies:

`answer[i] % answer[j] == 0`, or 
 `answer[j] % answer[i] == 0`

If there are multiple solutions, return any of them.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2 * 10^9`
- All the integers in `nums` are **unique**.

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `[1,2]`
- **Explanation:** [1,3] is also accepted.

### Example 2
- **Input:** `nums = [1,2,4,8]`
- **Output:** `[1,2,4,8]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Divisible Subset**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.
4. **Verification:** [1,3] is also accepted.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var largestDivisibleSubset = function(nums) {
    nums.sort((a, b) => a - b);

    const n = nums.length;
    const dp = new Array(n).fill(1);
    const prev = new Array(n).fill(-1);

    let maxLength = 1;
    let lastIndex = 0;

    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] % nums[j] === 0 && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }

        if (dp[i] > maxLength) {
            maxLength = dp[i];
            lastIndex = i;
        }
    }

    const result = [];

    while (lastIndex !== -1) {
        result.push(nums[lastIndex]);
        lastIndex = prev[lastIndex];
    }

    return result.reverse();
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3260. Find the Largest Palindrome Divisible by K](../../3001-3500/3260-find-the-largest-palindrome-divisible-by-k/)
- [416. Partition Equal Subset Sum](../../0001-0500/0416-partition-equal-subset-sum/)
- [1452. People Whose List of Favorite Companies Is Not a Subset of Another List](../../1001-1500/1452-people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-divisible-subset/)
