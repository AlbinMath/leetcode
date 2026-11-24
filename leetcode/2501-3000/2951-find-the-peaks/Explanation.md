# LeetCode 2951: Find the Peaks

**LeetCode Problem #2951 — Find the Peaks**
Solve LeetCode Find the Peaks using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Peaks |
| LeetCode | #2951 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array `mountain`. Your task is to find all the **peaks** in the `mountain` array.

Return *an array that consists of *indices * of **peaks** in the given array in **any order**.*

**Notes:**

A **peak** is defined as an element that is **strictly greater** than its neighboring elements. 
 The first and last elements of the array are **not** a peak.

## Constraints
- `3 <= mountain.length <= 100`
- `1 <= mountain[i] <= 100`

## Examples
### Example 1
- **Input:** `mountain = [2,4,4]`
- **Output:** `[]`
- **Explanation:** mountain[0] and mountain[2] can not be a peak because they are first and last elements of the array.
mountain[1] also can not be a peak because it is not strictly greater than mountain[2].
So the answer is [].

### Example 2
- **Input:** `mountain = [1,4,3,8,5]`
- **Output:** `[1,3]`
- **Explanation:** mountain[0] and mountain[4] can not be a peak because they are first and last elements of the array.
mountain[2] also can not be a peak because it is not strictly greater than mountain[3] and mountain[1].
But mountain [1] and mountain[3] are strictly greater than their neighboring elements.
So the answer is [1,3].

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Find the Peaks**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mountain = [2,4,4]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[]`.
4. **Verification:** mountain[0] and mountain[2] can not be a peak because they are first and last elements of the array.
mountain[1] also can not be a peak because it is not strictly greater than mountain[2].
So the answer is [].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [i for i in range(1, len(mountain) - 1)
                if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]]
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [3187. Peaks in Array](../../3001-3500/3187-peaks-in-array/)
- [4017. Peaks in Array II](../../4001-4500/4017-peaks-in-array-ii/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-peaks/)
