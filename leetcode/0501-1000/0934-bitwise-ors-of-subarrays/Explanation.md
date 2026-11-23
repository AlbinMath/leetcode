# LeetCode 898: Bitwise ORs of Subarrays

**LeetCode Problem #898 — Bitwise ORs of Subarrays**
Solve LeetCode Bitwise ORs of Subarrays using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Bitwise ORs of Subarrays |
| LeetCode | #898 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `arr`, return *the number of distinct bitwise ORs of all the non-empty subarrays of* `arr`.

The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## Constraints
- `1 <= arr.length <= 5 * 10^4`
- `0 <= arr[i] <= 10^9`

## Examples
### Example 1
- **Input:** `arr = [0]`
- **Output:** `1`
- **Explanation:** There is only one possible result: 0.

### Example 2
- **Input:** `arr = [1,1,2]`
- **Output:** `3`
- **Explanation:** The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.

### Example 3
- **Input:** `arr = [1,2,4]`
- **Output:** `6`
- **Explanation:** The possible results are 1, 2, 3, 4, 6, and 7.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Bitwise ORs of Subarrays**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [0]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There is only one possible result: 0.

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
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        all_vals = set()
        cur = set()
        for x in arr:
            cur = {v | x for v in cur}
            cur.add(x)
            all_vals |= cur
        return len(all_vals)
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
- [2411. Smallest Subarrays With Maximum Bitwise OR](../../2001-2500/2498-smallest-subarrays-with-maximum-bitwise-or/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [930. Binary Subarrays With Sum](../../0501-1000/0966-binary-subarrays-with-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/bitwise-ors-of-subarrays/)
