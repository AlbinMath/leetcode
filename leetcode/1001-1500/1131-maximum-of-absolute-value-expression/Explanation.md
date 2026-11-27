# LeetCode 1131: Maximum of Absolute Value Expression

**LeetCode Problem #1131 — Maximum of Absolute Value Expression**
Solve LeetCode Maximum of Absolute Value Expression using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum of Absolute Value Expression |
| LeetCode | #1131 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two arrays of integers with equal lengths, return the maximum value of:

`|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|`

where the maximum is taken over all `0 <= i, j < arr1.length`.

## Constraints
- `2 <= arr1.length == arr2.length <= 40000`
- `-10^6 <= arr1[i], arr2[i] <= 10^6`

## Examples
### Example 1
- **Input:** `arr1 = [1,2,3,4], arr2 = [-1,4,5,6]`
- **Output:** `13`

### Example 2
- **Input:** `arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]`
- **Output:** `20`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum of Absolute Value Expression**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr1 = [1,2,3,4], arr2 = [-1,4,5,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.

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
class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        ans = 0
        
        for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            max_val = float('-inf')
            min_val = float('inf')
            
            for i, (a, b) in enumerate(zip(arr1, arr2)):
                curr = s1 * a + s2 * b + i
                if curr > max_val:
                    max_val = curr
                if curr < min_val:
                    min_val = curr
                    
            ans = max(ans, max_val - min_val)
            
        return ans
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
- [1695. Maximum Erasure Value](../../1501-2000/1695-maximum-erasure-value/)
- [1802. Maximum Value at a Given Index in a Bounded Array](../../1501-2000/1802-maximum-value-at-a-given-index-in-a-bounded-array/)
- [1881. Maximum Value after Insertion](../../1501-2000/1881-maximum-value-after-insertion/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-of-absolute-value-expression/)
