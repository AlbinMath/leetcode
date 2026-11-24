# LeetCode 2032: Two Out of Three

**LeetCode Problem #2032 — Two Out of Three**
Solve LeetCode Two Out of Three using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Two Out of Three |
| LeetCode | #2032 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given three integer arrays `nums1`, `nums2`, and `nums3`, return *a **distinct** array containing all the values that are present in **at least two** out of the three arrays. You may return the values in **any** order*.

## Constraints
- `1 <= nums1.length, nums2.length, nums3.length <= 100`
- `1 <= nums1[i], nums2[j], nums3[k] <= 100`

## Examples
### Example 1
- **Input:** `nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]`
- **Output:** `[3,2]`
- **Explanation:** The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.

### Example 2
- **Input:** `nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]`
- **Output:** `[2,3,1]`
- **Explanation:** The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.

### Example 3
- **Input:** `nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]`
- **Output:** `[]`
- **Explanation:** No value is present in at least two arrays.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Two Out of Three**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,2]`.
4. **Verification:** The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.

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

  def twoOutOfThree(
      self, nums1: List[int], nums2: List[int], nums3: List[int]
  ) -> List[int]:
    s1, s2, s3 = set(nums1), set(nums2), set(nums3)
    return list((s1 & s2) | (s2 & s3) | (s1 & s3))
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
- [1503. Last Moment Before All Ants Fall Out of a Plank](../../1501-2000/1627-last-moment-before-all-ants-fall-out-of-a-plank/)
- [185. Department Top Three Salaries](../../0001-0500/0185-department-top-three-salaries/)
- [326. Power of Three](../../0001-0500/0326-power-of-three/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/two-out-of-three/)
