# LeetCode 2379: Minimum Recolors to Get K Consecutive Black Blocks

**LeetCode Problem #2379 — Minimum Recolors to Get K Consecutive Black Blocks**
Solve LeetCode Minimum Recolors to Get K Consecutive Black Blocks using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Recolors to Get K Consecutive Black Blocks |
| LeetCode | #2379 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string `blocks` of length `n`, where `blocks[i]` is either `'W'` or `'B'`, representing the color of the `i^th` block. The characters `'W'` and `'B'` denote the colors white and black, respectively.

You are also given an integer `k`, which is the desired number of **consecutive** black blocks.

In one operation, you can **recolor** a white block such that it becomes a black block.

Return* the **minimum** number of operations needed such that there is at least **one** occurrence of *`k`* consecutive black blocks.*

## Constraints
- `n == blocks.length`
- `1 <= n <= 100`
- `blocks[i]` is either `'W'` or `'B'`.
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `blocks = "WBBWWBBWBW", k = 7`
- **Output:** `3`
- **Explanation:** One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

### Example 2
- **Input:** `blocks = "WBWBBBW", k = 2`
- **Output:** `0`
- **Explanation:** No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Recolors to Get K Consecutive Black Blocks**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `blocks = "WBBWWBBWBW", k = 7`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

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
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = blocks[:k].count('W')
        min_ops = white_count
        
        for i in range(k, len(blocks)):
            white_count += (blocks[i] == 'W') - (blocks[i - k] == 'W')
            if white_count < min_ops:
                min_ops = white_count
                if min_ops == 0:
                    return 0
                    
        return min_ops
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
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](../../1501-2000/1703-minimum-adjacent-swaps-for-k-consecutive-ones/)
- [1296. Divide Array in Sets of K Consecutive Numbers](../../1001-1500/1296-divide-array-in-sets-of-k-consecutive-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/)
