# LeetCode 1936: Add Minimum Number of Rungs

**LeetCode Problem #1936 — Add Minimum Number of Rungs**
Solve LeetCode Add Minimum Number of Rungs using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Add Minimum Number of Rungs |
| LeetCode | #1936 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **strictly increasing** integer array `rungs` that represents the **height** of rungs on a ladder. You are currently on the **floor** at height `0`, and you want to reach the last rung.

You are also given an integer `dist`. You can only climb to the next highest rung if the distance between where you are currently at (the floor or on a rung) and the next rung is **at most** `dist`. You are able to insert rungs at any positive **integer** height if a rung is not already there.

Return *the **minimum** number of rungs that must be added to the ladder in order for you to climb to the last rung.*

## Constraints
- `1 <= rungs.length <= 10^5`
- `1 <= rungs[i] <= 10^9`
- `1 <= dist <= 10^9`
- `rungs` is **strictly increasing**.

## Examples
### Example 1
- **Input:** `rungs = [1,3,5,10], dist = 2`
- **Output:** `2`
- **Explanation:** You currently cannot reach the last rung.
Add rungs at heights 7 and 8 to climb this ladder. 
The ladder will now have rungs at [1,3,5, 7 , 8 ,10].

### Example 2
- **Input:** `rungs = [3,6,8,10], dist = 3`
- **Output:** `0`
- **Explanation:** This ladder can be climbed without adding additional rungs.

### Example 3
- **Input:** `rungs = [3,4,6,7], dist = 2`
- **Output:** `1`
- **Explanation:** You currently cannot reach the first rung from the ground.
Add a rung at height 1 to climb this ladder.
The ladder will now have rungs at [ 1 ,3,4,6,7].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Add Minimum Number of Rungs**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rungs = [1,3,5,10], dist = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** You currently cannot reach the last rung.
Add rungs at heights 7 and 8 to climb this ladder. 
The ladder will now have rungs at [1,3,5, 7 , 8 ,10].

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
from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        prev = 0
        added = 0
        for r in rungs:
            added += (r - prev - 1) // dist
            prev = r
        return added
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
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [871. Minimum Number of Refueling Stops](../../0501-1000/0871-minimum-number-of-refueling-stops/)
- [921. Minimum Add to Make Parentheses Valid](../../0501-1000/0921-minimum-add-to-make-parentheses-valid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/add-minimum-number-of-rungs/)
