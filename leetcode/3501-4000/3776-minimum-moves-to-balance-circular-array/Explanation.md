# LeetCode 3776: Minimum Moves to Balance Circular Array

**LeetCode Problem #3776 — Minimum Moves to Balance Circular Array**
Solve LeetCode Minimum Moves to Balance Circular Array using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Balance Circular Array |
| LeetCode | #3776 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **circular** array `balance` of length `n`, where `balance[i]` is the net balance of person `i`.

In one move, a person can transfer **exactly** 1 unit of balance to either their left or right neighbor.

Return the **minimum** number of moves required so that every person has a **non-negative** balance. If it is impossible, return `-1`.

**Note**: You are guaranteed that **at most** 1 index has a **negative** balance initially.

## Constraints
- `1 <= n == balance.length <= 10^5`
- `-10^9 <= balance[i] <= 10^9`
- There is at most one negative value in `balance` initially.

## Examples
### Example 1
- **Input:** `balance = [5,1,-4]`
- **Output:** `4`
- **Explanation:** One optimal sequence of moves is: 

 
 Move 1 unit from `i = 1` to `i = 2`, resulting in `balance = [5, 0, -3]` 
 Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [4, 0, -2]` 
 Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [3, 0, -1]` 
 Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [2, 0, 0]` 
 

 Thus, the minimum number of moves required is 4.

### Example 2
- **Input:** `balance = [1,2,-5,2]`
- **Output:** `6`
- **Explanation:** One optimal sequence of moves is: 

 
 Move 1 unit from `i = 1` to `i = 2`, resulting in `balance = [1, 1, -4, 2]` 
 Move 1 unit from `i = 1` to `i = 2`, resulting in `balance = [1, 0, -3, 2]` 
 Move 1 unit from `i = 3` to `i = 2`, resulting in `balance = [1, 0, -2, 1]` 
 Move 1 unit from `i = 3` to `i = 2`, resulting in `balance = [1, 0, -1, 0]` 
 Move 1 unit from `i = 0` to `i = 1`, resulting in `balance = [0, 1, -1, 0]` 
 Move 1 unit from `i = 1` to `i = 2`, resulting in `balance = [0, 0, 0, 0]` 
 

 Thus, the minimum number of moves required is 6.​​​

### Example 3
- **Input:** `balance = [-3,2]`
- **Output:** `-1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Moves to Balance Circular Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `balance = [5,1,-4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** One optimal sequence of moves is: 

 
 Move 1 unit from `i = 1` to `i = 2`, resulting in `balance = [5, 0, -3]` 
 Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [4, 0, -2]` 
 Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [3, 0, -1]` 
 Move 1 unit from `i = 0` to `i = 2`, resulting in `balance = [2, 0, 0]` 
 

 Thus, the minimum number of moves required is 4.

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
var minMoves = function(balance) {
    const n = balance.length;

    let total = 0;
    let negativeIndex = -1;

    for (let i = 0; i < n; i++) {
        total += balance[i];

        if (balance[i] < 0) {
            negativeIndex = i;
        }
    }

    if (total < 0) return -1;

    if (negativeIndex === -1) return 0;

    let needed = -balance[negativeIndex];
    let moves = 0;

    for (let distance = 1; distance <= Math.floor(n / 2); distance++) {
        const left = (negativeIndex - distance + n) % n;
        const right = (negativeIndex + distance) % n;

        const indices = left === right ? [left] : [left, right];

        for (const index of indices) {
            const available = balance[index];
            const take = Math.min(needed, available);

            moves += take * distance;
            needed -= take;

            if (needed === 0) return moves;
        }
    }

    return -1;
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
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)
- [462. Minimum Moves to Equal Array Elements II](../../0001-0500/0462-minimum-moves-to-equal-array-elements-ii/)
- [1674. Minimum Moves to Make Array Complementary](../../1501-2000/1674-minimum-moves-to-make-array-complementary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-balance-circular-array/)
