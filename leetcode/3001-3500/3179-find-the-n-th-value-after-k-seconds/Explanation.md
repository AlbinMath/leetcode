# LeetCode 3179: Find the N-th Value After K Seconds

**LeetCode Problem #3179 — Find the N-th Value After K Seconds**
Solve LeetCode Find the N-th Value After K Seconds using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the N-th Value After K Seconds |
| LeetCode | #3179 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `n` and `k`.

Initially, you start with an array `a` of `n` integers where `a[i] = 1` for all `0 <= i <= n - 1`. After each second, you simultaneously update each element to be the sum of all its preceding elements plus the element itself. For example, after one second, `a[0]` remains the same, `a[1]` becomes `a[0] + a[1]`, `a[2]` becomes `a[0] + a[1] + a[2]`, and so on.

Return the **value** of `a[n - 1]` after `k` seconds.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= n, k <= 1000`

## Examples
### Example 1
- **Input:** `n = 4, k = 5`
- **Output:** `56`
- **Explanation:** Second 
 State After 
 
 
 0 
 [1,1,1,1] 
 
 
 1 
 [1,2,3,4] 
 
 
 2 
 [1,3,6,10] 
 
 
 3 
 [1,4,10,20] 
 
 
 4 
 [1,5,15,35] 
 
 
 5 
 [1,6,21,56]

### Example 2
- **Input:** `n = 5, k = 3`
- **Output:** `35`
- **Explanation:** Second 
 State After 
 
 
 0 
 [1,1,1,1,1] 
 
 
 1 
 [1,2,3,4,5] 
 
 
 2 
 [1,3,6,10,15] 
 
 
 3 
 [1,4,10,20,35]

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the N-th Value After K Seconds**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, k = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `56`.
4. **Verification:** Second 
 State After 
 
 
 0 
 [1,1,1,1] 
 
 
 1 
 [1,2,3,4] 
 
 
 2 
 [1,3,6,10] 
 
 
 3 
 [1,4,10,20] 
 
 
 4 
 [1,5,15,35] 
 
 
 5 
 [1,6,21,56]

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
var valueAfterKSeconds = function(n, k) {
    const MOD = 1000000007;
    const arr = new Array(n).fill(1);

    for (let t = 0; t < k; t++) {
        for (let i = 1; i < n; i++) {
            arr[i] = (arr[i] + arr[i - 1]) % MOD;
        }
    }

    return arr[n - 1];
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
- [3178. Find the Child Who Has the Ball After K Seconds](../../3001-3500/3178-find-the-child-who-has-the-ball-after-k-seconds/)
- [1415. The k-th Lexicographical String of All Happy Strings of Length n](../../1001-1500/1415-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)
- [3154. Find Number of Ways to Reach the K-th Stair](../../3001-3500/3154-find-number-of-ways-to-reach-the-k-th-stair/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/)
