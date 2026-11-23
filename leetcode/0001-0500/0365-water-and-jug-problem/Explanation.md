# LeetCode 365: Water and Jug Problem

**LeetCode Problem #365 — Water and Jug Problem**
Solve LeetCode Water and Jug Problem using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Water and Jug Problem |
| LeetCode | #365 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two jugs with capacities `x` liters and `y` liters. You have an infinite water supply. Return whether the total amount of water in both jugs may reach `target` using the following operations:

Fill either jug completely with water. 
 Completely empty either jug. 
 Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty.

## Constraints
- `1 <= x, y, target <= 10^3`

## Examples
### Example 1
- **Input:** `x = 3, y = 5, target = 4`
- **Output:** `true`
- **Explanation:** Follow these steps to reach a total of 4 liters: 

 
 Fill the 5-liter jug (0, 5). 
 Pour from the 5-liter jug into the 3-liter jug, leaving 2 liters (3, 2). 
 Empty the 3-liter jug (0, 2). 
 Transfer the 2 liters from the 5-liter jug to the 3-liter jug (2, 0). 
 Fill the 5-liter jug again (2, 5). 
 Pour from the 5-liter jug into the 3-liter jug until the 3-liter jug is full. This leaves 4 liters in the 5-liter jug (3, 4). 
 Empty the 3-liter jug. Now, you have exactly 4 liters in the 5-liter jug (0, 4). 
 

 Reference: The Die Hard example.

### Example 2
- **Input:** `x = 2, y = 6, target = 5`
- **Output:** `false`

### Example 3
- **Input:** `x = 1, y = 2, target = 3`
- **Output:** `true`
- **Explanation:** Fill both jugs. The total amount of water in both jugs is equal to 3 now.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Water and Jug Problem**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `x = 3, y = 5, target = 4`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Follow these steps to reach a total of 4 liters: 

 
 Fill the 5-liter jug (0, 5). 
 Pour from the 5-liter jug into the 3-liter jug, leaving 2 liters (3, 2). 
 Empty the 3-liter jug (0, 2). 
 Transfer the 2 liters from the 5-liter jug to the 3-liter jug (2, 0). 
 Fill the 5-liter jug again (2, 5). 
 Pour from the 5-liter jug into the 3-liter jug until the 3-liter jug is full. This leaves 4 liters in the 5-liter jug (3, 4). 
 Empty the 3-liter jug. Now, you have exactly 4 liters in the 5-liter jug (0, 4). 
 

 Reference: The Die Hard example.

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
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        return target <= x + y and target % gcd(x, y) == 0
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
- [218. The Skyline Problem](../../0001-0500/0218-the-skyline-problem/)
- [11. Container With Most Water](../../0001-0500/0011-container-with-most-water/)
- [42. Trapping Rain Water](../../0001-0500/0042-trapping-rain-water/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/water-and-jug-problem/)
