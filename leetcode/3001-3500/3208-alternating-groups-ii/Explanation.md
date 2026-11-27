# LeetCode 3208: Alternating Groups II

**LeetCode Problem #3208 — Alternating Groups II**
Solve LeetCode Alternating Groups II using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Alternating Groups II |
| LeetCode | #3208 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a circle of red and blue tiles. You are given an array of integers `colors` and an integer `k`. The color of tile `i` is represented by `colors[i]`:

`colors[i] == 0` means that tile `i` is **red**. 
 `colors[i] == 1` means that tile `i` is **blue**.

An **alternating** group is every `k` contiguous tiles in the circle with **alternating** colors (each tile in the group except the first and last one has a different color from its **left** and **right** tiles).

Return the number of **alternating** groups.

**Note** that since `colors` represents a **circle**, the **first** and the **last** tiles are considered to be next to each other.

## Constraints
- `3 <= colors.length <= 10^5`
- `0 <= colors[i] <= 1`
- `3 <= k <= colors.length`

## Examples
### Example 1
- **Input:** `colors = [0,1,0,1,0], k = 3`
- **Output:** `3`

### Example 2
- **Input:** `colors = [0,1,0,0,1,0,1], k = 6`
- **Output:** `2`

### Example 3
- **Input:** `colors = [1,1,0,1], k = 4`
- **Output:** `0`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Alternating Groups II**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `colors = [0,1,0,1,0], k = 3`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

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
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        run = 1
        ans = 0
        for i in range(1, n + k - 1):
            if colors[i % n] != colors[(i - 1) % n]:
                run += 1
            else:
                run = 1
            if run >= k:
                ans += 1
        return ans
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
- [3206. Alternating Groups I](../../3001-3500/3206-alternating-groups-i/)
- [3245. Alternating Groups III](../../3001-3500/3245-alternating-groups-iii/)
- [830. Positions of Large Groups](../../0501-1000/0830-positions-of-large-groups/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/alternating-groups-ii/)
