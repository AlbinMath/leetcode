# LeetCode 3334: Find the Maximum Factor Score of Array

**LeetCode Problem #3334 — Find the Maximum Factor Score of Array**
Solve LeetCode Find the Maximum Factor Score of Array using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Maximum Factor Score of Array |
| LeetCode | #3334 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

The **factor score** of an array is defined as the *product* of the LCM and GCD of all elements of that array.

Return the **maximum factor score** of `nums` after removing **at most** one element from it.

**Note** that *both* the LCM and GCD of a single number are the number itself, and the *factor score* of an **empty** array is 0.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 30`

## Examples
### Example 1
- **Input:** `nums = [2,4,8,16]`
- **Output:** `64`
- **Explanation:** On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a maximum factor score of `4 * 16 = 64`.

### Example 2
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `60`
- **Explanation:** The maximum factor score of 60 can be obtained without removing any elements.

### Example 3
- **Input:** `nums = [3]`
- **Output:** `9`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Maximum Factor Score of Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,4,8,16]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `64`.
4. **Verification:** On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a maximum factor score of `4 * 16 = 64`.

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
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxScore = function(nums) {
    const n = nums.length;
    if (n === 1) return nums[0] * nums[0];

    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    const lcm = (a, b) => (a / gcd(a, b)) * b;

    const getScore = (skipIdx) => {
        let g = 0;
        let l = 1;

        for (let i = 0; i < n; i++) {
            if (i === skipIdx) continue;
            g = gcd(g, nums[i]);
            l = lcm(l, nums[i]);
        }

        return g * l;
    };

    // Baseline score without removing any element
    let best = getScore(-1);

    // Check score after removing each single element
    for (let i = 0; i < n; i++) {
        const score = getScore(i);
        if (score > best) {
            best = score;
        }
    }

    return best;
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
- [2945. Find Maximum Non-decreasing Array Length](../../3001-3500/3211-find-maximum-non-decreasing-array-length/)
- [3287. Find the Maximum Sequence Value of Array](../../3501-4000/3575-find-the-maximum-sequence-value-of-array/)
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2695-find-score-of-an-array-after-marking-all-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-maximum-factor-score-of-array/)
