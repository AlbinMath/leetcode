# LeetCode 1464: Maximum Product of Two Elements in an Array

**LeetCode Problem #1464 — Maximum Product of Two Elements in an Array**
Solve LeetCode Maximum Product of Two Elements in an Array using Scala and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Two Elements in an Array |
| LeetCode | #1464 |
| Difficulty | Easy |
| Language | Scala |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `nums`.

Choose two **different** indices `i` and `j` of that array.

Return the **maximum** value of `(nums[i] - 1) * (nums[j] - 1)`.

## Constraints
- `2 <= nums.length <= 500`
- `1 <= nums[i] <= 10^3`

## Examples
### Example 1
- **Input:** `nums = [3,4,5,2]`
- **Output:** `12`
- **Explanation:** If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

### Example 2
- **Input:** `nums = [1,5,4,5]`
- **Output:** `16`
- **Explanation:** Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

### Example 3
- **Input:** `nums = [3,7]`
- **Output:** `12`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code finds the two largest elements in the array (either by sorting or a single-pass scan). The maximum product is `(largest - 1) * (secondLargest - 1)` since subtracting 1 from the two biggest numbers gives the best result.

Time complexity is $O(N)$ with a single pass (or $O(N \log N)$ with sorting) and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,4,5,2]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

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
Scala

## Source Code
- [solution.scala](./solution.scala)


```scala
object Solution {
    def maxProduct(nums: Array[Int]): Int = {
        var first = 0
        var second = 0

        for (num <- nums) {
            if (num > first) {
                second = first
                first = num
            } else if (num > second) {
                second = num
            }
        }

        (first - 1) * (second - 1)
    }
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
- [1969. Minimum Non-Zero Product of the Array Elements](../../1501-2000/1969-minimum-non-zero-product-of-the-array-elements/)
- [1913. Maximum Product Difference Between Two Pairs](../../1501-2000/1913-maximum-product-difference-between-two-pairs/)
- [1960. Maximum Product of the Length of Two Palindromic Substrings](../../1501-2000/1960-maximum-product-of-the-length-of-two-palindromic-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)
