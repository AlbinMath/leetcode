# LeetCode 2197: Replace Non-Coprime Numbers in Array

**LeetCode Problem #2197 — Replace Non-Coprime Numbers in Array**
Solve LeetCode Replace Non-Coprime Numbers in Array using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Replace Non-Coprime Numbers in Array |
| LeetCode | #2197 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `nums`. Perform the following steps:

Find **any** two **adjacent** numbers in `nums` that are **non-coprime**. 
 If no such numbers are found, **stop** the process. 
 Otherwise, delete the two numbers and **replace** them with their **LCM (Least Common Multiple)**. 
 **Repeat** this process as long as you keep finding two adjacent non-coprime numbers.

Return *the **final** modified array.* It can be shown that replacing adjacent non-coprime numbers in **any** arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are **less than or equal** to `10^8`.

Two values `x` and `y` are **non-coprime** if `GCD(x, y) > 1` where `GCD(x, y)` is the **Greatest Common Divisor** of `x` and `y`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- The test cases are generated such that the values in the final array are **less than or equal** to `10^8`.

## Examples
### Example 1
- **Input:** `nums = [6,4,3,2,7,6,2]`
- **Output:** `[12,7,6]`
- **Explanation:** - (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [

### Example 2
- **Input:** `nums = [2,2,1,1,3,3,3]`
- **Output:** `[2,1,1,3]`
- **Explanation:** - (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Replace Non-Coprime Numbers in Array**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [6,4,3,2,7,6,2]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[12,7,6]`.
4. **Verification:** - (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [

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
from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []
        for x in nums:
            while s and gcd(s[-1], x) > 1:
                g = gcd(s[-1], x)
                x = s.pop() // g * x
            s.append(x)
        return s
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
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [448. Find All Numbers Disappeared in an Array](../../0001-0500/0448-find-all-numbers-disappeared-in-an-array/)
- [1558. Minimum Numbers of Function Calls to Make Target Array](../../1501-2000/1558-minimum-numbers-of-function-calls-to-make-target-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/)
