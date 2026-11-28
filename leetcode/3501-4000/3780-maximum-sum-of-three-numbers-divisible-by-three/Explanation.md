# LeetCode 3780: Maximum Sum of Three Numbers Divisible by Three

**LeetCode Problem #3780 — Maximum Sum of Three Numbers Divisible by Three**
Solve LeetCode Maximum Sum of Three Numbers Divisible by Three using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum of Three Numbers Divisible by Three |
| LeetCode | #3780 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Your task is to choose **exactly three** integers from `nums` such that their sum is divisible by three.

Return the **maximum** possible sum of such a triplet. If no such triplet exists, return 0.

## Constraints
- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [4,2,3,1]`
- **Output:** `9`
- **Explanation:** The valid triplets whose sum is divisible by 3 are: 

 
 `(4, 2, 3)` with a sum of `4 + 2 + 3 = 9`. 
 `(2, 3, 1)` with a sum of `2 + 3 + 1 = 6`. 
 

 Thus, the answer is 9.

### Example 2
- **Input:** `nums = [2,1,5]`
- **Output:** `0`
- **Explanation:** No triplet forms a sum divisible by 3, so the answer is 0.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Sum of Three Numbers Divisible by Three**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,2,3,1]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** The valid triplets whose sum is divisible by 3 are: 

 
 `(4, 2, 3)` with a sum of `4 + 2 + 3 = 9`. 
 `(2, 3, 1)` with a sum of `2 + 3 + 1 = 6`. 
 

 Thus, the answer is 9.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maximumSum = function(nums) {
    const groups = [[], [], []];

    for (const num of nums) {
        groups[num % 3].push(num);
    }

    for (const group of groups) {
        group.sort((a, b) => b - a);
    }

    let ans = 0;

    if (groups[0].length >= 3) {
        ans = Math.max(
            ans,
            groups[0][0] + groups[0][1] + groups[0][2]
        );
    }

    if (groups[1].length >= 3) {
        ans = Math.max(
            ans,
            groups[1][0] + groups[1][1] + groups[1][2]
        );
    }

    if (groups[2].length >= 3) {
        ans = Math.max(
            ans,
            groups[2][0] + groups[2][1] + groups[2][2]
        );
    }

    if (
        groups[0].length >= 1 &&
        groups[1].length >= 1 &&
        groups[2].length >= 1
    ) {
        ans = Math.max(
            ans,
            groups[0][0] + groups[1][0] + groups[2][0]
        );
    }

    return ans;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [628. Maximum Product of Three Numbers](../../0501-1000/0628-maximum-product-of-three-numbers/)
- [3256. Maximum Value Sum by Placing Three Rooks I](../../3001-3500/3256-maximum-value-sum-by-placing-three-rooks-i/)
- [3257. Maximum Value Sum by Placing Three Rooks II](../../3001-3500/3257-maximum-value-sum-by-placing-three-rooks-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/)
