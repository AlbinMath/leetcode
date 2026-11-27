# LeetCode 3169: Count Days Without Meetings

**LeetCode Problem #3169 — Count Days Without Meetings**
Solve LeetCode Count Days Without Meetings using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Days Without Meetings |
| LeetCode | #3169 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `days` representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array `meetings` of size `n` where, `meetings[i] = [start_i, end_i]` represents the starting and ending days of meeting `i` (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

**Note: **The meetings may overlap.

## Constraints
- `1 <= days <= 10^9`
- `1 <= meetings.length <= 10^5`
- `meetings[i].length == 2`
- ` 1 <= meetings[i][0] <= meetings[i][1] <= days `

## Examples
### Example 1
- **Input:** `days = 10, meetings = [[5,7],[1,3],[9,10]]`
- **Output:** `2`
- **Explanation:** There is no meeting scheduled on the 4^th and 8^th days.

### Example 2
- **Input:** `days = 5, meetings = [[2,4],[1,3]]`
- **Output:** `1`
- **Explanation:** There is no meeting scheduled on the 5^th day.

### Example 3
- **Input:** `days = 6, meetings = [[1,6]]`
- **Output:** `0`
- **Explanation:** Meetings are scheduled for all working days.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Days Without Meetings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `days = 10, meetings = [[5,7],[1,3],[9,10]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There is no meeting scheduled on the 4^th and 8^th days.

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
var countDays = function(days, meetings) {
    meetings.sort((a, b) => a[0] - b[0]);

    let lastDay = 0;
    let freeDays = 0;

    for (const [start, end] of meetings) {

        if (start > lastDay + 1) {
            freeDays += start - lastDay - 1;
        }

        lastDay = Math.max(lastDay, end);
    }

    freeDays += days - lastDay;

    return freeDays;
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
- [2409. Count Days Spent Together](../../2001-2500/2409-count-days-spent-together/)
- [957. Prison Cells After N Days](../../0501-1000/0957-prison-cells-after-n-days/)
- [1011. Capacity To Ship Packages Within D Days](../../1001-1500/1011-capacity-to-ship-packages-within-d-days/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-days-without-meetings/)
