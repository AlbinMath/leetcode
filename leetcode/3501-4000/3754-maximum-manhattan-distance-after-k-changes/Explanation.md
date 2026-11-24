# LeetCode 3443: Maximum Manhattan Distance After K Changes

**LeetCode Problem #3443 — Maximum Manhattan Distance After K Changes**
Solve LeetCode Maximum Manhattan Distance After K Changes using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Manhattan Distance After K Changes |
| LeetCode | #3443 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of the characters `'N'`, `'S'`, `'E'`, and `'W'`, where `s[i]` indicates movements in an infinite grid:

`'N'` : Move north by 1 unit. 
 `'S'` : Move south by 1 unit. 
 `'E'` : Move east by 1 unit. 
 `'W'` : Move west by 1 unit.

Initially, you are at the origin `(0, 0)`. You can change **at most** `k` characters to any of the four directions.

Find the **maximum** **Manhattan distance** from the origin that can be achieved **at any time** while performing the movements **in order**.

The **Manhattan Distance** between two cells `(x_i, y_i)` and `(x_j, y_j)` is `|x_i - x_j| + |y_i - y_j|`.

## Constraints
- `1 <= s.length <= 10^5`
- `0 <= k <= s.length`
- `s` consists of only `'N'`, `'S'`, `'E'`, and `'W'`.

## Examples
### Example 1
- **Input:** `s = "NWSE", k = 1`
- **Output:** `3`
- **Explanation:** Change `s[2]` from `'S'` to `'N'`. The string `s` becomes `"NWNE"`. 

 
 
 
 Movement 
 Position (x, y) 
 Manhattan Distance 
 Maximum 
 
 
 
 
 s[0] == 'N' 
 (0, 1) 
 0 + 1 = 1 
 1 
 
 
 s[1] == 'W' 
 (-1, 1) 
 1 + 1 = 2 
 2 
 
 
 s[2] == 'N' 
 (-1, 2) 
 1 + 2 = 3 
 3 
 
 
 s[3] == 'E' 
 (0, 2) 
 0 + 2 = 2 
 3 
 
 
 

 The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

### Example 2
- **Input:** `s = "NSWWEW", k = 3`
- **Output:** `6`
- **Explanation:** Change `s[1]` from `'S'` to `'N'`, and `s[4]` from `'E'` to `'W'`. The string `s` becomes `"NNWWWW"`. 

 The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Manhattan Distance After K Changes**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "NWSE", k = 1`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Change `s[2]` from `'S'` to `'N'`. The string `s` becomes `"NWNE"`. 

 
 
 
 Movement 
 Position (x, y) 
 Manhattan Distance 
 Maximum 
 
 
 
 
 s[0] == 'N' 
 (0, 1) 
 0 + 1 = 1 
 1 
 
 
 s[1] == 'W' 
 (-1, 1) 
 1 + 1 = 2 
 2 
 
 
 s[2] == 'N' 
 (-1, 2) 
 1 + 2 = 3 
 3 
 
 
 s[3] == 'E' 
 (0, 2) 
 0 + 2 = 2 
 3 
 
 
 

 The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

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
var maxDistance = function(s, k) {
    let x = 0, y = 0;
    let maxDist = 0;

    for (let i = 0; i < s.length; i++) {
        switch (s[i]) {
            case 'N': y++; break;
            case 'S': y--; break;
            case 'E': x++; break;
            case 'W': x--; break;
        }

        // Maximum achievable distance at this prefix
        let dist = Math.abs(x) + Math.abs(y);
        let possible = Math.min(i + 1, dist + 2 * k);

        maxDist = Math.max(maxDist, possible);
    }

    return maxDist;
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
- [3968. Maximum Manhattan Distance After All Moves](../../4001-4500/4340-maximum-manhattan-distance-after-all-moves/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2229-maximum-fruits-harvested-after-at-most-k-steps/)
- [3962. Maximum Subarray Sum After at Most K Swaps](../../4001-4500/4246-maximum-subarray-sum-after-at-most-k-swaps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/)
