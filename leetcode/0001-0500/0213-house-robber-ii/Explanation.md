# LeetCode 213: House Robber II

**LeetCode Problem #213 — House Robber II**
Solve LeetCode House Robber II using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | House Robber II |
| LeetCode | #213 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

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
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **House Robber II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,2]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

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
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [198. House Robber](../../0001-0500/0198-house-robber/)
- [337. House Robber III](../../0001-0500/0337-house-robber-iii/)
- [2560. House Robber IV](../../2501-3000/2560-house-robber-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/house-robber-ii/)
