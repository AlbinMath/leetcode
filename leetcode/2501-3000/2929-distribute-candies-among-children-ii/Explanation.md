# LeetCode 2929: Distribute Candies Among Children II

**LeetCode Problem #2929 — Distribute Candies Among Children II**
Solve LeetCode Distribute Candies Among Children II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distribute Candies Among Children II |
| LeetCode | #2929 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two positive integers `n` and `limit`.

Return *the **total number** of ways to distribute *`n` *candies among *`3`* children such that no child gets more than *`limit`* candies.*

## Constraints
- `1 <= n <= 10^6`
- `1 <= limit <= 10^6`

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
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Distribute Candies Among Children II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, limit = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var distributeCandies = function(n, limit) {
    const C2 = x => x < 2 ? 0 : x * (x - 1) / 2;

    return C2(n + 2)
         - 3 * C2(n - limit + 1)
         + 3 * C2(n - 2 * limit)
         - C2(n - 3 * limit - 1);
};
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
- [2928. Distribute Candies Among Children I](../../2501-3000/2928-distribute-candies-among-children-i/)
- [2226. Maximum Candies Allocated to K Children](../../2001-2500/2226-maximum-candies-allocated-to-k-children/)
- [575. Distribute Candies](../../0501-1000/0575-distribute-candies/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distribute-candies-among-children-ii/)
