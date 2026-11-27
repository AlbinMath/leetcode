# LeetCode 3207: Maximum Points After Enemy Battles

**LeetCode Problem #3207 — Maximum Points After Enemy Battles**
Solve LeetCode Maximum Points After Enemy Battles using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Points After Enemy Battles |
| LeetCode | #3207 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `enemyEnergies` denoting the energy values of various enemies.

You are also given an integer `currentEnergy` denoting the amount of energy you have initially.

You start with 0 points, and all the enemies are unmarked initially.

You can perform **either** of the following operations **zero **or multiple times to gain points:

Choose an **unmarked** enemy, `i`, such that `currentEnergy >= enemyEnergies[i]`. By choosing this option:

You gain 1 point. 
 Your energy is reduced by the enemy's energy, i.e. `currentEnergy = currentEnergy - enemyEnergies[i]`. 
 
 
 If you have **at least** 1 point, you can choose an **unmarked** enemy, `i`. By choosing this option:
 
 Your energy increases by the enemy's energy, i.e. `currentEnergy = currentEnergy + enemyEnergies[i]`. 
 The e nemy `i` is **marked**.

Return an integer denoting the **maximum** points you can get in the end by optimally performing operations.

## Constraints
- `1 <= enemyEnergies.length <= 10^5`
- `1 <= enemyEnergies[i] <= 10^9`
- `0 <= currentEnergy <= 10^9`

## Examples
### Example 1
- **Input:** `enemyEnergies = [3,2,2], currentEnergy = 2`
- **Output:** `3`
- **Explanation:** The following operations can be performed to get 3 points, which is the maximum: 

 
 First operation on enemy 1: `points` increases by 1, and `currentEnergy` decreases by 2. So, `points = 1`, and `currentEnergy = 0`. 
 Second operation on enemy 0: `currentEnergy` increases by 3, and enemy 0 is marked. So, `points = 1`, `currentEnergy = 3`, and marked enemies = `[0]`. 
 First operation on enemy 2: `points` increases by 1, and `currentEnergy` decreases by 2. So, `points = 2`, `currentEnergy = 1`, and marked enemies = `[0]`. 
 Second operation on enemy 2: `currentEnergy` increases by 2, and enemy 2 is marked. So, `points = 2`, `currentEnergy = 3`, and marked enemies = `[0, 2]`. 
 First operation on enemy 1: `points` increases by 1, and `currentEnergy` decreases by 2. So, `points = 3`, `currentEnergy = 1`, and marked enemies = `[0, 2]`.

### Example 2
- **Input:** `enemyEnergies = [2] , currentEnergy = 10`
- **Output:** `5`
- **Explanation:** Performing the first operation 5 times on enemy 0 results in the maximum number of points.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Points After Enemy Battles**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `enemyEnergies = [3,2,2], currentEnergy = 2`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The following operations can be performed to get 3 points, which is the maximum: 

 
 First operation on enemy 1: `points` increases by 1, and `currentEnergy` decreases by 2. So, `points = 1`, and `currentEnergy = 0`. 
 Second operation on enemy 0: `currentEnergy` increases by 3, and enemy 0 is marked. So, `points = 1`, `currentEnergy = 3`, and marked enemies = `[0]`. 
 First operation on enemy 2: `points` increases by 1, and `currentEnergy` decreases by 2. So, `points = 2`, `currentEnergy = 1`, and marked enemies = `[0]`. 
 Second operation on enemy 2: `currentEnergy` increases by 2, and enemy 2 is marked. So, `points = 2`, `currentEnergy = 3`, and marked enemies = `[0, 2]`. 
 First operation on enemy 1: `points` increases by 1, and `currentEnergy` decreases by 2. So, `points = 3`, `currentEnergy = 1`, and marked enemies = `[0, 2]`.

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
var maximumPoints = function(enemyEnergies, currentEnergy) {
    const minEnergy = Math.min(...enemyEnergies);

    if (currentEnergy < minEnergy) {
        return 0;
    }

    let totalEnergy = currentEnergy;

    let skippedMin = false;

    for (const energy of enemyEnergies) {
        if (energy === minEnergy && !skippedMin) {
            skippedMin = true;
            continue;
        }

        totalEnergy += energy;
    }

    return Math.floor(totalEnergy / minEnergy);
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
- [2920. Maximum Points After Collecting Coins From All Nodes](../../2501-3000/2920-maximum-points-after-collecting-coins-from-all-nodes/)
- [1422. Maximum Score After Splitting a String](../../1001-1500/1422-maximum-score-after-splitting-a-string/)
- [1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts](../../1001-1500/1465-maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-points-after-enemy-battles/)
