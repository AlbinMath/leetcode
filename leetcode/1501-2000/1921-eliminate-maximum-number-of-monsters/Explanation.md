# LeetCode 1921: Eliminate Maximum Number of Monsters

**LeetCode Problem #1921 — Eliminate Maximum Number of Monsters**
Solve LeetCode Eliminate Maximum Number of Monsters using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Eliminate Maximum Number of Monsters |
| LeetCode | #1921 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are playing a video game where you are defending your city from a group of `n` monsters. You are given a **0-indexed** integer array `dist` of size `n`, where `dist[i]` is the **initial distance** in kilometers of the `i^th` monster from the city.

The monsters walk toward the city at a **constant** speed. The speed of each monster is given to you in an integer array `speed` of size `n`, where `speed[i]` is the speed of the `i^th` monster in kilometers per minute.

You have a weapon that, once fully charged, can eliminate a **single** monster. However, the weapon takes **one minute** to charge. The weapon is fully charged at the very start.

You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a **loss**, and the game ends before you can use your weapon.

Return *the **maximum** number of monsters that you can eliminate before you lose, or *`n`* if you can eliminate all the monsters before they reach the city.*

## Constraints
- `n == dist.length == speed.length`
- `1 <= n <= 10^5`
- `1 <= dist[i], speed[i] <= 10^5`

## Examples
### Example 1
- **Input:** `dist = [1,3,4], speed = [1,1,1]`
- **Output:** `3`
- **Explanation:** In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
After a minute, the distances of the monsters are [X,X,2]. You eliminate the third monster.
All 3 monsters can be eliminated.

### Example 2
- **Input:** `dist = [1,1,2,3], speed = [1,1,1,1]`
- **Output:** `1`
- **Explanation:** In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,0,1,2], so you lose.
You can only eliminate 1 monster.

### Example 3
- **Input:** `dist = [3,2,4], speed = [5,3,2]`
- **Output:** `1`
- **Explanation:** In the beginning, the distances of the monsters are [3,2,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,0,2], so you lose.
You can only eliminate 1 monster.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Eliminate Maximum Number of Monsters**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `dist = [1,3,4], speed = [1,1,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
After a minute, the distances of the monsters are [X,X,2]. You eliminate the third monster.
All 3 monsters can be eliminated.

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
var eliminateMaximum = function(dist, speed) {
    const n = dist.length;
    const arrivalTimes = [];
    for (let i = 0; i < n; i++) {
        arrivalTimes.push(Math.ceil(dist[i] / speed[i]));
    }
    arrivalTimes.sort((a, b) => a - b);
    for (let i = 0; i < n; i++) {
        if (arrivalTimes[i] <= i) {
            return i;
        }
    }
    return n;
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
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)
- [414. Third Maximum Number](../../0001-0500/0414-third-maximum-number/)
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1072-flip-columns-for-maximum-number-of-equal-rows/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/)
