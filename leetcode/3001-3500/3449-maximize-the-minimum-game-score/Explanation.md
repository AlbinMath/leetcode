# LeetCode 3449: Maximize the Minimum Game Score

**LeetCode Problem #3449 — Maximize the Minimum Game Score**
Solve LeetCode Maximize the Minimum Game Score using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Minimum Game Score |
| LeetCode | #3449 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `points` of size `n` and an integer `m`. There is another array `gameScore` of size `n`, where `gameScore[i]` represents the score achieved at the `i^th` game. Initially, `gameScore[i] == 0` for all `i`.

You start at index -1, which is outside the array (before the first position at index 0). You can make **at most** `m` moves. In each move, you can either:

Increase the index by 1 and add `points[i]` to `gameScore[i]`. 
 Decrease the index by 1 and add `points[i]` to `gameScore[i]`.

**Note** that the index must always remain within the bounds of the array after the first move.

Return the **maximum possible minimum** value in `gameScore` after **at most** `m` moves.

## Constraints
- `2 <= n == points.length <= 5 * 10^4`
- `1 <= points[i] <= 10^6`
- `1 <= m <= 10^9`

## Examples
### Example 1
- **Input:** `points = [2,4], m = 3`
- **Output:** `4`
- **Explanation:** Initially, index `i = -1` and `gameScore = [0, 0]`. 

 
 
 
 Move 
 Index 
 gameScore 
 
 
 
 
 Increase `i` 
 0 
 `[2, 0]` 
 
 
 Increase `i` 
 1 
 `[2, 4]` 
 
 
 Decrease `i` 
 0 
 `[4, 4]` 
 
 
 

 The minimum value in `gameScore` is 4, and this is the maximum possible minimum among all configurations. Hence, 4 is the output.

### Example 2
- **Input:** `points = [1,2,3], m = 5`
- **Output:** `2`
- **Explanation:** Initially, index `i = -1` and `gameScore = [0, 0, 0]`. 

 
 
 
 Move 
 Index 
 gameScore 
 
 
 
 
 Increase `i` 
 0 
 `[1, 0, 0]` 
 
 
 Increase `i` 
 1 
 `[1, 2, 0]` 
 
 
 Decrease `i` 
 0 
 `[2, 2, 0]` 
 
 
 Increase `i` 
 1 
 `[2, 4, 0]` 
 
 
 Increase `i` 
 2 
 `[2, 4, 3]` 
 
 
 

 The minimum value in `gameScore` is 2, and this is the maximum possible minimum among all configurations. Hence, 2 is the output.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize the Minimum Game Score**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [2,4], m = 3`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Initially, index `i = -1` and `gameScore = [0, 0]`. 

 
 
 
 Move 
 Index 
 gameScore 
 
 
 
 
 Increase `i` 
 0 
 `[2, 0]` 
 
 
 Increase `i` 
 1 
 `[2, 4]` 
 
 
 Decrease `i` 
 0 
 `[4, 4]` 
 
 
 

 The minimum value in `gameScore` is 4, and this is the maximum possible minimum among all configurations. Hence, 4 is the output.

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
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)

        def check(x: int) -> bool:
            rem = m
            pre = 0
            for i in range(n):
                k = -(-x // points[i]) - pre      # ceil(x / p) - pre
                if i == n - 1 and k <= 0:
                    break
                if k < 1:
                    k = 1
                rem -= 2 * k - 1
                if rem < 0:
                    return False
                pre = k - 1
            return True

        lo, hi = 0, 10**15
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
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
- [2836. Maximize Value of Function in a Ball Passing Game](../../2501-3000/2836-maximize-value-of-function-in-a-ball-passing-game/)
- [2974. Minimum Number Game](../../2501-3000/2974-minimum-number-game/)
- [3847. Find the Score Difference in a Game](../../3501-4000/3847-find-the-score-difference-in-a-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-minimum-game-score/)
