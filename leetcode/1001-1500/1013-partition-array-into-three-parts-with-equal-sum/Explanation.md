# LeetCode 1013: Partition Array Into Three Parts With Equal Sum

**LeetCode Problem #1013 — Partition Array Into Three Parts With Equal Sum**
Solve LeetCode Partition Array Into Three Parts With Equal Sum using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array Into Three Parts With Equal Sum |
| LeetCode | #1013 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `arr`, return `true` if we can partition the array into three **non-empty** parts with equal sums.

Formally, we can partition the array if we can find indexes `i + 1 < j` with `(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])`

## Constraints
- `3 <= arr.length <= 5 * 10^4`
- `-10^4 <= arr[i] <= 10^4`

## Examples
### Example 1
- **Input:** `arr = [0,2,1,-6,6,-7,9,1,2,0,1]`
- **Output:** `true`
- **Explanation:** 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

### Example 2
- **Input:** `arr = [0,2,1,-6,6,7,9,-1,2,0,1]`
- **Output:** `false`

### Example 3
- **Input:** `arr = [3,3,6,5,-2,2,5,1,-9,4]`
- **Output:** `true`
- **Explanation:** 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Partition Array Into Three Parts With Equal Sum**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [0,2,1,-6,6,-7,9,1,2,0,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

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
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        cur = 0
        parts = 0
        for x in arr:
            cur += x
            if cur == target:
                parts += 1
                cur = 0
        return parts >= 3
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
- [3566. Partition Array into Two Equal Product Subsets](../../3501-4000/3566-partition-array-into-two-equal-product-subsets/)
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2035-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [416. Partition Equal Subset Sum](../../0001-0500/0416-partition-equal-subset-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/)
