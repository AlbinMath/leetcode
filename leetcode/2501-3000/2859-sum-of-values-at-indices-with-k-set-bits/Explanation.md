# LeetCode 2859: Sum of Values at Indices With K Set Bits

**LeetCode Problem #2859 — Sum of Values at Indices With K Set Bits**
Solve LeetCode Sum of Values at Indices With K Set Bits using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Values at Indices With K Set Bits |
| LeetCode | #2859 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` and an integer `k`.

Return *an integer that denotes the **sum** of elements in *`nums`* whose corresponding **indices** have **exactly** *`k`* set bits in their binary representation.*

The **set bits** in an integer are the `1`'s present when it is written in binary.

For example, the binary representation of `21` is `10101`, which has `3` set bits.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^5`
- `0 <= k <= 10`

## Examples
### Example 1
- **Input:** `nums = [5,10,1,5,2], k = 1`
- **Output:** `13`
- **Explanation:** The binary representation of the indices are: 
0 = 000_2
1 = 001_2
2 = 010_2
3 = 011_2
4 = 100 2 
 Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
Hence, the answer is nums[1] + nums[2] + nums[4] = 13.

### Example 2
- **Input:** `nums = [4,3,2,1], k = 2`
- **Output:** `1`
- **Explanation:** The binary representation of the indices are:
0 = 00_2
1 = 01_2
2 = 10_2
3 = 11 2
 Only index 3 has k = 2 set bits in its binary representation.
Hence, the answer is nums[3] = 1.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Values at Indices With K Set Bits**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,10,1,5,2], k = 1`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** The binary representation of the indices are: 
0 = 000_2
1 = 001_2
2 = 010_2
3 = 011_2
4 = 100 2 
 Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
Hence, the answer is nums[1] + nums[2] + nums[4] = 13.

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
    def sumIndicesWithKSetBits(self, nums, k):
        total = 0
        for i, x in enumerate(nums):
            if bin(i).count('1') == k:
                total += x
        return total
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
- [3068. Find the Maximum Sum of Node Values](../../3001-3500/3068-find-the-maximum-sum-of-node-values/)
- [3117. Minimum Sum of Values by Dividing Array](../../3001-3500/3117-minimum-sum-of-values-by-dividing-array/)
- [3547. Maximum Sum of Edge Values in a Graph](../../3501-4000/3547-maximum-sum-of-edge-values-in-a-graph/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/)
