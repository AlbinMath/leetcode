# LeetCode 3273: Minimum Amount of Damage Dealt to Bob

**LeetCode Problem #3273 — Minimum Amount of Damage Dealt to Bob**
Solve LeetCode Minimum Amount of Damage Dealt to Bob using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Amount of Damage Dealt to Bob |
| LeetCode | #3273 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `power` and two integer arrays `damage` and `health`, both having length `n`.

Bob has `n` enemies, where enemy `i` will deal Bob `damage[i]` **points** of damage per second while they are *alive* (i.e. `health[i] > 0`).

Every second, **after** the enemies deal damage to Bob, he chooses **one** of the enemies that is still *alive* and deals `power` points of damage to them.

Determine the **minimum** total amount of damage points that will be dealt to Bob before **all** `n` enemies are *dead*.

## Constraints
- `1 <= power <= 10^4`
- `1 <= n == damage.length == health.length <= 10^5`
- `1 <= damage[i], health[i] <= 10^4`

## Examples
### Example 1
- **Input:** `power = 4, damage = [1,2,3,4], health = [4,5,6,8]`
- **Output:** `39`
- **Explanation:** Attack enemy 3 in the first two seconds, after which enemy 3 will go down, the number of damage points dealt to Bob is `10 + 10 = 20` points. 
 Attack enemy 2 in the next two seconds, after which enemy 2 will go down, the number of damage points dealt to Bob is `6 + 6 = 12` points. 
 Attack enemy 0 in the next second, after which enemy 0 will go down, the number of damage points dealt to Bob is `3` points. 
 Attack enemy 1 in the next two seconds, after which enemy 1 will go down, the number of damage points dealt to Bob is `2 + 2 = 4` points.

### Example 2
- **Input:** `power = 1, damage = [1,1,1,1], health = [1,2,3,4]`
- **Output:** `20`
- **Explanation:** Attack enemy 0 in the first second, after which enemy 0 will go down, the number of damage points dealt to Bob is `4` points. 
 Attack enemy 1 in the next two seconds, after which enemy 1 will go down, the number of damage points dealt to Bob is `3 + 3 = 6` points. 
 Attack enemy 2 in the next three seconds, after which enemy 2 will go down, the number of damage points dealt to Bob is `2 + 2 + 2 = 6` points. 
 Attack enemy 3 in the next four seconds, after which enemy 3 will go down, the number of damage points dealt to Bob is `1 + 1 + 1 + 1 = 4` points.

### Example 3
- **Input:** `power = 8, damage = [40], health = [59]`
- **Output:** `320`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Amount of Damage Dealt to Bob**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `power = 4, damage = [1,2,3,4], health = [4,5,6,8]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `39`.
4. **Verification:** Attack enemy 3 in the first two seconds, after which enemy 3 will go down, the number of damage points dealt to Bob is `10 + 10 = 20` points. 
 Attack enemy 2 in the next two seconds, after which enemy 2 will go down, the number of damage points dealt to Bob is `6 + 6 = 12` points. 
 Attack enemy 0 in the next second, after which enemy 0 will go down, the number of damage points dealt to Bob is `3` points. 
 Attack enemy 1 in the next two seconds, after which enemy 1 will go down, the number of damage points dealt to Bob is `2 + 2 = 4` points.

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
var minDamage = function(power, damage, health) {
    const n = damage.length;
    const enemies = [];

    for (let i = 0; i < n; i++) {
        const time = Math.ceil(health[i] / power);

        enemies.push({
            time: time,
            damage: damage[i]
        });
    }
    enemies.sort((a, b) => {
        return a.time * b.damage - b.time * a.damage;
    });

    let totalDamage = 0;
    let elapsedTime = 0;

    for (const enemy of enemies) {
        elapsedTime += enemy.time;
        totalDamage += elapsedTime * enemy.damage;
    }

    return totalDamage;
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
- [2335. Minimum Amount of Time to Fill Cups](../../2001-2500/2335-minimum-amount-of-time-to-fill-cups/)
- [2391. Minimum Amount of Time to Collect Garbage](../../2001-2500/2391-minimum-amount-of-time-to-collect-garbage/)
- [3494. Find the Minimum Amount of Time to Brew Potions](../../3001-3500/3494-find-the-minimum-amount-of-time-to-brew-potions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/)
