# LeetCode 858: Mirror Reflection

**LeetCode Problem #858 — Mirror Reflection**
Solve LeetCode Mirror Reflection using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Mirror Reflection |
| LeetCode | #858 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered `0`, `1`, and `2`.

The square room has walls of length `p` and a laser ray from the southwest corner first meets the east wall at a distance `q` from the `0^th` receptor.

Given the two integers `p` and `q`, return *the number of the receptor that the ray meets first*.

The test cases are guaranteed so that the ray will meet a receptor eventually.

## Constraints
- `1 <= q <= p <= 1000`

## Examples
### Example 1
- **Input:** `p = 2, q = 1`
- **Output:** `2`
- **Explanation:** The ray meets receptor 2 the first time it gets reflected back to the left wall.

### Example 2
- **Input:** `p = 3, q = 1`
- **Output:** `1`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Mirror Reflection**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `p = 2, q = 1`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The ray meets receptor 2 the first time it gets reflected back to the left wall.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from math import gcd

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        p //= g
        q //= g
        if p % 2 == 0:
            return 2
        return 1 if q % 2 == 1 else 0
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2081. Sum of k-Mirror Numbers](../../2001-2500/2081-sum-of-k-mirror-numbers/)
- [3412. Find Mirror Score of a String](../../3001-3500/3412-find-mirror-score-of-a-string/)
- [3665. Twisted Mirror Path Count](../../3501-4000/3665-twisted-mirror-path-count/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/mirror-reflection/)
