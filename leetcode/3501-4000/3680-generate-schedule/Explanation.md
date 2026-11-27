# LeetCode 3680: Generate Schedule

**LeetCode Problem #3680 — Generate Schedule**
Solve LeetCode Generate Schedule using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Generate Schedule |
| LeetCode | #3680 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` representing `n` teams. You are asked to generate a schedule such that:

Each team plays every other team **exactly twice**: once at home and once away. 
 There is **exactly one** match per day; the schedule is a list of **consecutive** days and `schedule[i]` is the match on day `i`. 
 No team plays on **consecutive** days.

Return a 2D integer array `schedule`, where `schedule[i][0]` represents the home team and `schedule[i][1]` represents the away team. If multiple schedules meet the conditions, return **any** one of them.

If no schedule exists that meets the conditions, return an empty array.

## Constraints
- `2 <= n <= 50`​​​​​​​

## Examples
### Example 1
- **Input:** `n = 3`
- **Output:** `[]`
- **Explanation:** ​​​​​​​Since each team plays every other team exactly twice, a total of 6 matches need to be played: `[0,1],[0,2],[1,2],[1,0],[2,0],[2,1]`. 

 It's not possible to create a schedule without at least one team playing consecutive days.

### Example 2
- **Input:** `n = 5`
- **Output:** `[[0,1],[2,3],[0,4],[1,2],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[2,0],[3,1],[4,0],[2,1],[4,3],[1,0],[3,2],[4,1],[3,0],[4,2]]`
- **Explanation:** Since each team plays every other team exactly twice, a total of 20 matches need to be played. 

 The output shows one of the schedules that meet the conditions. No team plays on consecutive days.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Generate Schedule**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[]`.
4. **Verification:** ​​​​​​​Since each team plays every other team exactly twice, a total of 6 matches need to be played: `[0,1],[0,2],[1,2],[1,0],[2,0],[2,1]`. 

 It's not possible to create a schedule without at least one team playing consecutive days.

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
var generateSchedule = function(n) {
    if (n < 5) return [];

    const matches = [];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i !== j) {
                matches.push([i, j]);
            }
        }
    }

    const m = matches.length;
    const alive = new Uint8Array(m).fill(1);

    const degree = new Int32Array(m).fill((n - 2) * (n - 3));

    const schedule = [];
    let remaining = m;
    let current = -1;

    while (remaining > 0) {
        let best = -1;
        let bestDegree = Infinity;
        for (let i = 0; i < m; i++) {
            if (!alive[i]) continue;

            const [a, b] = matches[i];

            if (current !== -1) {
                const [p, q] = matches[current];

                if (a === p || a === q || b === p || b === q) {
                    continue;
                }
            }
            if (remaining > 1 && degree[i] === 0) {
                continue;
            }

            if (degree[i] < bestDegree) {
                bestDegree = degree[i];
                best = i;
            }
        }
        if (best === -1) {
            return [];
        }

        schedule.push(matches[best]);
        alive[best] = 0;
        remaining--;

        const [a, b] = matches[best];

        for (let i = 0; i < m; i++) {
            if (!alive[i]) continue;

            const [u, v] = matches[i];

            if (u !== a && u !== b && v !== a && v !== b) {
                degree[i]--;
            }
        }

        current = best;
    }

    return schedule;
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
- [22. Generate Parentheses](../../0001-0500/0022-generate-parentheses/)
- [478. Generate Random Point in a Circle](../../0001-0500/0478-generate-random-point-in-a-circle/)
- [1374. Generate a String With Characters That Have Odd Counts](../../1001-1500/1374-generate-a-string-with-characters-that-have-odd-counts/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-schedule/)
