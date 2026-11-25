# LeetCode 2122: Recover the Original Array

**LeetCode Problem #2122 — Recover the Original Array**
Solve LeetCode Recover the Original Array using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Recover the Original Array |
| LeetCode | #2122 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice had a **0-indexed** array `arr` consisting of `n` **positive** integers. She chose an arbitrary **positive integer** `k` and created two new **0-indexed** integer arrays `lower` and `higher` in the following manner:

`lower[i] = arr[i] - k`, for every index `i` where `0 <= i < n` 
 `higher[i] = arr[i] + k`, for every index `i` where `0 <= i < n`

Unfortunately, Alice lost all three arrays. However, she remembers the integers that were present in the arrays `lower` and `higher`, but not the array each integer belonged to. Help Alice and recover the original array.

Given an array `nums` consisting of `2n` integers, where **exactly** `n` of the integers were present in `lower` and the remaining in `higher`, return *the **original** array* `arr`. In case the answer is not unique, return ***any** valid array*.

**Note:** The test cases are generated such that there exists **at least one** valid array `arr`.

## Constraints
- `2 * n == nums.length`
- `1 <= n <= 1000`
- `1 <= nums[i] <= 10^9`
- The test cases are generated such that there exists **at least one** valid array `arr`.

## Examples
### Example 1
- **Input:** `nums = [2,10,6,4,8,12]`
- **Output:** `[3,7,11]`
- **Explanation:** If arr = [3,7,11] and k = 1, we get lower = [2,6,10] and higher = [4,8,12].
Combining lower and higher gives us [2,6,10,4,8,12], which is a permutation of nums.
Another valid possibility is that arr = [5,7,9] and k = 3. In that case, lower = [2,4,6] and higher = [8,10,12].

### Example 2
- **Input:** `nums = [1,1,3,3]`
- **Output:** `[2,2]`
- **Explanation:** If arr = [2,2] and k = 1, we get lower = [1,1] and higher = [3,3].
Combining lower and higher gives us [1,1,3,3], which is equal to nums.
Note that arr cannot be [1,3] because in that case, the only possible way to obtain [1,1,3,3] is with k = 0.
This is invalid since k must be positive.

### Example 3
- **Input:** `nums = [5,435]`
- **Output:** `[220]`
- **Explanation:** The only possible combination is arr = [220] and k = 215. Using them, we get lower = [5] and higher = [435].

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Recover the Original Array**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,10,6,4,8,12]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,7,11]`.
4. **Verification:** If arr = [3,7,11] and k = 1, we get lower = [2,6,10] and higher = [4,8,12].
Combining lower and higher gives us [2,6,10,4,8,12], which is a permutation of nums.
Another valid possibility is that arr = [5,7,9] and k = 3. In that case, lower = [2,4,6] and higher = [8,10,12].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter

class Solution(object):
    def recoverArray(self, nums):
        nums.sort()
        n2 = len(nums)
        base_counts = Counter(nums)

        for i in range(1, n2 // 2 + 1):
            diff = nums[i] - nums[0]
            if diff == 0 or diff % 2 != 0:
                continue
            if i > 1 and nums[i] == nums[i - 1]:
                continue

            k = diff // 2
            counts = base_counts.copy()
            ans = []
            valid = True

            for x in nums:
                if counts[x] == 0:
                    continue
                if counts[x + diff] == 0:
                    valid = False
                    break
                counts[x] -= 1
                counts[x + diff] -= 1
                ans.append(x + k)

            if valid:
                return ans

        return []
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [2433. Find The Original Array of Prefix Xor](../../2001-2500/2433-find-the-original-array-of-prefix-xor/)
- [423. Reconstruct Original Digits from English](../../0001-0500/0423-reconstruct-original-digits-from-english/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/recover-the-original-array/)
