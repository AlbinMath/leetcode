# LeetCode 1095: Find in Mountain Array

**LeetCode Problem #1095 — Find in Mountain Array**
Solve LeetCode Find in Mountain Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find in Mountain Array |
| LeetCode | #1095 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
*(This problem is an **interactive problem**.)*

You may recall that an array `arr` is a **mountain array** if and only if:

`arr.length >= 3` 
 There exists some `i` with `0 < i < arr.length - 1` such that:
 
 `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]` 
 `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given a mountain array `mountainArr`, return the **minimum** `index` such that `mountainArr.get(index) == target`. If such an `index` does not exist, return `-1`.

**You cannot access the mountain array directly.** You may only access the array using a `MountainArray` interface:

`MountainArray.get(k)` returns the element of the array at index `k` (0-indexed). 
 `MountainArray.length()` returns the length of the array.

Submissions making more than `100` calls to `MountainArray.get` will be judged *Wrong Answer*. Also, any solutions that attempt to circumvent the judge will result in disqualification.

## Constraints
- `3 <= mountainArr.length() <= 10^4`
- `0 <= target <= 10^9`
- `0 <= mountainArr.get(index) <= 10^9`

## Examples
### Example 1
- **Input:** `mountainArr = [1,2,3,4,5,3,1], target = 3`
- **Output:** `2`
- **Explanation:** 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

### Example 2
- **Input:** `mountainArr = [0,1,2,4,2,1], target = 3`
- **Output:** `-1`
- **Explanation:** 3 does not exist in `the array,` so we return -1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find in Mountain Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mountainArr = [1,2,3,4,5,3,1], target = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        cache = {}

        def get(i: int) -> int:
            if i not in cache:
                cache[i] = mountain_arr.get(i)
            return cache[i]

        n = mountain_arr.length()

        # 1. find the peak index
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if get(mid) < get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo

        # 2. search the ascending part [0, peak]
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            v = get(mid)
            if v == target:
                return mid
            if v < target:
                lo = mid + 1
            else:
                hi = mid - 1

        # 3. search the descending part [peak + 1, n - 1]
        lo, hi = peak + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = get(mid)
            if v == target:
                return mid
            if v > target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../../0001-0500/0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-in-mountain-array/)
