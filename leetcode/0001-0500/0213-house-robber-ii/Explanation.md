# LeetCode 213: House Robber II

**LeetCode Problem #213 — House Robber II**
Solve LeetCode House Robber II using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | House Robber II |
| LeetCode | #213 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night .

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [2,3,2]`
- **Output:** `3`
- **Explanation:** You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

### Example 2
- **Input:** `nums = [1,2,3,1]`
- **Output:** `4`
- **Explanation:** Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

### Example 3
- **Input:** `nums = [1,2,3]`
- **Output:** `3`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **House Robber II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

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
var rob = function(nums) {
    const n = nums.length;

    if (n === 1) return nums[0];

    function robLinear(start, end) {
        let prev2 = 0;
        let prev1 = 0;

        for (let i = start; i <= end; i++) {
            let current = Math.max(
                prev1,
                prev2 + nums[i]
            );

            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }

    return Math.max(
        robLinear(0, n - 2),
        robLinear(1, n - 1)
    );
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
- [198. House Robber](../../0001-0500/0198-house-robber/)
- [337. House Robber III](../../0001-0500/0337-house-robber-iii/)
- [2560. House Robber IV](../../2501-3000/2560-house-robber-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/house-robber-ii/)
