# LeetCode 2860: Happy Students

**LeetCode Problem #2860 — Happy Students**
Solve LeetCode Happy Students using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Happy Students |
| LeetCode | #2860 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` of length `n` where `n` is the total number of students in the class. The class teacher tries to select a group of students so that all the students remain happy.

The `i^th` student will become happy if one of these two conditions is met:

The student is selected and the total number of selected students is** strictly greater than** `nums[i]`. 
 The student is not selected and the total number of selected students is **strictly** **less than** `nums[i]`.

Return *the number of ways to select a group of students so that everyone remains happy.*

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] < nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,1]`
- **Output:** `2`
- **Explanation:** The two possible ways are:
The class teacher selects no student.
The class teacher selects both students to form the group. 
If the class teacher selects just one student to form a group then the both students will not be happy. Therefore, there are only two possible ways.

### Example 2
- **Input:** `nums = [6,0,3,3,6,7,2,7]`
- **Output:** `3`
- **Explanation:** The three possible ways are:
The class teacher selects the student with index = 1 to form the group.
The class teacher selects the students with index = 1, 2, 3, 6 to form the group.
The class teacher selects all the students to form the group.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Happy Students**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The two possible ways are:
The class teacher selects no student.
The class teacher selects both students to form the group. 
If the class teacher selects just one student to form a group then the both students will not be happy. Therefore, there are only two possible ways.

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
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for k in range(n + 1):
            if k > 0 and nums[k - 1] >= k:
                continue
            if k < n and nums[k] <= k:
                continue
            ans += 1
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
- [202. Happy Number](../../0001-0500/0202-happy-number/)
- [1392. Longest Happy Prefix](../../1501-2000/1508-longest-happy-prefix/)
- [1405. Longest Happy String](../../1001-1500/1304-longest-happy-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/happy-students/)
