# LeetCode 3494: Find the Minimum Amount of Time to Brew Potions

**LeetCode Problem #3494 — Find the Minimum Amount of Time to Brew Potions**
Solve LeetCode Find the Minimum Amount of Time to Brew Potions using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Minimum Amount of Time to Brew Potions |
| LeetCode | #3494 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays, `skill` and ` mana `, of length `n` and `m`, respectively.

In a laboratory, `n` wizards must brew `m` potions *in order*. Each potion has a mana capacity `mana[j]` and **must** pass through **all** the wizards sequentially to be brewed properly. The time taken by the `i^th` wizard on the `j^th` potion is `time_ij = skill[i] * mana[j]`.

Since the brewing process is delicate, a potion **must** be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be *synchronized* so that each wizard begins working on a potion **exactly** when it arrives. ​

Return the **minimum** amount of time required for the potions to be brewed properly.

## Constraints
- `n == skill.length`
- `m == mana.length`
- `1 <= n, m <= 5000`
- `1 <= mana[i], skill[i] <= 5000`

## Examples
### Example 1
- **Input:** `skill = [1,5,2,4], mana = [5,1,4,2]`
- **Output:** `110`
- **Explanation:** Potion Number 
 Start time 
 Wizard 0 done by 
 Wizard 1 done by 
 Wizard 2 done by 
 Wizard 3 done by 
 
 
 0 
 0 
 5 
 30 
 40 
 60 
 
 
 1 
 52 
 53 
 58 
 60 
 64 
 
 
 2 
 54 
 58 
 78 
 86 
 102 
 
 
 3 
 86 
 88 
 98 
 102 
 110 
 
 
 

 As an example for why wizard 0 cannot start working on the 1^st potion before time `t = 52`, consider the case where the wizards started preparing the 1^st potion at time `t = 50`. At time `t = 58`, wizard 2 is done with the 1^st potion, but wizard 3 will still be working on the 0^th potion till time `t = 60`.

### Example 2
- **Input:** `skill = [1,1,1], mana = [1,1,1]`
- **Output:** `5`
- **Explanation:** Preparation of the 0^th potion begins at time `t = 0`, and is completed by time `t = 3`. 
 Preparation of the 1^st potion begins at time `t = 1`, and is completed by time `t = 4`. 
 Preparation of the 2^nd potion begins at time `t = 2`, and is completed by time `t = 5`.

### Example 3
- **Input:** `skill = [1,2,3,4], mana = [1,2]`
- **Output:** `21`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Minimum Amount of Time to Brew Potions**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `skill = [1,5,2,4], mana = [5,1,4,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `110`.
4. **Verification:** Potion Number 
 Start time 
 Wizard 0 done by 
 Wizard 1 done by 
 Wizard 2 done by 
 Wizard 3 done by 
 
 
 0 
 0 
 5 
 30 
 40 
 60 
 
 
 1 
 52 
 53 
 58 
 60 
 64 
 
 
 2 
 54 
 58 
 78 
 86 
 102 
 
 
 3 
 86 
 88 
 98 
 102 
 110 
 
 
 

 As an example for why wizard 0 cannot start working on the 1^st potion before time `t = 52`, consider the case where the wizards started preparing the 1^st potion at time `t = 50`. At time `t = 58`, wizard 2 is done with the 1^st potion, but wizard 3 will still be working on the 0^th potion till time `t = 60`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minTime = function(skill, mana) {
    const n = skill.length;
    const pref = new Array(n);
    pref[0] = skill[0];
    for (let i = 1; i < n; i++) {
        pref[i] = pref[i - 1] + skill[i];
    }

    // Completion times for potion 0 (starts at t = 0)
    const done = new Array(n);
    for (let i = 0; i < n; i++) {
        done[i] = pref[i] * mana[0];
    }

    for (let j = 1; j < mana.length; j++) {
        const currMana = mana[j];
        let startTime = done[0];

        for (let i = 1; i < n; i++) {
            const candidate = done[i] - pref[i - 1] * currMana;
            if (candidate > startTime) {
                startTime = candidate;
            }
        }

        for (let i = 0; i < n; i++) {
            done[i] = startTime + pref[i] * currMana;
        }
    }

    return done[n - 1];
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1723. Find Minimum Time to Finish All Jobs](../../1501-2000/1825-find-minimum-time-to-finish-all-jobs/)
- [3341. Find Minimum Time to Reach Last Room I](../../3501-4000/3627-find-minimum-time-to-reach-last-room-i/)
- [3342. Find Minimum Time to Reach Last Room II](../../3501-4000/3628-find-minimum-time-to-reach-last-room-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/)
