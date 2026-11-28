# LeetCode 3951: Minimum Energy to Maintain Brightness

**LeetCode Problem #3951 — Minimum Energy to Maintain Brightness**
Solve LeetCode Minimum Energy to Maintain Brightness using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Energy to Maintain Brightness |
| LeetCode | #3951 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n`, representing `n` light bulbs arranged in a line and indexed from 0 to `n - 1`.

You are also given an integer `brightness` and a 2D integer array `intervals`, where `intervals[i] = [start_i, end_i]` represents an **inclusive** time interval during which the lighting requirement **must** be satisfied.

At each time unit, every bulb can independently be either on or off. A bulb that is on **illuminates** its own position and its **adjacent** positions, if they exist.

The **total illumination** at a time unit is the number of **illuminated** positions. Each position is counted **at most once**.

For every integer time unit covered by **at least** one interval in `intervals`, the **total illumination** must be **at least** `brightness`. At time units not covered by any interval, all bulbs may remain off. Each bulb that is on consumes 1 unit of energy for that time unit.

Return an integer denoting the **minimum** total energy required.

## Constraints
- `1 <= n <= 10^6`
- `1 <= brightness <= n`
- `1 <= intervals.length <= 10^5`
- `intervals[i] == [start_i, end_i]`
- `0 <= start_i <= end_i <= 10^9`

## Examples
### Example 1
- **Input:** `n = 5, brightness = 5, intervals = [[6,12]]`
- **Output:** `14`
- **Explanation:** Turn on the light bulbs at positions 1 and 4. 
 Current state of line: `0 1 0 0 1`. 
 All 5 positions are illuminated, so the required brightness is reached. 
 The active interval has length `12 - 6 + 1 = 7`, so the total energy is `2 * 7 = 14`.

### Example 2
- **Input:** `n = 2, brightness = 1, intervals = [[0,0],[2,2]]`
- **Output:** `2`
- **Explanation:** Turn on one light bulb during each active interval. 
 Each interval has length 1, so the total active time is `1 + 1 = 2`. 
 The total energy is `1 * 2 = 2`.

### Example 3
- **Input:** `n = 4, brightness = 2, intervals = [[1,3],[2,4]]`
- **Output:** `4`
- **Explanation:** Turn on one light bulb. It can illuminate at least 2 positions. 
 The active intervals overlap, so the total active time is the length of `[1,4]`, which is 4. 
 The total energy is `1 * 4 = 4`.

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Energy to Maintain Brightness**, we observe the problem requirements and utilize the **Greedy** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, brightness = 5, intervals = [[6,12]]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** Turn on the light bulbs at positions 1 and 4. 
 Current state of line: `0 1 0 0 1`. 
 All 5 positions are illuminated, so the required brightness is reached. 
 The active interval has length `12 - 6 + 1 = 7`, so the total energy is `2 * 7 = 14`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minEnergy = function(n, brightness, intervals) {
    const bulbsNeeded = Math.ceil(brightness / 3);

    intervals.sort((a, b) => a[0] - b[0]);

    let totalTime = 0;

    let start = intervals[0][0];
    let end = intervals[0][1];

    for (let i = 1; i < intervals.length; i++) {
        const [nextStart, nextEnd] = intervals[i];

        if (nextStart <= end + 1) {
            end = Math.max(end, nextEnd);
        } else {
            totalTime += end - start + 1;

            start = nextStart;
            end = nextEnd;
        }
    }

    totalTime += end - start + 1;

    return totalTime * bulbsNeeded;
};
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1665. Minimum Initial Energy to Finish Tasks](../../1501-2000/1665-minimum-initial-energy-to-finish-tasks/)
- [3147. Taking Maximum Energy From the Mystic Dungeon](../../3001-3500/3147-taking-maximum-energy-from-the-mystic-dungeon/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-energy-to-maintain-brightness/)
