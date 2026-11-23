# LeetCode 621: Task Scheduler

**LeetCode Problem #621 — Task Scheduler**
Solve LeetCode Task Scheduler using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Task Scheduler |
| LeetCode | #621 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of CPU `tasks`, each labeled with a letter from A to Z, and a number `n`. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of **at least** `n` intervals between two tasks with the same label.

Return the **minimum** number of CPU intervals required to complete all tasks.

## Constraints
- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter.
- `0 <= n <= 100`

## Examples
### Example 1
- **Input:** `tasks = ["A","A","A","B","B","B"], n = 2`
- **Output:** `8`
- **Explanation:** A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B. 

 After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3^rd interval, neither A nor B can be done, so you idle. By the 4^th interval, you can do A again as 2 intervals have passed.

### Example 2
- **Input:** `tasks = ["A","C","A","B","D","B"], n = 1`
- **Output:** `6`
- **Explanation:** A possible sequence is: A -> B -> C -> D -> A -> B. 

 With a cooling interval of 1, you can repeat a task after just one other task.

### Example 3
- **Input:** `tasks = ["A","A","A", "B","B","B"], n = 3`
- **Output:** `10`
- **Explanation:** A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B. 

 There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Task Scheduler**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tasks = ["A","A","A","B","B","B"], n = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B. 

 After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3^rd interval, neither A nor B can be done, so you idle. By the 4^th interval, you can do A again as 2 intervals have passed.

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
    def leastInterval(self, tasks: list[str], n: int) -> int:
        cnt = Counter(tasks)
        maxf = max(cnt.values())
        cnt_max = sum(1 for v in cnt.values() if v == maxf)
        return max(len(tasks), (maxf - 1) * (n + 1) + cnt_max)
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
- [2365. Task Scheduler II](../../2001-2500/2483-task-scheduler-ii/)
- [3408. Design Task Manager](../../3501-4000/3678-design-task-manager/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/task-scheduler/)
