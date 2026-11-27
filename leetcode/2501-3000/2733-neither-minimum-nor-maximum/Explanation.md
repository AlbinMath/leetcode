# LeetCode 2733: Neither Minimum nor Maximum

**LeetCode Problem #2733 — Neither Minimum nor Maximum**
Solve LeetCode Neither Minimum nor Maximum using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Neither Minimum nor Maximum |
| LeetCode | #2733 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` containing **distinct** **positive** integers, find and return **any** number from the array that is neither the **minimum** nor the **maximum** value in the array, or **`-1`** if there is no such number.

Return *the selected integer.*

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- All values in `nums` are distinct

## Examples
### Example 1
- **Input:** `nums = [3,2,1,4]`
- **Output:** `2`
- **Explanation:** In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.

### Example 2
- **Input:** `nums = [1,2]`
- **Output:** `-1`
- **Explanation:** Since there is no number in nums that is neither the maximum nor the minimum, we cannot select a number that satisfies the given condition. Therefore, there is no answer.

### Example 3
- **Input:** `nums = [2,1,3]`
- **Output:** `2`
- **Explanation:** Since 2 is neither the maximum nor the minimum value in nums, it is the only valid answer.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Neither Minimum nor Maximum**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,2,1,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.

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
var findNonMinOrMax = function(nums) {
    if (nums.length < 3) {
        return -1;
    }

    nums.sort((a, b) => a - b);

    return nums[1];
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
- [1491. Average Salary Excluding the Minimum and Maximum Salary](../../1001-1500/1491-average-salary-excluding-the-minimum-and-maximum-salary/)
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [2091. Removing Minimum and Maximum From Array](../../2001-2500/2091-removing-minimum-and-maximum-from-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/neither-minimum-nor-maximum/)
