# LeetCode 88: Merge Sorted Array

**LeetCode Problem #88 — Merge Sorted Array**
Solve LeetCode Merge Sorted Array using PHP and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge Sorted Array |
| LeetCode | #88 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be *stored inside the array *`nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

## Constraints
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Examples
### Example 1
- **Input:** `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3`
- **Output:** `[1,2,2,3,5,6]`
- **Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [ 1 , 2 ,2, 3 ,5,6] with the underlined elements coming from nums1.

### Example 2
- **Input:** `nums1 = [1], m = 1, nums2 = [], n = 0`
- **Output:** `[1]`
- **Explanation:** The arrays we are merging are [1] and [].
The result of the merge is [1].

### Example 3
- **Input:** `nums1 = [0], m = 0, nums2 = [1], n = 1`
- **Output:** `[1]`
- **Explanation:** The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Merge Sorted Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,2,3,5,6]`.
4. **Verification:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [ 1 , 2 ,2, 3 ,5,6] with the underlined elements coming from nums1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {
    function merge(&$nums1, $m, $nums2, $n) {
        $i = $m - 1;          // Last element in nums1
        $j = $n - 1;          // Last element in nums2
        $k = $m + $n - 1;     // Last position in nums1

        while ($j >= 0) {

            if ($i >= 0 && $nums1[$i] > $nums2[$j]) {
                $nums1[$k] = $nums1[$i];
                $i--;
            } else {
                $nums1[$k] = $nums2[$j];
                $j--;
            }

            $k--;
        }
    }
}
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
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-sorted-array/)
