# LeetCode 1344: Angle Between Hands of a Clock

**LeetCode Problem #1344 — Angle Between Hands of a Clock**
Solve LeetCode Angle Between Hands of a Clock using Java and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Angle Between Hands of a Clock |
| LeetCode | #1344 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two numbers, `hour` and `minutes`, return *the smaller angle (in degrees) formed between the *`hour`* and the *`minute`* hand*.

Answers within `10^-5` of the actual value will be accepted as correct.

## Constraints
- `1 <= hour <= 12`
- `0 <= minutes <= 59`

## Examples
### Example 1
- **Input:** `hour = 12, minutes = 30`
- **Output:** `165`

### Example 2
- **Input:** `hour = 3, minutes = 30`
- **Output:** `75`

### Example 3
- **Input:** `hour = 3, minutes = 15`
- **Output:** `7.5`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
1. **Minute Hand Angle:** Each minute moves the minute hand by `6°` → `minuteAngle = minutes * 6.0`.
2. **Hour Hand Angle:** Each hour moves the hour hand by `30°`, and each minute moves it by `0.5°` → `hourAngle = (hour % 12) * 30.0 + minutes * 0.5`.
3. **Angle Between:** The absolute difference gives one angle. The other angle is `360 - difference`. Return the smaller of the two.

Time and space complexity are both $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `hour = 12, minutes = 30`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `165`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public double angleClock(int hour, int minutes) {
        // Minute hand: 6 degrees per minute
        double minuteAngle = minutes * 6.0;

        // Hour hand: 30 degrees per hour + 0.5 degrees per minute
        double hourAngle = (hour % 12) * 30.0 + minutes * 0.5;

        double angle = Math.abs(hourAngle - minuteAngle);

        // Return the smaller angle
        return Math.min(angle, 360.0 - angle);
    }
}
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
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0783-minimum-distance-between-bst-nodes/)
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1026-maximum-difference-between-node-and-ancestor/)
- [1190. Reverse Substrings Between Each Pair of Parentheses](../../1001-1500/1190-reverse-substrings-between-each-pair-of-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/angle-between-hands-of-a-clock/)
