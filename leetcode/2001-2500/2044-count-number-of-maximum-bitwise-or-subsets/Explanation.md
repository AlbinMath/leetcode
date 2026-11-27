# LeetCode 2044: Count Number of Maximum Bitwise-OR Subsets

**LeetCode Problem #2044 — Count Number of Maximum Bitwise-OR Subsets**
Solve LeetCode Count Number of Maximum Bitwise-OR Subsets using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Maximum Bitwise-OR Subsets |
| LeetCode | #2044 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `nums`, find the **maximum** possible **bitwise OR** of a subset of `nums` and return *the **number of different non-empty subsets** with the maximum bitwise OR*.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`. Two subsets are considered **different** if the indices of the elements chosen are different.

The bitwise OR of an array `a` is equal to `a[0] **OR** a[1] **OR** ... **OR** a[a.length - 1]` (**0-indexed**).

## Constraints
- `1 <= nums.length <= 16`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [3,1]`
- **Output:** `2`
- **Explanation:** The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]

### Example 2
- **Input:** `nums = [2,2,2]`
- **Output:** `7`
- **Explanation:** All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 2^3 - 1 = 7 total subsets.

### Example 3
- **Input:** `nums = [3,2,1,5]`
- **Output:** `6`
- **Explanation:** The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Number of Maximum Bitwise-OR Subsets**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        for x in nums:
            target |= x

        n = len(nums)

        def dfs(i: int, cur: int) -> int:
            if i == n:
                return 1 if cur == target else 0
            return dfs(i + 1, cur | nums[i]) + dfs(i + 1, cur)

        return dfs(0, 0)
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2572. Count the Number of Square-Free Subsets](../../2501-3000/2572-count-the-number-of-square-free-subsets/)
- [1994. The Number of Good Subsets](../../1501-2000/1994-the-number-of-good-subsets/)
- [2597. The Number of Beautiful Subsets](../../2501-3000/2597-the-number-of-beautiful-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/)
