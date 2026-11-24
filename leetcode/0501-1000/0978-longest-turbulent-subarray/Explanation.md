# LeetCode 978: Longest Turbulent Subarray

**LeetCode Problem #978 — Longest Turbulent Subarray**
Solve LeetCode Longest Turbulent Subarray using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Turbulent Subarray |
| LeetCode | #978 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `arr`, return *the length of a maximum size turbulent subarray of* `arr`.

A subarray is **turbulent** if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray `[arr[i], arr[i + 1], ..., arr[j]]` of `arr` is said to be turbulent if and only if:

For `i <= k < j`:

`arr[k] > arr[k + 1]` when `k` is odd, and 
 `arr[k] < arr[k + 1]` when `k` is even. 
 
 
 Or, for `i <= k < j`:
 
 `arr[k] > arr[k + 1]` when `k` is even, and 
 `arr[k] < arr[k + 1]` when `k` is odd.

## Constraints
- `1 <= arr.length <= 4 * 10^4`
- `0 <= arr[i] <= 10^9`

## Examples
### Example 1
- **Input:** `arr = [9,4,2,10,7,8,8,1,9]`
- **Output:** `5`
- **Explanation:** arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

### Example 2
- **Input:** `arr = [4,8,12,16]`
- **Output:** `2`

### Example 3
- **Input:** `arr = [100]`
- **Output:** `1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Turbulent Subarray**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [9,4,2,10,7,8,8,1,9]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

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
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = down = max_len = 1
        
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                up, down = down + 1, 1
            elif arr[i - 1] > arr[i]:
                down, up = up + 1, 1
            else:
                up = down = 1
                
            if up > max_len:
                max_len = up
            if down > max_len:
                max_len = down
                
        return max_len
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
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](../../1001-1500/1438-longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
- [1493. Longest Subarray of 1's After Deleting One Element](../../1001-1500/1493-longest-subarray-of-1s-after-deleting-one-element/)
- [2401. Longest Nice Subarray](../../2001-2500/2401-longest-nice-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-turbulent-subarray/)
