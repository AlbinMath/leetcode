# LeetCode 2244: Minimum Rounds to Complete All Tasks

**LeetCode Problem #2244 — Minimum Rounds to Complete All Tasks**
Solve LeetCode Minimum Rounds to Complete All Tasks using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Rounds to Complete All Tasks |
| LeetCode | #2244 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `tasks`, where `tasks[i]` represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the **same difficulty level**.

Return *the **minimum** rounds required to complete all the tasks, or *`-1`* if it is not possible to complete all the tasks.*

## Constraints
- `1 <= tasks.length <= 10^5`
- `1 <= tasks[i] <= 10^9`

## Examples
### Example 1
- **Input:** `tasks = [2,2,3,3,2,4,4,4,4,4]`
- **Output:** `4`
- **Explanation:** To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4. 
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.

### Example 2
- **Input:** `tasks = [2,3,3]`
- **Output:** `-1`
- **Explanation:** There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Rounds to Complete All Tasks**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tasks = [2,2,3,3,2,4,4,4,4,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4. 
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.

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
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        freq = Counter(tasks)
        total_rounds = 0
        
        for count in freq.values():
            if count == 1:
                return -1
            total_rounds += (count + 2) // 3
            
        return total_rounds
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
- [2589. Minimum Time to Complete All Tasks](../../2501-3000/2657-minimum-time-to-complete-all-tasks/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1395-minimum-time-visiting-all-points/)
- [1443. Minimum Time to Collect All Apples in a Tree](../../1501-2000/1554-minimum-time-to-collect-all-apples-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/)
