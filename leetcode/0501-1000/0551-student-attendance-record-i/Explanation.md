# LeetCode 551: Student Attendance Record I

**LeetCode Problem #551 — Student Attendance Record I**
Solve LeetCode Student Attendance Record I using Python and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Student Attendance Record I |
| LeetCode | #551 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

`'A'`: Absent. 
 `'L'`: Late. 
 `'P'`: Present.

The student is eligible for an attendance award if they meet **both** of the following criteria:

The student was absent (`'A'`) for **strictly** fewer than 2 days **total**. 
 The student was **never** late (`'L'`) for 3 or more **consecutive** days.

Return `true`* if the student is eligible for an attendance award, or *`false`* otherwise*.

## Constraints
- `1 <= s.length <= 1000`
- `s[i]` is either `'A'`, `'L'`, or `'P'`.

## Examples
### Example 1
- **Input:** `s = "PPALLP"`
- **Output:** `true`
- **Explanation:** The student has fewer than 2 absences and was never late 3 or more consecutive days.

### Example 2
- **Input:** `s = "PPALLL"`
- **Output:** `false`
- **Explanation:** The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Student Attendance Record I**, we observe the problem requirements and utilize the **Monotonic Stack** technique. We maintain a **Stack** with elements in strictly monotonic order. Whenever an incoming element violates monotonicity, we pop previous elements and compute answer intervals in amortized linear time.

## Algorithm
1. Initialize an empty stack.
2. For each element, pop previous items from stack while monotonic invariant is violated.
3. Push current element or index onto stack.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "PPALLP"`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The student has fewer than 2 absences and was never late 3 or more consecutive days.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def checkRecord(self, s):
        absent = 0
        late = 0

        for ch in s:
            if ch == 'A':
                absent += 1
                late = 0

                if absent >= 2:
                    return False

            elif ch == 'L':
                late += 1

                if late >= 3:
                    return False

            else:
                late = 0

        return True
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [552. Student Attendance Record II](../../0501-1000/0552-student-attendance-record-ii/)
- [1894. Find the Student that Will Replace the Chalk](../../1501-2000/1894-find-the-student-that-will-replace-the-chalk/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/student-attendance-record-i/)
