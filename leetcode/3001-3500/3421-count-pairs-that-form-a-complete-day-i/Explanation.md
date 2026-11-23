# LeetCode 3184: Count Pairs That Form a Complete Day I

**LeetCode Problem #3184 — Count Pairs That Form a Complete Day I**
Solve LeetCode Count Pairs That Form a Complete Day I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Pairs That Form a Complete Day I |
| LeetCode | #3184 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `hours` representing times in **hours**, return an integer denoting the number of pairs `i`, `j` where `i < j` and `hours[i] + hours[j]` forms a **complete day**.

A **complete day** is defined as a time duration that is an **exact** **multiple** of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

## Constraints
- `1 <= hours.length <= 100`
- `1 <= hours[i] <= 10^9`

## Examples
### Example 1
- **Input:** `hours = [12,12,30,24,24]`
- **Output:** `2`
- **Explanation:** The pairs of indices that form a complete day are `(0, 1)` and `(3, 4)`.

### Example 2
- **Input:** `hours = [72,48,24,3]`
- **Output:** `3`
- **Explanation:** The pairs of indices that form a complete day are `(0, 1)`, `(0, 2)`, and `(1, 2)`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Pairs That Form a Complete Day I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `hours = [12,12,30,24,24]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The pairs of indices that form a complete day are `(0, 1)` and `(3, 4)`.

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
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        rem_counts = [0] * 24
        pairs = 0
        
        for h in hours:
            rem = h % 24
            complement = (24 - rem) % 24
            pairs += rem_counts[complement]
            rem_counts[rem] += 1
            
        return pairs
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
- [3185. Count Pairs That Form a Complete Day II](../../3001-3500/3418-count-pairs-that-form-a-complete-day-ii/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1501-2000/1553-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [2791. Count Paths That Can Form a Palindrome in a Tree](../../2501-3000/2905-count-paths-that-can-form-a-palindrome-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/)
