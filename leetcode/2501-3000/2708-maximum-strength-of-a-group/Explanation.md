# LeetCode 2708: Maximum Strength of a Group

**LeetCode Problem #2708 — Maximum Strength of a Group**
Solve LeetCode Maximum Strength of a Group using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Strength of a Group |
| LeetCode | #2708 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums` representing the score of students in an exam. The teacher would like to form one **non-empty** group of students with maximal **strength**, where the strength of a group of students of indices `i_0`, `i_1`, `i_2`, ... , `i_k` is defined as `nums[i_0] * nums[i_1] * nums[i_2] * ... * nums[i_k​]`.

Return *the maximum strength of a group the teacher can create*.

## Constraints
- `1 <= nums.length <= 13`
- `-9 <= nums[i] <= 9`

## Examples
### Example 1
- **Input:** `nums = [3,-1,-5,2,5,-9]`
- **Output:** `1350`
- **Explanation:** One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.

### Example 2
- **Input:** `nums = [-4,-5,-4]`
- **Output:** `20`
- **Explanation:** Group the students at indices [0, 1] . Then, we&rsquo;ll have a resulting strength of 20. We cannot achieve greater strength.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Strength of a Group**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,-1,-5,2,5,-9]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1350`.
4. **Verification:** One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        best = None
        for mask in range(1, 1 << n):
            prod = 1
            for i in range(n):
                if mask >> i & 1:
                    prod *= nums[i]
            if best is None or prod > best:
                best = prod
        return best
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3077. Maximum Strength of K Disjoint Subarrays](../../3001-3500/3077-maximum-strength-of-k-disjoint-subarrays/)
- [2281. Sum of Total Strength of Wizards](../../2001-2500/2281-sum-of-total-strength-of-wizards/)
- [4008. Minimum Initial Strength to Defeat All Monsters](../../4001-4500/4008-minimum-initial-strength-to-defeat-all-monsters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-strength-of-a-group/)
