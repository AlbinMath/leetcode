# LeetCode 1437: Check If All 1's Are at Least Length K Places Away

**LeetCode Problem #1437 — Check If All 1's Are at Least Length K Places Away**
Solve LeetCode Check If All 1's Are at Least Length K Places Away using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If All 1's Are at Least Length K Places Away |
| LeetCode | #1437 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an binary array `nums` and an integer `k`, return `true`* if all *`1`*'s are at least *`k`* places away from each other, otherwise return *`false`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= k <= nums.length`
- `nums[i]` is `0` or `1`

## Examples
### Example 1
- **Input:** `nums = [1,0,0,0,1,0,0,1], k = 2`
- **Output:** `true`
- **Explanation:** Each of the 1s are at least 2 places away from each other.

### Example 2
- **Input:** `nums = [1,0,0,1,0,1], k = 2`
- **Output:** `false`
- **Explanation:** The second 1 and third 1 are only one apart from each other.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check If All 1's Are at Least Length K Places Away**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,0,0,0,1,0,0,1], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Each of the 1s are at least 2 places away from each other.

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
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        previous = -1

        for i, num in enumerate(nums):
            if num == 1:
                if previous != -1 and i - previous <= k:
                    return False

                previous = i

        return True
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
- [1497. Check If Array Pairs Are Divisible by k](../../1001-1500/1497-check-if-array-pairs-are-divisible-by-k/)
- [1893. Check if All the Integers in a Range Are Covered](../../1501-2000/1893-check-if-all-the-integers-in-a-range-are-covered/)
- [1461. Check If a String Contains All Binary Codes of Size K](../../1001-1500/1461-check-if-a-string-contains-all-binary-codes-of-size-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/)
