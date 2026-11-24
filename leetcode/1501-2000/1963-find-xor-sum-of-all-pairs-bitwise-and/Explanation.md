# LeetCode 1835: Find XOR Sum of All Pairs Bitwise AND

**LeetCode Problem #1835 — Find XOR Sum of All Pairs Bitwise AND**
Solve LeetCode Find XOR Sum of All Pairs Bitwise AND using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find XOR Sum of All Pairs Bitwise AND |
| LeetCode | #1835 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **XOR sum** of a list is the bitwise `XOR` of all its elements. If the list only contains one element, then its **XOR sum** will be equal to this element.

For example, the **XOR sum** of `[1,2,3,4]` is equal to `1 XOR 2 XOR 3 XOR 4 = 4`, and the **XOR sum** of `[3]` is equal to `3`.

You are given two **0-indexed** arrays `arr1` and `arr2` that consist only of non-negative integers.

Consider the list containing the result of `arr1[i] AND arr2[j]` (bitwise `AND`) for every `(i, j)` pair where `0 <= i < arr1.length` and `0 <= j < arr2.length`.

Return *the **XOR sum** of the aforementioned list*.

## Constraints
- `1 <= arr1.length, arr2.length <= 10^5`
- `0 <= arr1[i], arr2[j] <= 10^9`

## Examples
### Example 1
- **Input:** `arr1 = [1,2,3], arr2 = [6,5]`
- **Output:** `0`
- **Explanation:** The list = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1].
The XOR sum = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0.

### Example 2
- **Input:** `arr1 = [12], arr2 = [4]`
- **Output:** `4`
- **Explanation:** The list = [12 AND 4] = [4]. The XOR sum = 4.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find XOR Sum of All Pairs Bitwise AND**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr1 = [1,2,3], arr2 = [6,5]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** The list = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1].
The XOR sum = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0.

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
from functools import reduce
import operator
from typing import List


class Solution:

  def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
    xor1 = reduce(operator.xor, arr1, 0)
    xor2 = reduce(operator.xor, arr2, 0)
    return xor1 & xor2
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
- [1863. Sum of All Subset XOR Totals](../../1501-2000/1993-sum-of-all-subset-xor-totals/)
- [2425. Bitwise XOR of All Pairings](../../2501-3000/2533-bitwise-xor-of-all-pairings/)
- [3153. Sum of Digit Differences of All Pairs](../../3001-3500/3416-sum-of-digit-differences-of-all-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/)
