# LeetCode 3178: Find the Child Who Has the Ball After K Seconds

**LeetCode Problem #3178 — Find the Child Who Has the Ball After K Seconds**
Solve LeetCode Find the Child Who Has the Ball After K Seconds using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Child Who Has the Ball After K Seconds |
| LeetCode | #3178 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **positive** integers `n` and `k`. There are `n` children numbered from `0` to `n - 1` standing in a queue *in order* from left to right.

Initially, child 0 holds a ball and the direction of passing the ball is towards the right direction. After each second, the child holding the ball passes it to the child next to them. Once the ball reaches **either** end of the line, i.e. child 0 or child `n - 1`, the direction of passing is **reversed**.

Return the number of the child who receives the ball after `k` seconds.

## Constraints
- `2 <= n <= 50`
- `1 <= k <= 50`

## Examples
### Example 1
- **Input:** `n = 3, k = 5`
- **Output:** `1`
- **Explanation:** Time elapsed 
 Children 
 
 
 `0` 
 `[ 0 , 1, 2]` 
 
 
 `1` 
 `[0, 1 , 2]` 
 
 
 `2` 
 `[0, 1, 2 ]` 
 
 
 `3` 
 `[0, 1 , 2]` 
 
 
 `4` 
 `[ 0 , 1, 2]` 
 
 
 `5` 
 `[0, 1 , 2]`

### Example 2
- **Input:** `n = 5, k = 6`
- **Output:** `2`
- **Explanation:** Time elapsed 
 Children 
 
 
 `0` 
 `[ 0 , 1, 2, 3, 4]` 
 
 
 `1` 
 `[0, 1 , 2, 3, 4]` 
 
 
 `2` 
 `[0, 1, 2 , 3, 4]` 
 
 
 `3` 
 `[0, 1, 2, 3 , 4]` 
 
 
 `4` 
 `[0, 1, 2, 3, 4 ]` 
 
 
 `5` 
 `[0, 1, 2, 3 , 4]` 
 
 
 `6` 
 `[0, 1, 2 , 3, 4]`

### Example 3
- **Input:** `n = 4, k = 2`
- **Output:** `2`
- **Explanation:** Time elapsed 
 Children 
 
 
 `0` 
 `[ 0 , 1, 2, 3]` 
 
 
 `1` 
 `[0, 1 , 2, 3]` 
 
 
 `2` 
 `[0, 1, 2 , 3]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Child Who Has the Ball After K Seconds**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, k = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Time elapsed 
 Children 
 
 
 `0` 
 `[ 0 , 1, 2]` 
 
 
 `1` 
 `[0, 1 , 2]` 
 
 
 `2` 
 `[0, 1, 2 ]` 
 
 
 `3` 
 `[0, 1 , 2]` 
 
 
 `4` 
 `[ 0 , 1, 2]` 
 
 
 `5` 
 `[0, 1 , 2]`

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
var numberOfChild = function(n, k) {
    const cycleLen = 2 * (n - 1);
    const rem = k % cycleLen;
    return rem <= n - 1 ? rem : cycleLen - rem;
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
- [3179. Find the N-th Value After K Seconds](../../3001-3500/3179-find-the-n-th-value-after-k-seconds/)
- [1377. Frog Position After T Seconds](../../1001-1500/1377-frog-position-after-t-seconds/)
- [373. Find K Pairs with Smallest Sums](../../0001-0500/0373-find-k-pairs-with-smallest-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/)
