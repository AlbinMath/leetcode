# LeetCode 2751: Robot Collisions

**LeetCode Problem #2751 — Robot Collisions**
Solve LeetCode Robot Collisions using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Robot Collisions |
| LeetCode | #2751 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` **1-indexed** robots, each having a position on a line, health, and movement direction.

You are given **0-indexed** integer arrays `positions`, `healths`, and a string `directions` (`directions[i]` is either **'L'** for **left** or **'R'** for **right**). All integers in `positions` are **unique**.

All robots start moving on the line** simultaneously** at the **same speed **in their given directions. If two robots ever share the same position while moving, they will **collide**.

If two robots collide, the robot with **lower health** is **removed** from the line, and the health of the other robot **decreases** **by one**. The surviving robot continues in the **same** direction it was going. If both robots have the **same** health, they are both** **removed from the line.

Your task is to determine the **health** of the robots that survive the collisions, in the same **order **that the robots were given,** **i.e. final health of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return *an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.*

**Note:** The positions may be unsorted.

## Constraints
- `1 <= positions.length == healths.length == directions.length == n <= 10^5`
- `1 <= positions[i], healths[i] <= 10^9`
- `directions[i] == 'L'` or `directions[i] == 'R'`
- All values in `positions` are distinct

## Examples
### Example 1
- **Input:** `positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"`
- **Output:** `[2,17,9,15,10]`
- **Explanation:** No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].

### Example 2
- **Input:** `positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"`
- **Output:** `[14]`
- **Explanation:** There are 2 collisions in this example. Firstly, robot 1 and robot 2 will collide, and since both have the same health, they will be removed from the line. Next, robot 3 and robot 4 will collide and since robot 4's health is smaller, it gets removed, and robot 3's health becomes 15 - 1 = 14. Only robot 3 remains, so we return [14].

### Example 3
- **Input:** `positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"`
- **Output:** `[]`
- **Explanation:** Robot 1 and robot 2 will collide and since both have the same health, they are both removed. Robot 3 and 4 will collide and since both have the same health, they are both removed. So, we return an empty array, [].

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Robot Collisions**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,17,9,15,10]`.
4. **Verification:** No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].

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
from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        order = sorted(range(len(positions)), key=lambda i: positions[i])
        stk = []
        
        for idx in order:
            if directions[idx] == 'R':
                stk.append(idx)
            else:
                while stk and healths[idx] > 0:
                    top = stk[-1]
                    if healths[top] < healths[idx]:
                        healths[top] = 0
                        stk.pop()
                        healths[idx] -= 1
                    elif healths[top] > healths[idx]:
                        healths[idx] = 0
                        healths[top] -= 1
                    else:
                        healths[top] = 0
                        healths[idx] = 0
                        stk.pop()
                        
        return [h for h in healths if h > 0]
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
- [657. Robot Return to Origin](../../0501-1000/0657-robot-return-to-origin/)
- [874. Walking Robot Simulation](../../0501-1000/0906-walking-robot-simulation/)
- [1041. Robot Bounded In Circle](../../1001-1500/1119-robot-bounded-in-circle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/robot-collisions/)
