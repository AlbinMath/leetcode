# LeetCode 231: Power of Two

**LeetCode Problem #231 — Power of Two**
Solve LeetCode Power of Two using PHP and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Power of Two |
| LeetCode | #231 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2^x`.

## Constraints
- `-2^31 <= n <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `true`
- **Explanation:** 2^0 = 1

### Example 2
- **Input:** `n = 16`
- **Output:** `true`
- **Explanation:** 2^4 = 16

### Example 3
- **Input:** `n = 3`
- **Output:** `false`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Power of Two**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** 2^0 = 1

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
    function isPowerOfTwo($n) {
        return $n > 0 && (($n & ($n - 1)) == 0);
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
- [1. Two Sum](../../0001-0500/0001-two-sum/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [4. Median of Two Sorted Arrays](../../0001-0500/0004-median-of-two-sorted-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/power-of-two/)
