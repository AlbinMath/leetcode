# LeetCode 1014: Best Sightseeing Pair

**LeetCode Problem #1014 — Best Sightseeing Pair**
Solve LeetCode Best Sightseeing Pair using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Best Sightseeing Pair |
| LeetCode | #1014 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `values` where values[i] represents the value of the `i^th` sightseeing spot. Two sightseeing spots `i` and `j` have a **distance** `j - i` between them.

The score of a pair (`i < j`) of sightseeing spots is `values[i] + values[j] + i - j`: the sum of the values of the sightseeing spots, minus the distance between them.

Return *the maximum score of a pair of sightseeing spots*.

## Constraints
- `2 <= values.length <= 5 * 10^4`
- `1 <= values[i] <= 1000`

## Examples
### Example 1
- **Input:** `values = [8,1,5,2,6]`
- **Output:** `11`
- **Explanation:** i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

### Example 2
- **Input:** `values = [1,2]`
- **Output:** `2`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Best Sightseeing Pair**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `values = [8,1,5,2,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `11`.
4. **Verification:** i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

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
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_left = values[0] + 0
        max_score = 0
        
        for j in range(1, len(values)):
            max_score = max(max_score, max_left + values[j] - j)
            max_left = max(max_left, values[j] + j)
            
        return max_score
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
- [646. Maximum Length of Pair Chain](../../0501-1000/0646-maximum-length-of-pair-chain/)
- [719. Find K-th Smallest Pair Distance](../../0501-1000/0719-find-k-th-smallest-pair-distance/)
- [1190. Reverse Substrings Between Each Pair of Parentheses](../../1001-1500/1190-reverse-substrings-between-each-pair-of-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/best-sightseeing-pair/)
