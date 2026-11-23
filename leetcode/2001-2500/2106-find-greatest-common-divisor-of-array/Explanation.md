# LeetCode 1979: Find Greatest Common Divisor of Array

**LeetCode Problem #1979 — Find Greatest Common Divisor of Array**
Solve LeetCode Find Greatest Common Divisor of Array using Kotlin and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Greatest Common Divisor of Array |
| LeetCode | #1979 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, return** ***the **greatest common divisor** of the smallest number and largest number in *`nums`.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

## Constraints
- `2 <= nums.length <= 1000`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [2,5,6,9,10]`
- **Output:** `2`
- **Explanation:** The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

### Example 2
- **Input:** `nums = [7,5,6,8,3]`
- **Output:** `1`
- **Explanation:** The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

### Example 3
- **Input:** `nums = [3,3]`
- **Output:** `3`
- **Explanation:** The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
1. Find the minimum and maximum of the array.
2. Compute the GCD of those two values using the Euclidean algorithm.

Time complexity is $O(N + \log(\min))$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,5,6,9,10]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)


```kotlin
class Solution {
    fun findGCD(nums: IntArray): Int {
        var a = nums.minOrNull()!!
        var b = nums.maxOrNull()!!

        while (b != 0) {
            val t = b
            b = a % b
            a = t
        }
        return a
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
- [2657. Find the Prefix Common Array of Two Arrays](../../2501-3000/2766-find-the-prefix-common-array-of-two-arrays/)
- [1071. Greatest Common Divisor of Strings](../../1001-1500/1146-greatest-common-divisor-of-strings/)
- [2709. Greatest Common Divisor Traversal](../../2501-3000/2827-greatest-common-divisor-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)
