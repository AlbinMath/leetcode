# LeetCode 1944: Number of Visible People in a Queue

**LeetCode Problem #1944 — Number of Visible People in a Queue**
Solve LeetCode Number of Visible People in a Queue using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Visible People in a Queue |
| LeetCode | #1944 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` people standing in a queue, and they numbered from `0` to `n - 1` in **left to right** order. You are given an array `heights` of **distinct** integers where `heights[i]` represents the height of the `i^th` person.

A person can **see** another person to their right in the queue if everybody in between is **shorter** than both of them. More formally, the `i^th` person can see the `j^th` person if `i < j` and `min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1])`.

Return *an array *`answer`* of length *`n`* where *`answer[i]`* is the **number of people** the *`i^th`* person can **see** to their right in the queue*.

## Constraints
- `n == heights.length`
- `1 <= n <= 10^5`
- `1 <= heights[i] <= 10^5`
- All the values of `heights` are **unique**.

## Examples
### Example 1
- **Input:** `heights = [10,6,8,5,11,9]`
- **Output:** `[3,1,2,1,1,0]`
- **Explanation:** Person 0 can see person 1, 2, and 4.
Person 1 can see person 2.
Person 2 can see person 3 and 4.
Person 3 can see person 4.
Person 4 can see person 5.
Person 5 can see no one since nobody is to the right of them.

### Example 2
- **Input:** `heights = [5,1,2,3,10]`
- **Output:** `[4,1,1,1,0]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Visible People in a Queue**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `heights = [10,6,8,5,11,9]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,1,2,1,1,0]`.
4. **Verification:** Person 0 can see person 1, 2, and 4.
Person 1 can see person 2.
Person 2 can see person 3 and 4.
Person 3 can see person 4.
Person 4 can see person 5.
Person 5 can see no one since nobody is to the right of them.

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
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # Shorter people are visible and then blocked by the
            # first person taller than them.
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                answer[i] += 1

            # The first person taller than heights[i] is also visible.
            if stack:
                answer[i] += 1

            stack.append(i)

        return answer
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
- [2327. Number of People Aware of a Secret](../../2001-2500/2327-number-of-people-aware-of-a-secret/)
- [3025. Find the Number of Ways to Place People I](../../3001-3500/3025-find-the-number-of-ways-to-place-people-i/)
- [3027. Find the Number of Ways to Place People II](../../3001-3500/3027-find-the-number-of-ways-to-place-people-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-visible-people-in-a-queue/)
