# LeetCode 3658: GCD of Odd and Even Sums

**LeetCode Problem #3658 — GCD of Odd and Even Sums**
Solve LeetCode GCD of Odd and Even Sums using Kotlin and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | GCD of Odd and Even Sums |
| LeetCode | #3658 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`. Your task is to compute the **GCD** (greatest common divisor) of two values:

`sumOdd`: the sum of the smallest `n` positive odd numbers.

`sumEven`: the sum of the smallest `n` positive even numbers.

Return the GCD of `sumOdd` and `sumEven`.

## Constraints
- `1 <= n <= 10​​​​​​​00`

## Examples
### Example 1
- **Input:** `n = 4`
- **Output:** `4`
- **Explanation:** Sum of the first 4 odd numbers `sumOdd = 1 + 3 + 5 + 7 = 16` 
 Sum of the first 4 even numbers `sumEven = 2 + 4 + 6 + 8 = 20` 
 

 Hence, `GCD(sumOdd, sumEven) = GCD(16, 20) = 4`.

### Example 2
- **Input:** `n = 5`
- **Output:** `5`
- **Explanation:** Sum of the first 5 odd numbers `sumOdd = 1 + 3 + 5 + 7 + 9 = 25` 
 Sum of the first 5 even numbers `sumEven = 2 + 4 + 6 + 8 + 10 = 30` 
 

 Hence, `GCD(sumOdd, sumEven) = GCD(25, 30) = 5`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **GCD of Odd and Even Sums**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Sum of the first 4 odd numbers `sumOdd = 1 + 3 + 5 + 7 = 16` 
 Sum of the first 4 even numbers `sumEven = 2 + 4 + 6 + 8 = 20` 
 

 Hence, `GCD(sumOdd, sumEven) = GCD(16, 20) = 4`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)


```kotlin
class Solution {
    fun gcdOfOddEvenSums(n: Int): Int {
        // Sum of first n odd numbers = n²
        val sumOdd = n * n

        // Sum of first n even numbers = n(n + 1)
        val sumEven = n * (n + 1)

        // GCD(n², n(n+1)) = n
        return n
    }
}
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [328. Odd Even Linked List](../../0001-0500/0328-odd-even-linked-list/)
- [975. Odd Even Jump](../../0501-1000/0975-odd-even-jump/)
- [1116. Print Zero Even Odd](../../1001-1500/1116-print-zero-even-odd/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums/)
