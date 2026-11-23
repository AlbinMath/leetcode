# LeetCode 137: Single Number II

**LeetCode Problem #137 — Single Number II**
Solve LeetCode Single Number II using JavaScript, Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Single Number II |
| LeetCode | #137 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` where every element appears **three times** except for one, which appears **exactly once**. *Find the single element and return it*.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each element in `nums` appears exactly **three times** except for one element which appears **once**.

## Examples
### Example 1
- **Input:** `nums = [2,2,3,2]`
- **Output:** `3`

### Example 2
- **Input:** `nums = [0,1,0,1,0,1,99]`
- **Output:** `99`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Single Number II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,2,3,2]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var singleNumber = function(nums) {
    let result = 0;

    for (let i = 0; i < 32; i++) {
        let count = 0;

        for (const num of nums) {
            // Check bit i
            count += (num >>> i) & 1;
        }

        // Restore the bit if it appears a non-multiple of 3 times
        if (count % 3 !== 0) {
            result |= (1 << i);
        }
    }

    return result | 0;
};
```

### Python
```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = twos = 0
        for x in nums:
            ones = (ones ^ x) & ~twos
            twos = (twos ^ x) & ~ones
        return ones
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [136. Single Number](../../0001-0500/0136-single-number/)
- [260. Single Number III](../../0001-0500/0260-single-number-iii/)
- [619. Biggest Single Number](../../0501-1000/0619-biggest-single-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/single-number-ii/)
