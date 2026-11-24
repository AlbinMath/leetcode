# LeetCode 1310: XOR Queries of a Subarray

**LeetCode Problem #1310 — XOR Queries of a Subarray**
Solve LeetCode XOR Queries of a Subarray using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | XOR Queries of a Subarray |
| LeetCode | #1310 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `arr` of positive integers. You are also given the array `queries` where `queries[i] = [left_i, right_i]`.

For each query `i` compute the **XOR** of elements from `left_i` to `right_i` (that is, `arr[left_i] XOR arr[left_i + 1] XOR ... XOR arr[right_i]` ).

Return an array `answer` where `answer[i]` is the answer to the `i^th` query.

## Constraints
- `1 <= arr.length, queries.length <= 3 * 10^4`
- `1 <= arr[i] <= 10^9`
- `queries[i].length == 2`
- `0 <= left_i <= right_i < arr.length`

## Examples
### Example 1
- **Input:** `arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]`
- **Output:** `[2,7,14,8]`
- **Explanation:** The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8

### Example 2
- **Input:** `arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]`
- **Output:** `[8,0,4,4]`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **XOR Queries of a Subarray**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,7,14,8]`.
4. **Verification:** The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8

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
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        p = [0] * (len(arr) + 1)
        for i, x in enumerate(arr):
            p[i + 1] = p[i] ^ x
        return [p[r + 1] ^ p[l] for l, r in queries]
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
- [3755. Find Maximum Balanced XOR Subarray Length](../../3501-4000/3755-find-maximum-balanced-xor-subarray-length/)
- [3845. Maximum Subarray XOR with Bounded Range](../../3501-4000/3845-maximum-subarray-xor-with-bounded-range/)
- [2564. Substring XOR Queries](../../2501-3000/2564-substring-xor-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/xor-queries-of-a-subarray/)
