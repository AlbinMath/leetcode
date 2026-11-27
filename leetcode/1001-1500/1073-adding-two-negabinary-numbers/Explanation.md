# LeetCode 1073: Adding Two Negabinary Numbers

**LeetCode Problem #1073 — Adding Two Negabinary Numbers**
Solve LeetCode Adding Two Negabinary Numbers using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Adding Two Negabinary Numbers |
| LeetCode | #1073 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two numbers `arr1` and `arr2` in base **-2**, return the result of adding them together.

Each number is given in *array format*: as an array of 0s and 1s, from most significant bit to least significant bit. For example, `arr = [1,1,0,1]` represents the number `(-2)^3 + (-2)^2 + (-2)^0 = -3`. A number `arr` in *array, format* is also guaranteed to have no leading zeros: either `arr == [0]` or `arr[0] == 1`.

Return the result of adding `arr1` and `arr2` in the same format: as an array of 0s and 1s with no leading zeros.

## Constraints
- `1 <= arr1.length, arr2.length <= 1000`
- `arr1[i]` and `arr2[i]` are `0` or `1`
- `arr1` and `arr2` have no leading zeros

## Examples
### Example 1
- **Input:** `arr1 = [1,1,1,1,1], arr2 = [1,0,1]`
- **Output:** `[1,0,0,0,0]`
- **Explanation:** arr1 represents 11, arr2 represents 5, the output represents 16.

### Example 2
- **Input:** `arr1 = [0], arr2 = [0]`
- **Output:** `[0]`

### Example 3
- **Input:** `arr1 = [0], arr2 = [1]`
- **Output:** `[1]`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Adding Two Negabinary Numbers**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr1 = [1,1,1,1,1], arr2 = [1,0,1]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,0,0,0,0]`.
4. **Verification:** arr1 represents 11, arr2 represents 5, the output represents 16.

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
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0 or carry != 0:
            total = carry
            if i >= 0:
                total += arr1[i]
                i -= 1
            if j >= 0:
                total += arr2[j]
                j -= 1
                
            res.append(total & 1)
            carry = -(total >> 1)
            
        while len(res) > 1 and res[-1] == 0:
            res.pop()
            
        return res[::-1]
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
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [445. Add Two Numbers II](../../0001-0500/0445-add-two-numbers-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/adding-two-negabinary-numbers/)
