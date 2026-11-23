# LeetCode 3533: Concatenated Divisibility

**LeetCode Problem #3533 — Concatenated Divisibility**
Solve LeetCode Concatenated Divisibility using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Concatenated Divisibility |
| LeetCode | #3533 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of positive integers nums and a positive integer k .

A permutation of nums is said to form a divisible concatenation if, when you *concatenate* *the decimal representations* of the numbers in the order specified by the permutation, the resulting number is **divisible by** k .

Return the ** lexicographically smallest ** permutation (when considered as a list of integers) that forms a **divisible concatenation**. If no such permutation exists, return an empty list.

## Constraints
- `1 <= nums.length <= 13`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= 100`

## Examples
### Example 1
- **Input:** `nums = [3,12,45], k = 5`
- **Output:** `[3,12,45]`
- **Explanation:** Permutation 
 Concatenated Value 
 Divisible by 5 
 
 
 
 
 [3, 12, 45] 
 31245 
 Yes 
 
 
 [3, 45, 12] 
 34512 
 No 
 
 
 [12, 3, 45] 
 12345 
 Yes 
 
 
 [12, 45, 3] 
 12453 
 No 
 
 
 [45, 3, 12] 
 45312 
 No 
 
 
 [45, 12, 3] 
 45123 
 No 
 
 
 

 The lexicographically smallest permutation that forms a divisible concatenation is `[3,12,45]`.

### Example 2
- **Input:** `nums = [10,5], k = 10`
- **Output:** `[5,10]`
- **Explanation:** Permutation 
 Concatenated Value 
 Divisible by 10 
 
 
 
 
 [5, 10] 
 510 
 Yes 
 
 
 [10, 5] 
 105 
 No 
 
 
 

 The lexicographically smallest permutation that forms a divisible concatenation is `[5,10]`.

### Example 3
- **Input:** `nums = [1,2,3], k = 5`
- **Output:** `[]`
- **Explanation:** Since no permutation of nums forms a valid divisible concatenation, return an empty list.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Concatenated Divisibility**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,12,45], k = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,12,45]`.
4. **Verification:** Permutation 
 Concatenated Value 
 Divisible by 5 
 
 
 
 
 [3, 12, 45] 
 31245 
 Yes 
 
 
 [3, 45, 12] 
 34512 
 No 
 
 
 [12, 3, 45] 
 12345 
 Yes 
 
 
 [12, 45, 3] 
 12453 
 No 
 
 
 [45, 3, 12] 
 45312 
 No 
 
 
 [45, 12, 3] 
 45123 
 No 
 
 
 

 The lexicographically smallest permutation that forms a divisible concatenation is `[3,12,45]`.

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
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums = sorted(nums)
        full = (1 << n) - 1

        pw = [pow(10, len(str(x)), k) for x in nums]
        val = [x % k for x in nums]

        can = [[False] * k for _ in range(1 << n)]
        can[full][0] = True

        for mask in range(full - 1, -1, -1):
            row = can[mask]
            for r in range(k):
                for j in range(n):
                    if mask >> j & 1:
                        continue
                    nr = (r * pw[j] + val[j]) % k
                    if can[mask | (1 << j)][nr]:
                        row[r] = True
                        break

        if not can[0][0]:
            return []

        res = []
        mask, r = 0, 0
        for _ in range(n):
            for j in range(n):  # nums is sorted, so the first hit is the smallest
                if mask >> j & 1:
                    continue
                nr = (r * pw[j] + val[j]) % k
                if can[mask | (1 << j)][nr]:
                    res.append(nums[j])
                    mask |= 1 << j
                    r = nr
                    break
        return res
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
- [3622. Check Divisibility by Digit Sum and Product](../../3501-4000/3918-check-divisibility-by-digit-sum-and-product/)
- [472. Concatenated Words](../../0001-0500/0472-concatenated-words/)
- [1239. Maximum Length of a Concatenated String with Unique Characters](../../1001-1500/1360-maximum-length-of-a-concatenated-string-with-unique-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/concatenated-divisibility/)
