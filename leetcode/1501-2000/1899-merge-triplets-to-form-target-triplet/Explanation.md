# LeetCode 1899: Merge Triplets to Form Target Triplet

**LeetCode Problem #1899 — Merge Triplets to Form Target Triplet**
Solve LeetCode Merge Triplets to Form Target Triplet using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge Triplets to Form Target Triplet |
| LeetCode | #1899 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **triplet** is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [a_i, b_i, c_i]` describes the `i^th` **triplet**. You are also given an integer array `target = [x, y, z]` that describes the **triplet** you want to obtain.

To obtain `target`, you may apply the following operation on `triplets` **any number** of times (possibly **zero**):

Choose two indices (**0-indexed**) `i` and `j` (`i != j`) and **update** `triplets[j]` to become `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]`.

For example, if `triplets[i] = [2, 5, 3]` and `triplets[j] = [1, 7, 5]`, `triplets[j]` will be updated to `[max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5]`.

Return `true` *if it is possible to obtain the *`target`* **triplet** *`[x, y, z]`* as an** element** of *`triplets`*, or *`false`* otherwise*.

## Constraints
- `1 <= triplets.length <= 10^5`
- `triplets[i].length == target.length == 3`
- `1 <= a_i, b_i, c_i, x, y, z <= 1000`

## Examples
### Example 1
- **Input:** `triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]`
- **Output:** `true`
- **Explanation:** Perform the following operations:
- Choose the first and last triplets [ [2,5,3] ,[1,8,4], [1,7,5] ]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4], [2,7,5] ]
The target triplet [2,7,5] is now an element of triplets.

### Example 2
- **Input:** `triplets = [[3,4,5],[4,5,6]], target = [3,2,5]`
- **Output:** `false`
- **Explanation:** It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.

### Example 3
- **Input:** `triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]`
- **Output:** `true`
- **Explanation:** Perform the following operations:
- Choose the first and third triplets [ [2,5,3] ,[2,3,4], [1,2,5] ,[5,2,3]]. Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4], [2,5,5] ,[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4], [2,5,5] , [5,2,3] ]. Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5], [5,5,5] ].
The target triplet [5,5,5] is now an element of triplets.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Merge Triplets to Form Target Triplet**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Perform the following operations:
- Choose the first and last triplets [ [2,5,3] ,[1,8,4], [1,7,5] ]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4], [2,7,5] ]
The target triplet [2,7,5] is now an element of triplets.

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
from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        got = [False, False, False]
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                if a == x:
                    got[0] = True
                if b == y:
                    got[1] = True
                if c == z:
                    got[2] = True
        return all(got)
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
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1526-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)
- [1639. Number of Ways to Form a Target String Given a Dictionary](../../1501-2000/1639-number-of-ways-to-form-a-target-string-given-a-dictionary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/)
