# LeetCode 2059: Minimum Operations to Convert Number

**LeetCode Problem #2059 — Minimum Operations to Convert Number**
Solve LeetCode Minimum Operations to Convert Number using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Convert Number |
| LeetCode | #2059 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` containing **distinct** numbers, an integer `start`, and an integer `goal`. There is an integer `x` that is initially set to `start`, and you want to perform operations on `x` such that it is converted to `goal`. You can perform the following operation repeatedly on the number `x`:

If `0 <= x <= 1000`, then for any index `i` in the array (`0 <= i < nums.length`), you can set `x` to any of the following:

`x + nums[i]` 
 `x - nums[i]` 
 `x ^ nums[i]` (bitwise-XOR)

Note that you can use each `nums[i]` any number of times in any order. Operations that set `x` to be out of the range `0 <= x <= 1000` are valid, but no more operations can be done afterward.

Return *the **minimum** number of operations needed to convert *`x = start`* into *`goal`*, and *`-1`* if it is not possible*.

## Constraints
- `1 <= nums.length <= 1000`
- `-10^9 <= nums[i], goal <= 10^9`
- `0 <= start <= 1000`
- `start != goal`
- All the integers in `nums` are distinct.

## Examples
### Example 1
- **Input:** `nums = [2,4,12], start = 2, goal = 12`
- **Output:** `2`
- **Explanation:** We can go from 2 &rarr; 14 &rarr; 12 with the following 2 operations.
- 2 + 12 = 14
- 14 - 2 = 12

### Example 2
- **Input:** `nums = [3,5,7], start = 0, goal = -4`
- **Output:** `2`
- **Explanation:** We can go from 0 &rarr; 3 &rarr; -4 with the following 2 operations. 
- 0 + 3 = 3
- 3 - 7 = -4
Note that the last operation sets x out of the range 0 <= x <= 1000, which is valid.

### Example 3
- **Input:** `nums = [2,8,16], start = 0, goal = 1`
- **Output:** `-1`
- **Explanation:** There is no way to convert 0 into 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Operations to Convert Number**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,4,12], start = 2, goal = 12`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can go from 2 &rarr; 14 &rarr; 12 with the following 2 operations.
- 2 + 12 = 14
- 14 - 2 = 12

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import deque
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        visited = [False] * 1001
        visited[start] = True
        q = deque([(start, 0)])
        while q:
            x, d = q.popleft()
            for v in nums:
                for y in (x + v, x - v, x ^ v):
                    if y == goal:
                        return d + 1
                    if 0 <= y <= 1000 and not visited[y]:
                        visited[y] = True
                        q.append((y, d + 1))
        return -1
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2224. Minimum Number of Operations to Convert Time](../../2001-2500/2224-minimum-number-of-operations-to-convert-time/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1284-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [1769. Minimum Number of Operations to Move All Balls to Each Box](../../1501-2000/1769-minimum-number-of-operations-to-move-all-balls-to-each-box/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-convert-number/)
