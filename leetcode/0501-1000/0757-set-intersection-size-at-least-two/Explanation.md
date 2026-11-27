# LeetCode 757: Set Intersection Size At Least Two

**LeetCode Problem #757 — Set Intersection Size At Least Two**
Solve LeetCode Set Intersection Size At Least Two using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Set Intersection Size At Least Two |
| LeetCode | #757 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `intervals` where `intervals[i] = [start_i, end_i]` represents all the integers from `start_i` to `end_i` inclusively.

A **containing set** is an array `nums` where each interval from `intervals` has **at least two** integers in `nums`.

For example, if `intervals = [[1,3], [3,7], [8,9]]`, then `[1,2,4,7,8,9]` and `[2,3,4,8,9]` are **containing sets**.

Return *the minimum possible size of a containing set*.

## Constraints
- `1 <= intervals.length <= 3000`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^8`

## Examples
### Example 1
- **Input:** `intervals = [[1,3],[3,7],[8,9]]`
- **Output:** `5`
- **Explanation:** let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.

### Example 2
- **Input:** `intervals = [[1,3],[1,4],[2,5],[3,5]]`
- **Output:** `3`
- **Explanation:** let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.

### Example 3
- **Input:** `intervals = [[1,2],[2,3],[2,4],[4,5]]`
- **Output:** `5`
- **Explanation:** let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Set Intersection Size At Least Two**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `intervals = [[1,3],[3,7],[8,9]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.

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
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        a, b = -1, -1  # two largest chosen points, a < b
        ans = 0
        for s, e in intervals:
            if s > b:
                # neither point is inside
                ans += 2
                a, b = e - 1, e
            elif s > a:
                # only b is inside
                ans += 1
                if b == e:
                    a, b = e - 1, e
                else:
                    a, b = b, e
        return ans
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
- [3002. Maximum Size of a Set After Removals](../../3001-3500/3002-maximum-size-of-a-set-after-removals/)
- [160. Intersection of Two Linked Lists](../../0001-0500/0160-intersection-of-two-linked-lists/)
- [349. Intersection of Two Arrays](../../0001-0500/0349-intersection-of-two-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/set-intersection-size-at-least-two/)
