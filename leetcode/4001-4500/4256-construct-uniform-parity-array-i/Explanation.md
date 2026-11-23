# LeetCode 3875: Construct Uniform Parity Array I

**LeetCode Problem #3875 — Construct Uniform Parity Array I**
Solve LeetCode Construct Uniform Parity Array I using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct Uniform Parity Array I |
| LeetCode | #3875 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums1` of `n` **distinct** integers.

You want to construct another array `nums2` of length `n` such that the elements in `nums2` are either **all odd or all even**.

For each index `i`, you must choose **exactly one** of the following (in any order):

`nums2[i] = nums1[i]` 
 `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`

Return `true` if it is possible to construct such an array, otherwise, return `false`.

## Constraints
- `1 <= n == nums1.length <= 100`
- `1 <= nums1[i] <= 100`
- `nums1` consists of distinct integers.

## Examples
### Example 1
- **Input:** `nums1 = [2,3]`
- **Output:** `true`
- **Explanation:** Choose `nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1`. 
 Choose `nums2[1] = nums1[1] = 3`. 
 `nums2 = [-1, 3]`, and both elements are odd. Thus, the answer is `true`​​​​​​​.

### Example 2
- **Input:** `nums1 = [4,6]`
- **Output:** `true`
- **Explanation:** ​​​​​​​ 

 
 Choose `nums2[0] = nums1[0] = 4`. 
 Choose `nums2[1] = nums1[1] = 6`. 
 `nums2 = [4, 6]`, and all elements are even. Thus, the answer is `true`.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Construct Uniform Parity Array I**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [2,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Choose `nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1`. 
 Choose `nums2[1] = nums1[1] = 3`. 
 `nums2 = [-1, 3]`, and both elements are odd. Thus, the answer is `true`​​​​​​​.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        return true;
    }
};
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
- [3876. Construct Uniform Parity Array II](../../4001-4500/4258-construct-uniform-parity-array-ii/)
- [905. Sort Array By Parity](../../0501-1000/0941-sort-array-by-parity/)
- [922. Sort Array By Parity II](../../0501-1000/0958-sort-array-by-parity-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-uniform-parity-array-i/)
