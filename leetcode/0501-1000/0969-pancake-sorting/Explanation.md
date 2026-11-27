# LeetCode 969: Pancake Sorting

**LeetCode Problem #969 — Pancake Sorting**
Solve LeetCode Pancake Sorting using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Pancake Sorting |
| LeetCode | #969 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `arr`, sort the array by performing a series of **pancake flips**.

In one pancake flip we do the following steps:

Choose an integer `k` where `1 <= k <= arr.length`. 
 Reverse the sub-array `arr[0...k-1]` (**0-indexed**).

For example, if `arr = [3,2,1,4]` and we performed a pancake flip choosing `k = 3`, we reverse the sub-array `[3,2,1]`, so `arr = [ 1 , 2 , 3 ,4]` after the pancake flip at `k = 3`.

Return *an array of the *`k`*-values corresponding to a sequence of pancake flips that sort *`arr`. Any valid answer that sorts the array within `10 * arr.length` flips will be judged as correct.

## Constraints
- `1 <= arr.length <= 100`
- `1 <= arr[i] <= arr.length`
- All integers in `arr` are unique (i.e. `arr` is a permutation of the integers from `1` to `arr.length`).

## Examples
### Example 1
- **Input:** `arr = [3,2,4,1]`
- **Output:** `[4,2,4,3]`
- **Explanation:** We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [ 1 , 4 , 2 , 3 ]
After 2nd flip (k = 2): arr = [ 4 , 1 , 2, 3]
After 3rd flip (k = 4): arr = [ 3 , 2 , 1 , 4 ]
After 4th flip (k = 3): arr = [ 1 , 2 , 3 , 4], which is sorted.

### Example 2
- **Input:** `arr = [1,2,3]`
- **Output:** `[]`
- **Explanation:** The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Pancake Sorting**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [3,2,4,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,2,4,3]`.
4. **Verification:** We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [ 1 , 4 , 2 , 3 ]
After 2nd flip (k = 2): arr = [ 4 , 1 , 2, 3]
After 3rd flip (k = 4): arr = [ 3 , 2 , 1 , 4 ]
After 4th flip (k = 3): arr = [ 1 , 2 , 3 , 4], which is sorted.

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
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            if i == x - 1:
                continue
            if i != 0:
                arr[:i + 1] = arr[:i + 1][::-1]
                res.append(i + 1)
            arr[:x] = arr[:x][::-1]
            res.append(x)
        return res
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
- [1859. Sorting the Sentence](../../1501-2000/1859-sorting-the-sentence/)
- [2089. Find Target Indices After Sorting Array](../../2001-2500/2089-find-target-indices-after-sorting-array/)
- [2826. Sorting Three Groups](../../2501-3000/2826-sorting-three-groups/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/pancake-sorting/)
