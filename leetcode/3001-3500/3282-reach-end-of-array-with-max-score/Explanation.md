# LeetCode 3282: Reach End of Array With Max Score

**LeetCode Problem #3282 — Reach End of Array With Max Score**
Solve LeetCode Reach End of Array With Max Score using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reach End of Array With Max Score |
| LeetCode | #3282 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

Your goal is to start at index `0` and reach index `n - 1`. You can only jump to indices **greater** than your current index.

The score for a jump from index `i` to index `j` is calculated as `(j - i) * nums[i]`.

Return the **maximum** possible total score by the time you reach the last index.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,3,1,5]`
- **Output:** `7`
- **Explanation:** First, jump to index 1 and then jump to the last index. The final score is `1 * 1 + 2 * 3 = 7`.

### Example 2
- **Input:** `nums = [4,3,1,3,2]`
- **Output:** `16`
- **Explanation:** Jump directly to the last index. The final score is `4 * 4 = 16`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reach End of Array With Max Score**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,1,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** First, jump to index 1 and then jump to the last index. The final score is `1 * 1 + 2 * 3 = 7`.

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
var findMaximumScore = function(nums) {
    let score = 0;
    let maxValue = nums[0];

    for (let i = 1; i < nums.length; i++) {
        score += maxValue;
        maxValue = Math.max(maxValue, nums[i]);
    }

    return score;
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
- [2587. Rearrange Array to Maximize Prefix Score](../../2501-3000/2587-rearrange-array-to-maximize-prefix-score/)
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2593-find-score-of-an-array-after-marking-all-elements/)
- [2640. Find the Score of All Prefixes of an Array](../../2501-3000/2640-find-the-score-of-all-prefixes-of-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reach-end-of-array-with-max-score/)
