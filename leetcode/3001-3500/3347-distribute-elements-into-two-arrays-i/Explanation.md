# LeetCode 3069: Distribute Elements Into Two Arrays I

**LeetCode Problem #3069 — Distribute Elements Into Two Arrays I**
Solve LeetCode Distribute Elements Into Two Arrays I using Go and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distribute Elements Into Two Arrays I |
| LeetCode | #3069 |
| Difficulty | Easy |
| Language | Go |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **1-indexed** array of **distinct** integers `nums` of length `n`.

You need to distribute all the elements of `nums` between two arrays `arr1` and `arr2` using `n` operations. In the first operation, append `nums[1]` to `arr1`. In the second operation, append `nums[2]` to `arr2`. Afterwards, in the `i^th` operation:

If the last element of `arr1` is** greater** than the last element of `arr2`, append `nums[i]` to `arr1`. Otherwise, append `nums[i]` to `arr2`.

The array `result` is formed by concatenating the arrays `arr1` and `arr2`. Concatenating two arrays appends the second to the end of the first; for example, concatenating `[1,2,3]` with `[4,5,6]` gives `[1,2,3,4,5,6]`.

Return *the array* `result`.

## Constraints
- `3 <= n <= 50`
- `1 <= nums[i] <= 100`
- All elements in `nums` are distinct.

## Examples
### Example 1
- **Input:** `nums = [2,1,3]`
- **Output:** `[2,3,1]`
- **Explanation:** After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (2 > 1), append nums[3] to arr1.
After 3 operations, arr1 = [2,3] and arr2 = [1].
Hence, the array result formed by concatenation is [2,3,1].

### Example 2
- **Input:** `nums = [5,4,3,8]`
- **Output:** `[5,3,4,8]`
- **Explanation:** After the first 2 operations, arr1 = [5] and arr2 = [4].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (5 > 4), append nums[3] to arr1, hence arr1 becomes [5,3].
In the 4^th operation, as the last element of arr2 is greater than the last element of arr1 (4 > 3), append nums[4] to arr2, hence arr2 becomes [4,8].
After 4 operations, arr1 = [5,3] and arr2 = [4,8].
Hence, the array result formed by concatenation is [5,3,4,8].

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Distribute Elements Into Two Arrays I**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3,1]`.
4. **Verification:** After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (2 > 1), append nums[3] to arr1.
After 3 operations, arr1 = [2,3] and arr2 = [1].
Hence, the array result formed by concatenation is [2,3,1].

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
Go

## Source Code
- [solution.go](./solution.go)


```go
func resultArray(nums []int) []int {
	arr1 := []int{nums[0]}
	arr2 := []int{nums[1]}

	for i := 2; i < len(nums); i++ {
		if arr1[len(arr1)-1] > arr2[len(arr2)-1] {
			arr1 = append(arr1, nums[i])
		} else {
			arr2 = append(arr2, nums[i])
		}
	}

	return append(arr1, arr2...)
}
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
- [3072. Distribute Elements Into Two Arrays II](../../3001-3500/3350-distribute-elements-into-two-arrays-ii/)
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2162-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [4. Median of Two Sorted Arrays](../../0001-0500/0004-median-of-two-sorted-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/)
