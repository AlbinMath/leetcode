# LeetCode 2275: Largest Combination With Bitwise AND Greater Than Zero

**LeetCode Problem #2275 — Largest Combination With Bitwise AND Greater Than Zero**
Solve LeetCode Largest Combination With Bitwise AND Greater Than Zero using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Combination With Bitwise AND Greater Than Zero |
| LeetCode | #2275 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **bitwise AND** of an array `nums` is the bitwise AND of all integers in `nums`.

For example, for `nums = [1, 5, 3]`, the bitwise AND is equal to `1 & 5 & 3 = 1`. 
 Also, for `nums = [7]`, the bitwise AND is `7`.

You are given an array of positive integers `candidates`. Compute the **bitwise AND** for all possible **combinations** of elements in the `candidates` array.

Return *the size of the **largest** combination of *`candidates`* with a bitwise AND **greater** than *`0`.

## Constraints
- `1 <= candidates.length <= 10^5`
- `1 <= candidates[i] <= 10^7`

## Examples
### Example 1
- **Input:** `candidates = [16,17,71,62,12,24,14]`
- **Output:** `4`
- **Explanation:** The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.

### Example 2
- **Input:** `candidates = [8,8]`
- **Output:** `2`
- **Explanation:** The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
The size of the combination is 2, so we return 2.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Combination With Bitwise AND Greater Than Zero**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `candidates = [16,17,71,62,12,24,14]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List


class Solution:

  def largestCombination(self, candidates: List[int]) -> int:
    return max(
        sum((num >> bit) & 1 for num in candidates) for bit in range(24)
    )
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [982. Triples with Bitwise AND Equal To Zero](../../1001-1500/1024-triples-with-bitwise-and-equal-to-zero/)
- [3702. Longest Subsequence With Non-Zero Bitwise XOR](../../4001-4500/4033-longest-subsequence-with-non-zero-bitwise-xor/)
- [3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND](../../4001-4500/4032-longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/)
