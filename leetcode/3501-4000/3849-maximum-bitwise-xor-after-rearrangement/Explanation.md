# LeetCode 3849: Maximum Bitwise XOR After Rearrangement

**LeetCode Problem #3849 — Maximum Bitwise XOR After Rearrangement**
Solve LeetCode Maximum Bitwise XOR After Rearrangement using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Bitwise XOR After Rearrangement |
| LeetCode | #3849 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two binary strings `s` and `t`​​​​​​​, each of length `n`.

You may **rearrange** the characters of `t` in any order, but `s` **must remain unchanged**.

Return a **binary string** of length `n` representing the **maximum** integer value obtainable by taking the bitwise **XOR** of `s` and rearranged `t`.

## Constraints
- `1 <= n == s.length == t.length <= 2 * 10^5`
- `s[i]` and `t[i]` are either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "101", t = "011"`
- **Output:** `"110"`
- **Explanation:** One optimal rearrangement of `t` is `"011"`. 
 The bitwise XOR of `s` and rearranged `t` is `"101" XOR "011" = "110"`, which is the maximum possible.

### Example 2
- **Input:** `s = "0110", t = "1110"`
- **Output:** `"1101"`
- **Explanation:** One optimal rearrangement of `t` is `"1011"`. 
 The bitwise XOR of `s` and rearranged `t` is `"0110" XOR "1011" = "1101"`, which is the maximum possible.

### Example 3
- **Input:** `s = "0101", t = "1001"`
- **Output:** `"1111"`
- **Explanation:** One optimal rearrangement of `t` is `"1010"`. 
 The bitwise XOR of `s` and rearranged `t` is `"0101" XOR "1010" = "1111"`, which is the maximum possible.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Bitwise XOR After Rearrangement**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "101", t = "011"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"110"`.
4. **Verification:** One optimal rearrangement of `t` is `"011"`. 
 The bitwise XOR of `s` and rearranged `t` is `"101" XOR "011" = "110"`, which is the maximum possible.

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
    def maximumXor(self, s, t):
        cnt = [t.count('0'), t.count('1')]
        res = []
        for ch in s:
            want = 1 - int(ch)  # bit of t that makes the XOR bit 1
            if cnt[want] > 0:
                cnt[want] -= 1
                res.append('1')
            else:
                cnt[1 - want] -= 1
                res.append('0')
        return ''.join(res)
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
- [2317. Maximum XOR After Operations ](../../2001-2500/2317-maximum-xor-after-operations/)
- [3806. Maximum Bitwise AND After Increment Operations](../../3501-4000/3806-maximum-bitwise-and-after-increment-operations/)
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/)
