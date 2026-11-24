# LeetCode 3674: Minimum Operations to Equalize Array

**LeetCode Problem #3674 — Minimum Operations to Equalize Array**
Solve LeetCode Minimum Operations to Equalize Array using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Equalize Array |
| LeetCode | #3674 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

In one operation, choose any subarray `nums[l...r]` (`0 <= l <= r < n`) and **replace** each element in that subarray with the **bitwise AND** of all elements.

Return the **minimum** number of operations required to make all elements of `nums` equal.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## Constraints
- `1 <= n == nums.length <= 100`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,2]`
- **Output:** `1`
- **Explanation:** Choose `nums[0...1]`: `(1 AND 2) = 0`, so the array becomes `[0, 0]` and all elements are equal in 1 operation.

### Example 2
- **Input:** `nums = [5,5,5]`
- **Output:** `0`
- **Explanation:** `nums` is `[5, 5, 5]` which already has all elements equal, so 0 operations are required.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Equalize Array**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Choose `nums[0...1]`: `(1 AND 2) = 0`, so the array becomes `[0, 0]` and all elements are equal in 1 operation.

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
    def minOperations(self, nums: List[int]) -> int:
        return 0 if len(set(nums)) == 1 else 1
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
- [3139. Minimum Cost to Equalize Array](../../3001-3500/3139-minimum-cost-to-equalize-array/)
- [3666. Minimum Operations to Equalize Binary String](../../3501-4000/3666-minimum-operations-to-equalize-binary-string/)
- [3762. Minimum Operations to Equalize Subarrays](../../3501-4000/3762-minimum-operations-to-equalize-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-equalize-array/)
