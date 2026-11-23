# LeetCode 421: Maximum XOR of Two Numbers in an Array

**LeetCode Problem #421 — Maximum XOR of Two Numbers in an Array**
Solve LeetCode Maximum XOR of Two Numbers in an Array using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum XOR of Two Numbers in an Array |
| LeetCode | #421 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, return *the maximum result of *`nums[i] XOR nums[j]`, where `0 <= i <= j < n`.

## Constraints
- `1 <= nums.length <= 2 * 10^5`
- `0 <= nums[i] <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `nums = [3,10,5,25,2,8]`
- **Output:** `28`
- **Explanation:** The maximum result is 5 XOR 25 = 28.

### Example 2
- **Input:** `nums = [14,70,53,83,49,91,36,80,92,51,66,70]`
- **Output:** `127`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum XOR of Two Numbers in an Array**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,10,5,25,2,8]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `28`.
4. **Verification:** The maximum result is 5 XOR 25 = 28.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for b in range(30, -1, -1):
            prefixes = {v >> b for v in nums}
            cand = (ans << 1) | 1
            if any((p ^ cand) in prefixes for p in prefixes):
                ans = cand
            else:
                ans <<= 1
        return ans
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
- [1464. Maximum Product of Two Elements in an Array](../../1501-2000/1574-maximum-product-of-two-elements-in-an-array/)
- [1707. Maximum XOR With an Element From Array](../../1501-2000/1826-maximum-xor-with-an-element-from-array/)
- [3630. Partition Array for Maximum XOR and AND](../../3501-4000/3882-partition-array-for-maximum-xor-and-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
