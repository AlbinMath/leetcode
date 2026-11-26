# LeetCode 3950: Exactly One Consecutive Set Bits Pair

**LeetCode Problem #3950 — Exactly One Consecutive Set Bits Pair**
Solve LeetCode Exactly One Consecutive Set Bits Pair using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Exactly One Consecutive Set Bits Pair |
| LeetCode | #3950 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`.

Return `true` if its binary representation contains **exactly one adjacent pair** of set bits , and `false` otherwise.

## Constraints
- `0 <= n <= 10^5`

## Examples
### Example 1
- **Input:** `n = 6`
- **Output:** `true`
- **Explanation:** Binary representation of 6 is `110`. 
 There is exactly one adjacent pair of set bits (`"11"`). Thus, the answer is `true`​​​​​​​.

### Example 2
- **Input:** `n = 5`
- **Output:** `false`
- **Explanation:** Binary representation of 5 is `101`. 
 There is no adjacent pair of set bits. Thus, the answer is `false`​​​​​​​.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Exactly One Consecutive Set Bits Pair**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Binary representation of 6 is `110`. 
 There is exactly one adjacent pair of set bits (`"11"`). Thus, the answer is `true`​​​​​​​.

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
class Solution(object):
    def consecutiveSetBits(self, n):
        return bin(n & (n >> 1)).count('1') == 1
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
- [3480. Maximize Subarrays After Removing One Conflicting Pair](../../3001-3500/3480-maximize-subarrays-after-removing-one-conflicting-pair/)
- [3821. Find Nth Smallest Integer With K One Bits](../../3501-4000/3821-find-nth-smallest-integer-with-k-one-bits/)
- [3963. Create Grid With Exactly One Path](../../3501-4000/3963-create-grid-with-exactly-one-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/)
