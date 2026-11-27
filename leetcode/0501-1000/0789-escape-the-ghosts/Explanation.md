# LeetCode 789: Escape The Ghosts

**LeetCode Problem #789 — Escape The Ghosts**
Solve LeetCode Escape The Ghosts using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Escape The Ghosts |
| LeetCode | #789 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point `[0, 0]`, and you are given a destination point `target = [x_target, y_target]` that you are trying to get to. There are several ghosts on the map with their starting positions given as a 2D array `ghosts`, where `ghosts[i] = [x_i, y_i]` represents the starting position of the `i^th` ghost. All inputs are **integral coordinates**.

Each turn, you and all the ghosts may independently choose to either **move 1 unit** in any of the four cardinal directions: north, east, south, or west, or **stay still**. All actions happen **simultaneously**.

You escape if and only if you can reach the target **before** any ghost reaches you. If you reach any square (including the target) at the **same time** as a ghost, it **does not** count as an escape.

Return `true`* if it is possible to escape regardless of how the ghosts move, otherwise return *`false`*.*

## Constraints
- `1 <= ghosts.length <= 100`
- `ghosts[i].length == 2`
- `-10^4 <= x_i, y_i <= 10^4`
- There can be **multiple ghosts** in the same location.
- `target.length == 2`
- `-10^4 <= x_target, y_target <= 10^4`

## Examples
### Example 1
- **Input:** `ghosts = [[1,0],[0,3]], target = [0,1]`
- **Output:** `true`
- **Explanation:** You can reach the destination (0, 1) after 1 turn, while the ghosts located at (1, 0) and (0, 3) cannot catch up with you.

### Example 2
- **Input:** `ghosts = [[1,0]], target = [2,0]`
- **Output:** `false`
- **Explanation:** You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.

### Example 3
- **Input:** `ghosts = [[2,0]], target = [1,0]`
- **Output:** `false`
- **Explanation:** The ghost can reach the target at the same time as you.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Escape The Ghosts**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `ghosts = [[1,0],[0,3]], target = [0,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** You can reach the destination (0, 1) after 1 turn, while the ghosts located at (1, 0) and (0, 3) cannot catch up with you.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        tx, ty = target
        player_dist = abs(tx) + abs(ty)
        
        for gx, gy in ghosts:
            ghost_dist = abs(gx - tx) + abs(gy - ty)
            if ghost_dist <= player_dist:
                return False
                
        return True
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1036. Escape a Large Maze](../../1001-1500/1036-escape-a-large-maze/)
- [2258. Escape the Spreading Fire](../../2001-2500/2258-escape-the-spreading-fire/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/escape-the-ghosts/)
