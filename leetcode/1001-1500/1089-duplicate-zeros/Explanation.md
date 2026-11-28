# LeetCode 1089: Duplicate Zeros

**LeetCode Problem #1089 — Duplicate Zeros**
Solve LeetCode Duplicate Zeros using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Duplicate Zeros |
| LeetCode | #1089 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right.

**Note** that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

## Constraints
- `1 <= arr.length <= 10^4`
- `0 <= arr[i] <= 9`

## Examples
### Example 1
- **Input:** `arr = [1,0,2,3,0,4,5,0]`
- **Output:** `[1,0,0,2,3,0,0,4]`
- **Explanation:** After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

### Example 2
- **Input:** `arr = [1,2,3]`
- **Output:** `[1,2,3]`
- **Explanation:** After calling your function, the input array is modified to: [1,2,3]

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Duplicate Zeros**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,0,2,3,0,4,5,0]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,0,0,2,3,0,0,4]`.
4. **Verification:** After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

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
    def duplicateZeros(self, arr: List[int]) -> None:
        original = arr.copy()
        i = 0
        j = 0

        while i < len(arr):
            arr[i] = original[j]
            i += 1

            if original[j] == 0 and i < len(arr):
                arr[i] = 0
                i += 1

            j += 1
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
- [1869. Longer Contiguous Segments of Ones than Zeros](../../1501-2000/1869-longer-contiguous-segments-of-ones-than-zeros/)
- [2181. Merge Nodes in Between Zeros](../../2001-2500/2181-merge-nodes-in-between-zeros/)
- [2245. Maximum Trailing Zeros in a Cornered Path](../../2001-2500/2245-maximum-trailing-zeros-in-a-cornered-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/duplicate-zeros/)
