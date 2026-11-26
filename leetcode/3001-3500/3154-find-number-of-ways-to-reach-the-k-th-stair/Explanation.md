# LeetCode 3154: Find Number of Ways to Reach the K-th Stair

**LeetCode Problem #3154 — Find Number of Ways to Reach the K-th Stair**
Solve LeetCode Find Number of Ways to Reach the K-th Stair using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Number of Ways to Reach the K-th Stair |
| LeetCode | #3154 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **non-negative** integer `k`. There exists a staircase with an infinite number of stairs, with the **lowest** stair numbered 0.

Alice has an integer `jump`, with an initial value of 0. She starts on stair 1 and wants to reach stair `k` using **any** number of **operations**. If she is on stair `i`, in one **operation** she can:

Go down to stair `i - 1`. This operation **cannot** be used consecutively or on stair 0. 
 Go up to stair `i + 2^jump`. And then, `jump` becomes `jump + 1`.

Return the *total* number of ways Alice can reach stair `k`.

**Note** that it is possible that Alice reaches the stair `k`, and performs some operations to reach the stair `k` again.

## Constraints
- `0 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `k = 0`
- **Output:** `2`
- **Explanation:** The 2 possible ways of reaching stair 0 are: 

 
 Alice starts at stair 1.
 
 Using an operation of the first type, she goes down 1 stair to reach stair 0. 
 
 
 Alice starts at stair 1.
 
 Using an operation of the first type, she goes down 1 stair to reach stair 0. 
 Using an operation of the second type, she goes up 2^0 stairs to reach stair 1. 
 Using an operation of the first type, she goes down 1 stair to reach stair 0.

### Example 2
- **Input:** `k = 1`
- **Output:** `4`
- **Explanation:** The 4 possible ways of reaching stair 1 are: 

 
 Alice starts at stair 1. Alice is at stair 1. 
 Alice starts at stair 1.
 
 Using an operation of the first type, she goes down 1 stair to reach stair 0. 
 Using an operation of the second type, she goes up 2^0 stairs to reach stair 1. 
 
 
 Alice starts at stair 1.
 
 Using an operation of the second type, she goes up 2^0 stairs to reach stair 2. 
 Using an operation of the first type, she goes down 1 stair to reach stair 1. 
 
 
 Alice starts at stair 1.
 
 Using an operation of the first type, she goes down 1 stair to reach stair 0. 
 Using an operation of the second type, she goes up 2^0 stairs to reach stair 1. 
 Using an operation of the first type, she goes down 1 stair to reach stair 0. 
 Using an operation of the second type, she goes up 2^1 stairs to reach stair 2. 
 Using an operation of the first type, she goes down 1 stair to reach stair 1.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Number of Ways to Reach the K-th Stair**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 0`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The 2 possible ways of reaching stair 0 are: 

 
 Alice starts at stair 1.
 
 Using an operation of the first type, she goes down 1 stair to reach stair 0. 
 
 
 Alice starts at stair 1.
 
 Using an operation of the first type, she goes down 1 stair to reach stair 0. 
 Using an operation of the second type, she goes up 2^0 stairs to reach stair 1. 
 Using an operation of the first type, she goes down 1 stair to reach stair 0.

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
var waysToReachStair = function(k) {
    let ans = 0;

    function comb(n, r) {
        if (r < 0 || r > n) return 0;

        let res = 1;
        for (let i = 1; i <= r; i++) {
            res = res * (n - i + 1) / i;
        }
        return Math.round(res);
    }

    for (let j = 0; j <= 30; j++) {
        const pos = (1 << j);
        const downs = pos - k;

        if (downs >= 0 && downs <= j + 1) {
            ans += comb(j + 1, downs);
        }
    }

    return ans;
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
- [2400. Number of Ways to Reach a Position After Exactly k Steps](../../2001-2500/2400-number-of-ways-to-reach-a-position-after-exactly-k-steps/)
- [719. Find K-th Smallest Pair Distance](../../0501-1000/0719-find-k-th-smallest-pair-distance/)
- [2269. Find the K-Beauty of a Number](../../2001-2500/2269-find-the-k-beauty-of-a-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/)
