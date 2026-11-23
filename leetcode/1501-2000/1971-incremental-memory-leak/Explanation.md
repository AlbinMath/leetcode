# LeetCode 1860: Incremental Memory Leak

**LeetCode Problem #1860 — Incremental Memory Leak**
Solve LeetCode Incremental Memory Leak using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Incremental Memory Leak |
| LeetCode | #1860 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `memory1` and `memory2` representing the available memory in bits on two memory sticks. There is currently a faulty program running that consumes an increasing amount of memory every second.

At the `i^th` second (starting from 1), `i` bits of memory are allocated to the stick with **more available memory** (or from the first memory stick if both have the same available memory). If neither stick has at least `i` bits of available memory, the program **crashes**.

Return *an array containing *`[crashTime, memory1_crash, memory2_crash]`*, where *`crashTime`* is the time (in seconds) when the program crashed and *`memory1_crash`* and *`memory2_crash`* are the available bits of memory in the first and second sticks respectively*.

## Constraints
- `0 <= memory1, memory2 <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `memory1 = 2, memory2 = 2`
- **Output:** `[3,1,0]`
- **Explanation:** The memory is allocated as follows:
- At the 1^st second, 1 bit of memory is allocated to stick 1. The first stick now has 1 bit of available memory.
- At the 2^nd second, 2 bits of memory are allocated to stick 2. The second stick now has 0 bits of available memory.
- At the 3^rd second, the program crashes. The sticks have 1 and 0 bits available respectively.

### Example 2
- **Input:** `memory1 = 8, memory2 = 11`
- **Output:** `[6,0,4]`
- **Explanation:** The memory is allocated as follows:
- At the 1^st second, 1 bit of memory is allocated to stick 2. The second stick now has 10 bit of available memory.
- At the 2^nd second, 2 bits of memory are allocated to stick 2. The second stick now has 8 bits of available memory.
- At the 3^rd second, 3 bits of memory are allocated to stick 1. The first stick now has 5 bits of available memory.
- At the 4^th second, 4 bits of memory are allocated to stick 2. The second stick now has 4 bits of available memory.
- At the 5^th second, 5 bits of memory are allocated to stick 1. The first stick now has 0 bits of available memory.
- At the 6^th second, the program crashes. The sticks have 0 and 4 bits available respectively.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Incremental Memory Leak**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `memory1 = 2, memory2 = 2`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,1,0]`.
4. **Verification:** The memory is allocated as follows:
- At the 1^st second, 1 bit of memory is allocated to stick 1. The first stick now has 1 bit of available memory.
- At the 2^nd second, 2 bits of memory are allocated to stick 2. The second stick now has 0 bits of available memory.
- At the 3^rd second, the program crashes. The sticks have 1 and 0 bits available respectively.

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
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        while max(memory1, memory2) >= i:
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i += 1
        return [i, memory1, memory2]
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
- [2502. Design Memory Allocator](../../2501-3000/2587-design-memory-allocator/)
- [3887. Incremental Even-Weighted Cycle Queries](../../4001-4500/4114-incremental-even-weighted-cycle-queries/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/incremental-memory-leak/)
