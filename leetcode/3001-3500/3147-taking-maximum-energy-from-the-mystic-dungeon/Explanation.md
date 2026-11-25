# LeetCode 3147: Taking Maximum Energy From the Mystic Dungeon

**LeetCode Problem #3147 — Taking Maximum Energy From the Mystic Dungeon**
Solve LeetCode Taking Maximum Energy From the Mystic Dungeon using JavaScript and Greedy. This solution finds the optimal result using Greedy Choice Strategy in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Taking Maximum Energy From the Mystic Dungeon |
| LeetCode | #3147 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Greedy Choice Strategy |
| Data Structure | Array / Priority Queue |
| Pattern | Greedy |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
In a mystic dungeon, `n` magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician `i`, you will be instantly transported to magician `(i + k)`. This process will be repeated until you reach the magician where `(i + k)` does not exist.

In other words, you will choose a starting point and then teleport with `k` jumps until you reach the end of the magicians' sequence, **absorbing all the energy** during the journey.

You are given an array `energy` and an integer `k`. Return the **maximum** possible energy you can gain.

**Note** that when you reach a magician, you *must* take energy from them, whether it is negative or positive energy.

## Constraints
- `1 <= energy.length <= 10^5`
- `-1000 <= energy[i] <= 1000`
- `1 <= k <= energy.length - 1`

## Examples
### Example 1
- **Input:** `energy = [5,2,-10,-5,1], k = 3`
- **Output:** `3`
- **Explanation:** We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

### Example 2
- **Input:** `energy = [-2,-3,-1], k = 2`
- **Output:** `-1`
- **Explanation:** We can gain a total energy of -1 by starting from magician 2.

## Key Insight
Leverage **Greedy** with **Array / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Taking Maximum Energy From the Mystic Dungeon**, we observe the problem requirements and utilize the **Greedy** technique. We iterate through the inputs using **Greedy Choice Strategy**, leveraging a **Array / Priority Queue** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array / Priority Queue**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `energy = [5,2,-10,-5,1], k = 3`.
2. **Processing Steps:** We apply **Greedy Choice Strategy** using our **Array / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Priority Queue.

## Pattern
**Greedy**

## Topics
- Greedy
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maximumEnergy = function(energy, k) {
    const n = energy.length;

    let ans = -Infinity;

    for (let i = n - 1; i >= 0; i--) {

        if (i + k < n) {
            energy[i] += energy[i + k];
        }

        ans = Math.max(ans, energy[i]);
    }

    return ans;
};
```

## Why This Works
By utilizing **Greedy**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)
- [1349. Maximum Students Taking Exam](../../1001-1500/1349-maximum-students-taking-exam/)
- [1423. Maximum Points You Can Obtain from Cards](../../1001-1500/1423-maximum-points-you-can-obtain-from-cards/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/)
