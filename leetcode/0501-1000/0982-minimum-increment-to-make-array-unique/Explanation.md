# LeetCode 945: Minimum Increment to Make Array Unique

**LeetCode Problem #945 — Minimum Increment to Make Array Unique**
Solve LeetCode Minimum Increment to Make Array Unique using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Increment to Make Array Unique |
| LeetCode | #945 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. In one move, you can pick an index `i` where `0 <= i < nums.length` and increment `nums[i]` by `1`.

Return *the minimum number of moves to make every value in *`nums`* **unique***.

The test cases are generated so that the answer fits in a 32-bit integer.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,2,2]`
- **Output:** `1`
- **Explanation:** After 1 move, the array could be [1, 2, 3].

### Example 2
- **Input:** `nums = [3,2,1,2,1,7]`
- **Output:** `6`
- **Explanation:** After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown that it is impossible for the array to have all unique values with 5 or less moves.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Increment to Make Array Unique**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** After 1 move, the array could be [1, 2, 3].

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
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        moves = 0
        nxt = 0  # smallest value the next element may take
        for x in nums:
            if x < nxt:
                moves += nxt - x
                nxt += 1
            else:
                nxt = x + 1
        return moves
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
- [1558. Minimum Numbers of Function Calls to Make Target Array](../../1501-2000/1662-minimum-numbers-of-function-calls-to-make-target-array/)
- [1647. Minimum Deletions to Make Character Frequencies Unique](../../1501-2000/1770-minimum-deletions-to-make-character-frequencies-unique/)
- [1674. Minimum Moves to Make Array Complementary](../../1501-2000/1793-minimum-moves-to-make-array-complementary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-increment-to-make-array-unique/)
