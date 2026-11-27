# LeetCode 2928: Distribute Candies Among Children I

**LeetCode Problem #2928 — Distribute Candies Among Children I**
Solve LeetCode Distribute Candies Among Children I using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distribute Candies Among Children I |
| LeetCode | #2928 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two positive integers `n` and `limit`.

Return *the **total number** of ways to distribute *`n` *candies among *`3`* children such that no child gets more than *`limit`* candies.*

## Constraints
- `1 <= n <= 50`
- `1 <= limit <= 50`

## Examples
### Example 1
- **Input:** `n = 5, limit = 2`
- **Output:** `3`
- **Explanation:** There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

### Example 2
- **Input:** `n = 3, limit = 3`
- **Output:** `10`
- **Explanation:** There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Distribute Candies Among Children I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, limit = 2`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

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
var distributeCandies = function(n, limit) {
    let ways = 0;

    for (let a = 0; a <= Math.min(n, limit); a++) {
        for (let b = 0; b <= Math.min(n - a, limit); b++) {
            const c = n - a - b;

            if (c >= 0 && c <= limit) {
                ways++;
            }
        }
    }

    return ways;
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
- [2929. Distribute Candies Among Children II](../../2501-3000/2929-distribute-candies-among-children-ii/)
- [575. Distribute Candies](../../0501-1000/0575-distribute-candies/)
- [1103. Distribute Candies to People](../../1001-1500/1103-distribute-candies-to-people/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distribute-candies-among-children-i/)
