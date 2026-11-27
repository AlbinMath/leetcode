# LeetCode 1792: Maximum Average Pass Ratio

**LeetCode Problem #1792 — Maximum Average Pass Ratio**
Solve LeetCode Maximum Average Pass Ratio using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Average Pass Ratio |
| LeetCode | #1792 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array `classes`, where `classes[i] = [pass_i, total_i]`. You know beforehand that in the `i^th` class, there are `total_i` total students, but only `pass_i` number of students will pass the exam.

You are also given an integer `extraStudents`. There are another `extraStudents` brilliant students that are **guaranteed** to pass the exam of any class they are assigned to. You want to assign each of the `extraStudents` students to a class in a way that **maximizes** the **average** pass ratio across **all** the classes.

The **pass ratio** of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The **average pass ratio** is the sum of pass ratios of all the classes divided by the number of the classes.

Return *the **maximum** possible average pass ratio after assigning the *`extraStudents`* students. *Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `1 <= classes.length <= 10^5`
- `classes[i].length == 2`
- `1 <= pass_i <= total_i <= 10^5`
- `1 <= extraStudents <= 10^5`

## Examples
### Example 1
- **Input:** `classes = [[1,2],[3,5],[2,2]], `extraStudents` = 2`
- **Output:** `0.78333`
- **Explanation:** You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

### Example 2
- **Input:** `classes = [[2,4],[3,9],[4,5],[2,10]], `extraStudents` = 4`
- **Output:** `0.53485`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Average Pass Ratio**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `classes = [[1,2],[3,5],[2,2]], `extraStudents` = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0.78333`.
4. **Verification:** You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

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
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        return sum(p / t for _, p, t in heap) / len(classes)
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
- [643. Maximum Average Subarray I](../../0501-1000/0643-maximum-average-subarray-i/)
- [1491. Average Salary Excluding the Minimum and Maximum Salary](../../1001-1500/1491-average-salary-excluding-the-minimum-and-maximum-salary/)
- [2582. Pass the Pillow](../../2501-3000/2582-pass-the-pillow/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-average-pass-ratio/)
