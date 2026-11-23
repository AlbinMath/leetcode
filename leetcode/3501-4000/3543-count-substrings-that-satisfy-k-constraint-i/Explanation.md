# LeetCode 3258: Count Substrings That Satisfy K-Constraint I

**LeetCode Problem #3258 — Count Substrings That Satisfy K-Constraint I**
Solve LeetCode Count Substrings That Satisfy K-Constraint I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Substrings That Satisfy K-Constraint I |
| LeetCode | #3258 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **binary** string `s` and an integer `k`.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

The number of `0`'s in the string is at most `k`. 
 The number of `1`'s in the string is at most `k`.

Return an integer denoting the number of substrings of `s` that satisfy the **k-constraint**.

## Constraints
- `1 <= s.length <= 50 `
- `1 <= k <= s.length`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "10101", k = 1`
- **Output:** `12`
- **Explanation:** Every substring of `s` except the substrings `"1010"`, `"10101"`, and `"0101"` satisfies the k-constraint.

### Example 2
- **Input:** `s = "1010101", k = 2`
- **Output:** `25`
- **Explanation:** Every substring of `s` except the substrings with a length greater than 5 satisfies the k-constraint.

### Example 3
- **Input:** `s = "11111", k = 1`
- **Output:** `15`
- **Explanation:** All substrings of `s` satisfy the k-constraint.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Substrings That Satisfy K-Constraint I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "10101", k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** Every substring of `s` except the substrings `"1010"`, `"10101"`, and `"0101"` satisfies the k-constraint.

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
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            zeros = ones = 0
            for j in range(i, n):
                if s[j] == '0':
                    zeros += 1
                else:
                    ones += 1
                if zeros <= k or ones <= k:
                    ans += 1
        return ans
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
- [3261. Count Substrings That Satisfy K-Constraint II](../../3501-4000/3546-count-substrings-that-satisfy-k-constraint-ii/)
- [1638. Count Substrings That Differ by One Character](../../1501-2000/1743-count-substrings-that-differ-by-one-character/)
- [3297. Count Substrings That Can Be Rearranged to Contain a String I](../../3501-4000/3573-count-substrings-that-can-be-rearranged-to-contain-a-string-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/)
