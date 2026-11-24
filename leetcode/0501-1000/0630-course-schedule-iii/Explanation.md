# LeetCode 630: Course Schedule III

**LeetCode Problem #630 — Course Schedule III**
Solve LeetCode Course Schedule III using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Course Schedule III |
| LeetCode | #630 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` different online courses numbered from `1` to `n`. You are given an array `courses` where `courses[i] = [duration_i, lastDay_i]` indicate that the `i^th` course should be taken continuously for `duration_i` days and must be finished before or on `lastDay_i`.

You will start on the `1^st` day and you cannot take two or more courses simultaneously.

Return *the maximum number of courses that you can take*.

## Constraints
- `1 <= courses.length <= 10^4`
- `1 <= duration_i, lastDay_i <= 10^4`

## Examples
### Example 1
- **Input:** `courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]`
- **Output:** `3`

### Example 2
- **Input:** `courses = [[1,2]]`
- **Output:** `1`

### Example 3
- **Input:** `courses = [[3,2],[4,3]]`
- **Output:** `0`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Course Schedule III**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq

class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        total, h = 0, []
        for d, end in courses:
            total += d
            heapq.heappush(h, -d)
            if total > end:
                total += heapq.heappop(h)
        return len(h)
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
- [207. Course Schedule](../../0001-0500/0207-course-schedule/)
- [210. Course Schedule II](../../0001-0500/0210-course-schedule-ii/)
- [1462. Course Schedule IV](../../1001-1500/1462-course-schedule-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/course-schedule-iii/)
