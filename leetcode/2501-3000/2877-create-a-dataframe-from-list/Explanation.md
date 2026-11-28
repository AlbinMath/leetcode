# LeetCode 2877: Create a DataFrame from List

**LeetCode Problem #2877 — Create a DataFrame from List**
Solve LeetCode Create a DataFrame from List using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Create a DataFrame from List |
| LeetCode | #2877 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Write a solution to **create** a DataFrame from a 2D list called `student_data`. This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, `student_id` and `age`, and be in the same order as the original 2D list.

The result format is in the following example.

## Examples
### Example 1
- **Input:** `student_data:`
- **Output:** `+------------+-----+
| student_id | age |
+------------+-----+
| 1 | 15 |
| 2 | 11 |
| 3 | 11 |
| 4 | 20 |
+------------+-----+`
- **Explanation:** A DataFrame was created on top of student_data, with two columns named `student_id` and `age`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Create a DataFrame from List**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `student_data:`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `+------------+-----+
| student_id | age |
+------------+-----+
| 1 | 15 |
| 2 | 11 |
| 3 | 11 |
| 4 | 20 |
+------------+-----+`.
4. **Verification:** A DataFrame was created on top of student_data, with two columns named `student_id` and `age`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2196. Create Binary Tree From Descriptions](../../2001-2500/2196-create-binary-tree-from-descriptions/)
- [19. Remove Nth Node From End of List](../../0001-0500/0019-remove-nth-node-from-end-of-list/)
- [82. Remove Duplicates from Sorted List II](../../0001-0500/0082-remove-duplicates-from-sorted-list-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-a-dataframe-from-list/)
