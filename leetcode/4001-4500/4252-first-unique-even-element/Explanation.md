# LeetCode 3866: First Unique Even Element

**LeetCode Problem #3866 — First Unique Even Element**
Solve LeetCode First Unique Even Element using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | First Unique Even Element |
| LeetCode | #3866 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Return an integer denoting the first **even** integer (earliest by array index) that appears **exactly** once in `nums`. If no such integer exists, return -1.

An integer `x` is considered **even** if it is divisible by 2.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [3,4,2,5,4,6]`
- **Output:** `2`
- **Explanation:** Both 2 and 6 are even and they appear exactly once. Since 2 occurs first in the array, the answer is 2.

### Example 2
- **Input:** `nums = [4,4]`
- **Output:** `-1`
- **Explanation:** No even integer appears exactly once, so return -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **First Unique Even Element**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,4,2,5,4,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Both 2 and 6 are even and they appear exactly once. Since 2 occurs first in the array, the answer is 2.

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
var firstUniqueEven = function(nums) {
    const freq = new Map();

    // Step 1: Count frequency of each number
    for (let num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // Step 2: Find the first unique even number
    for (let num of nums) {
        if (num % 2 === 0 && freq.get(num) === 1) {
            return num;
        }
    }

    return -1;
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
- [3843. First Element with Unique Frequency](../../4001-4500/4217-first-element-with-unique-frequency/)
- [387. First Unique Character in a String](../../0001-0500/0387-first-unique-character-in-a-string/)
- [3483. Unique 3-Digit Even Numbers](../../3501-4000/3799-unique-3-digit-even-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/first-unique-even-element/)
