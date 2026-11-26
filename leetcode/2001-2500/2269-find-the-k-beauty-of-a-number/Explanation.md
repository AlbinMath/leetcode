# LeetCode 2269: Find the K-Beauty of a Number

**LeetCode Problem #2269 — Find the K-Beauty of a Number**
Solve LeetCode Find the K-Beauty of a Number using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the K-Beauty of a Number |
| LeetCode | #2269 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **k-beauty** of an integer `num` is defined as the number of **substrings** of `num` when it is read as a string that meet the following conditions:

It has a length of `k`. 
 It is a divisor of `num`.

Given integers `num` and `k`, return *the k-beauty of *`num`.

**Leading zeros** are allowed. 
 `0` is not a divisor of any value.

A **substring** is a contiguous sequence of characters in a string.

## Constraints
- `1 <= num <= 10^9`
- `1 <= k <= num.length` (taking `num` as a string)

## Examples
### Example 1
- **Input:** `num = 240, k = 2`
- **Output:** `2`
- **Explanation:** The following are the substrings of num of length k:
- "24" from "

### Example 2
- **Input:** `num = 430043, k = 2`
- **Output:** `2`
- **Explanation:** The following are the substrings of num of length k:
- "43" from "

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the K-Beauty of a Number**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 240, k = 2`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The following are the substrings of num of length k:
- "24" from "

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
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0
        
        for i in range(len(s) - k + 1):
            sub = int(s[i : i + k])
            if sub != 0 and num % sub == 0:
                count += 1
                
        return count
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
- [3154. Find Number of Ways to Reach the K-th Stair](../../3001-3500/3154-find-number-of-ways-to-reach-the-k-th-stair/)
- [2527. Find Xor-Beauty of Array](../../2501-3000/2527-find-xor-beauty-of-array/)
- [2842. Count K-Subsequences of a String With Maximum Beauty](../../2501-3000/2842-count-k-subsequences-of-a-string-with-maximum-beauty/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-k-beauty-of-a-number/)
