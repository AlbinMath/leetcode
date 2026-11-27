# LeetCode 2582: Pass the Pillow

**LeetCode Problem #2582 — Pass the Pillow**
Solve LeetCode Pass the Pillow using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Pass the Pillow |
| LeetCode | #2582 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` people standing in a line labeled from `1` to `n`. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the `n^th` person they pass it to the `n - 1^th` person, then to the `n - 2^th` person and so on.

Given the two positive integers `n` and `time`, return *the index of the person holding the pillow after *`time`* seconds*.

## Constraints
- `2 <= n <= 1000`
- `1 <= time <= 1000`

## Examples
### Example 1
- **Input:** `n = 4, time = 5`
- **Output:** `2`
- **Explanation:** People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
After five seconds, the 2^nd person is holding the pillow.

### Example 2
- **Input:** `n = 3, time = 2`
- **Output:** `3`
- **Explanation:** People pass the pillow in the following way: 1 -> 2 -> 3.
After two seconds, the 3^r^d person is holding the pillow.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Pass the Pillow**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, time = 5`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
After five seconds, the 2^nd person is holding the pillow.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var passThePillow = function(n, time) {
    const fullTrips = Math.floor(time / (n - 1));
    const remainder = time % (n - 1);

    if (fullTrips % 2 === 0) {
        return 1 + remainder;
    }
    return n - remainder;
};
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
- [1792. Maximum Average Pass Ratio](../../1501-2000/1792-maximum-average-pass-ratio/)
- [48. Rotate Image](../../0001-0500/0048-rotate-image/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/pass-the-pillow/)
