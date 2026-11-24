# LeetCode 2574: Left and Right Sum Differences

**LeetCode Problem #2574 — Left and Right Sum Differences**
Solve LeetCode Left and Right Sum Differences using Kotlin and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Left and Right Sum Differences |
| LeetCode | #2574 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums` of size `n`.

Define two arrays `leftSum` and `rightSum` where:

`leftSum[i]` is the sum of elements to the left of the index `i` in the array `nums`. If there is no such element, `leftSum[i] = 0`. 
 `rightSum[i]` is the sum of elements to the right of the index `i` in the array `nums`. If there is no such element, `rightSum[i] = 0`.

Return an integer array `answer` of size `n` where `answer[i] = |leftSum[i] - rightSum[i]|`.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [10,4,8,3]`
- **Output:** `[15,1,11,22]`
- **Explanation:** The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

### Example 2
- **Input:** `nums = [1]`
- **Output:** `[0]`
- **Explanation:** The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Compute prefix sums for left sums and suffix sums for right sums, then calculate the absolute difference at each index.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,4,8,3]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[15,1,11,22]`.
4. **Verification:** The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)


```kotlin
class Solution {
    fun leftRightDifference(nums: IntArray): IntArray {
        val n = nums.size
        val answer = IntArray(n)

        var total = nums.sum()
        var leftSum = 0

        for (i in 0 until n) {
            // Remove current element from total
            total -= nums[i]

            // total is now the right sum
            answer[i] = kotlin.math.abs(leftSum - total)

            // Add current element to left sum
            leftSum += nums[i]
        }

        return answer
    }
}
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3153. Sum of Digit Differences of All Pairs](../../3001-3500/3153-sum-of-digit-differences-of-all-pairs/)
- [404. Sum of Left Leaves](../../0001-0500/0404-sum-of-left-leaves/)
- [2516. Take K of Each Character From Left and Right](../../2501-3000/2516-take-k-of-each-character-from-left-and-right/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/left-and-right-sum-differences/)
