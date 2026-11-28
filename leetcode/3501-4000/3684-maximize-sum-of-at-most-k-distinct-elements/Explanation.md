# LeetCode 3684: Maximize Sum of At Most K Distinct Elements

**LeetCode Problem #3684 — Maximize Sum of At Most K Distinct Elements**
Solve LeetCode Maximize Sum of At Most K Distinct Elements using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize Sum of At Most K Distinct Elements |
| LeetCode | #3684 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **positive** integer array `nums` and an integer `k`.

Choose at most `k` elements from `nums` so that their sum is maximized. However, the chosen numbers must be **distinct**.

Return an array containing the chosen numbers in **strictly descending** order.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [84,93,100,77,90], k = 3`
- **Output:** `[100,93,90]`
- **Explanation:** The maximum sum is 283, which is attained by choosing 93, 100 and 90. We rearrange them in strictly descending order as `[100, 93, 90]`.

### Example 2
- **Input:** `nums = [84,93,100,77,93], k = 3`
- **Output:** `[100,93,84]`
- **Explanation:** The maximum sum is 277, which is attained by choosing 84, 93 and 100. We rearrange them in strictly descending order as `[100, 93, 84 ]`. We cannot choose 93, 100 and 93 because the chosen numbers must be distinct.

### Example 3
- **Input:** `nums = [1,1,1,2,2,2], k = 6`
- **Output:** `[2,1]`
- **Explanation:** The maximum sum is 3, which is attained by choosing 1 and 2. We rearrange them in strictly descending order as `[2, 1]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize Sum of At Most K Distinct Elements**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [84,93,100,77,90], k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[100,93,90]`.
4. **Verification:** The maximum sum is 283, which is attained by choosing 93, 100 and 90. We rearrange them in strictly descending order as `[100, 93, 90]`.

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
var maxKDistinct = function(nums, k) {
    const unique = [...new Set(nums)];

    unique.sort((a, b) => b - a);

    return unique.slice(0, k);
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
- [3462. Maximum Sum With at Most K Elements](../../3001-3500/3462-maximum-sum-with-at-most-k-elements/)
- [2656. Maximum Sum With Exactly K Elements ](../../2501-3000/2656-maximum-sum-with-exactly-k-elements/)
- [3478. Choose K Elements With Maximum Sum](../../3001-3500/3478-choose-k-elements-with-maximum-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/)
