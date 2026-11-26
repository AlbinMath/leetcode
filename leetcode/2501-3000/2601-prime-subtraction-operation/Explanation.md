# LeetCode 2601: Prime Subtraction Operation

**LeetCode Problem #2601 — Prime Subtraction Operation**
Solve LeetCode Prime Subtraction Operation using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Prime Subtraction Operation |
| LeetCode | #2601 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` of length `n`.

You can perform the following operation as many times as you want:

Pick an index `i` that you haven&rsquo;t picked before, and pick a prime `p` **strictly less than** `nums[i]`, then subtract `p` from `nums[i]`.

Return *true if you can make `nums` a strictly increasing array using the above operation and false otherwise.*

A **strictly increasing array** is an array whose each element is strictly greater than its preceding element.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`
- ` nums.length == n `

## Examples
### Example 1
- **Input:** `nums = [4,9,6,10]`
- **Output:** `true`
- **Explanation:** In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.

### Example 2
- **Input:** `nums = [6,8,11,12]`
- **Output:** `true`
- **Explanation:** Initially nums is sorted in strictly increasing order, so we don't need to make any operations.

### Example 3
- **Input:** `nums = [5,8,3]`
- **Output:** `false`
- **Explanation:** It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Prime Subtraction Operation**, we observe the problem requirements and utilize the **Stack & Queue** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,9,6,10]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.

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
    def primeSubOperation(self, nums: List[int]) -> bool:
        # sieve of primes up to 1000
        N = 1000
        is_p = [True] * (N + 1)
        is_p[0] = is_p[1] = False
        for i in range(2, int(N ** 0.5) + 1):
            if is_p[i]:
                for j in range(i * i, N + 1, i):
                    is_p[j] = False

        # largest_below[x] = largest prime strictly less than x, or 0 if none
        largest_below = [0] * (N + 2)
        last = 0
        for x in range(N + 2):
            largest_below[x] = last
            if x <= N and is_p[x]:
                last = x

        prev = 0
        for x in nums:
            if x <= prev:
                return False
            p = largest_below[x - prev]  # prime < x - prev, so x - p > prev
            x -= p  # p == 0 means no subtraction
            prev = x
        return True
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
- [583. Delete Operation for Two Strings](../../0501-1000/0583-delete-operation-for-two-strings/)
- [1381. Design a Stack With Increment Operation](../../1001-1500/1381-design-a-stack-with-increment-operation/)
- [1486. XOR Operation in an Array](../../1001-1500/1486-xor-operation-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/prime-subtraction-operation/)
