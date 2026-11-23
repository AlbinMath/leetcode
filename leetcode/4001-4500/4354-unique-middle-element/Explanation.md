# LeetCode 3978: Unique Middle Element

**LeetCode Problem #3978 — Unique Middle Element**
Solve LeetCode Unique Middle Element using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unique Middle Element |
| LeetCode | #3978 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of odd length `n`.

Return `true` if the middle element of `nums` appears **exactly** once in the array. Otherwise return `false`.

## Constraints
- `1 <= n == nums.length <= 100`
- `n` is odd.
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `true`
- **Explanation:** The middle element of `nums` is 2, which appears exactly once. 

 Thus, the answer is `true`.

### Example 2
- **Input:** `nums = [1,2,2]`
- **Output:** `false`
- **Explanation:** The middle element of `nums` is 2, which appears twice. 

 Thus, the answer is `false`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Unique Middle Element**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The middle element of `nums` is 2, which appears exactly once. 

 Thus, the answer is `true`.

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
var isMiddleElementUnique = function(nums) {
    const mid = Math.floor(nums.length / 2);
    const middle = nums[mid];

    let count = 0;

    for (const num of nums) {
        if (num === middle) {
            count++;
        }
    }

    return count === 1;
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
- [3395. Subsequences with a Unique Middle Mode I](../../3501-4000/3700-subsequences-with-a-unique-middle-mode-i/)
- [3843. First Element with Unique Frequency](../../4001-4500/4217-first-element-with-unique-frequency/)
- [3866. First Unique Even Element](../../4001-4500/4252-first-unique-even-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/unique-middle-element/)
