# LeetCode 2022: Convert 1D Array Into 2D Array

**LeetCode Problem #2022 — Convert 1D Array Into 2D Array**
Solve LeetCode Convert 1D Array Into 2D Array using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Convert 1D Array Into 2D Array |
| LeetCode | #2022 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 1-dimensional (1D) integer array `original`, and two integers, `m` and `n`. You are tasked with creating a 2-dimensional (2D) array with ` m` rows and `n` columns using **all** the elements from `original`.

The elements from indices `0` to `n - 1` (**inclusive**) of `original` should form the first row of the constructed 2D array, the elements from indices `n` to `2 * n - 1` (**inclusive**) should form the second row of the constructed 2D array, and so on.

Return *an *`m x n`* 2D array constructed according to the above procedure, or an empty 2D array if it is impossible*.

## Constraints
- `1 <= original.length <= 5 * 10^4`
- `1 <= original[i] <= 10^5`
- `1 <= m, n <= 4 * 10^4`

## Examples
### Example 1
- **Input:** `original = [1,2,3,4], m = 2, n = 2`
- **Output:** `[[1,2],[3,4]]`
- **Explanation:** The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

### Example 2
- **Input:** `original = [1,2,3], m = 1, n = 3`
- **Output:** `[[1,2,3]]`
- **Explanation:** The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.

### Example 3
- **Input:** `original = [1,2], m = 1, n = 1`
- **Output:** `[]`
- **Explanation:** There are 2 elements in original.
It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Convert 1D Array Into 2D Array**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `original = [1,2,3,4], m = 2, n = 2`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2],[3,4]]`.
4. **Verification:** The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

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
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        return [original[i * n:(i + 1) * n] for i in range(m)]
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
- [108. Convert Sorted Array to Binary Search Tree](../../0001-0500/0108-convert-sorted-array-to-binary-search-tree/)
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0872-split-array-into-fibonacci-sequence/)
- [1480. Running Sum of 1d Array](../../1501-2000/1603-running-sum-of-1d-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/convert-1d-array-into-2d-array/)
