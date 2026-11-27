# LeetCode 1953: Maximum Number of Weeks for Which You Can Work

**LeetCode Problem #1953 — Maximum Number of Weeks for Which You Can Work**
Solve LeetCode Maximum Number of Weeks for Which You Can Work using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Weeks for Which You Can Work |
| LeetCode | #1953 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` projects numbered from `0` to `n - 1`. You are given an integer array `milestones` where each `milestones[i]` denotes the number of milestones the `i^th` project has.

You can work on the projects following these two rules:

Every week, you will finish **exactly one** milestone of **one** project. You **must** work every week. 
 You **cannot** work on two milestones from the same project for two **consecutive** weeks.

Once all the milestones of all the projects are finished, or if the only milestones that you can work on will cause you to violate the above rules, you will **stop working**. Note that you may not be able to finish every project's milestones due to these constraints.

Return *the **maximum** number of weeks you would be able to work on the projects without violating the rules mentioned above*.

## Constraints
- `n == milestones.length`
- `1 <= n <= 10^5`
- `1 <= milestones[i] <= 10^9`

## Examples
### Example 1
- **Input:** `milestones = [1,2,3]`
- **Output:** `6`
- **Explanation:** One possible scenario is:
​​​​- During the 1^st week, you will work on a milestone of project 0.
- During the 2^nd week, you will work on a milestone of project 2.
- During the 3^rd week, you will work on a milestone of project 1.
- During the 4^th week, you will work on a milestone of project 2.
- During the 5^th week, you will work on a milestone of project 1.
- During the 6^th week, you will work on a milestone of project 2.
The total number of weeks is 6.

### Example 2
- **Input:** `milestones = [5,2,1]`
- **Output:** `7`
- **Explanation:** One possible scenario is:
- During the 1^st week, you will work on a milestone of project 0.
- During the 2^nd week, you will work on a milestone of project 1.
- During the 3^rd week, you will work on a milestone of project 0.
- During the 4^th week, you will work on a milestone of project 1.
- During the 5^th week, you will work on a milestone of project 0.
- During the 6^th week, you will work on a milestone of project 2.
- During the 7^th week, you will work on a milestone of project 0.
The total number of weeks is 7.
Note that you cannot work on the last milestone of project 0 on 8^th week because it would violate the rules.
Thus, one milestone in project 0 will remain unfinished.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Weeks for Which You Can Work**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `milestones = [1,2,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** One possible scenario is:
​​​​- During the 1^st week, you will work on a milestone of project 0.
- During the 2^nd week, you will work on a milestone of project 2.
- During the 3^rd week, you will work on a milestone of project 1.
- During the 4^th week, you will work on a milestone of project 2.
- During the 5^th week, you will work on a milestone of project 1.
- During the 6^th week, you will work on a milestone of project 2.
The total number of weeks is 6.

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
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        mx = max(milestones)
        rest = total - mx
        if mx > rest + 1:
            return 2 * rest + 1
        return total
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
- [1561. Maximum Number of Coins You Can Get](../../1501-2000/1561-maximum-number-of-coins-you-can-get/)
- [1798. Maximum Number of Consecutive Values You Can Make](../../1501-2000/1798-maximum-number-of-consecutive-values-you-can-make/)
- [1935. Maximum Number of Words You Can Type](../../1501-2000/1935-maximum-number-of-words-you-can-type/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/)
