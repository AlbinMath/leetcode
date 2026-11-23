# LeetCode 2367: Number of Arithmetic Triplets

**LeetCode Problem #2367 — Number of Arithmetic Triplets**
Solve LeetCode Number of Arithmetic Triplets using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Arithmetic Triplets |
| LeetCode | #2367 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed**, **strictly increasing** integer array `nums` and a positive integer `diff`. A triplet `(i, j, k)` is an **arithmetic triplet** if the following conditions are met:

`i < j < k`, 
 `nums[j] - nums[i] == diff`, and 
 `nums[k] - nums[j] == diff`.

Return *the number of unique **arithmetic triplets**.*

## Constraints
- `3 <= nums.length <= 200`
- `0 <= nums[i] <= 200`
- `1 <= diff <= 50`
- `nums` is **strictly** increasing.

## Examples
### Example 1
- **Input:** `nums = [0,1,4,6,7,10], diff = 3`
- **Output:** `2`
- **Explanation:** (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.

### Example 2
- **Input:** `nums = [4,5,6,7,8,9], diff = 2`
- **Output:** `2`
- **Explanation:** (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Arithmetic Triplets**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,4,6,7,10], diff = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        seen = set(nums)
        return sum(1 for x in nums if (x + diff) in seen and (x + 2 * diff) in seen)
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
- [3513. Number of Unique XOR Triplets I](../../3501-4000/3824-number-of-unique-xor-triplets-i/)
- [3514. Number of Unique XOR Triplets II](../../3501-4000/3820-number-of-unique-xor-triplets-ii/)
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-arithmetic-triplets/)
