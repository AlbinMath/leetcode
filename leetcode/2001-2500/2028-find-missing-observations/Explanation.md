# LeetCode 2028: Find Missing Observations

**LeetCode Problem #2028 — Find Missing Observations**
Solve LeetCode Find Missing Observations using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Missing Observations |
| LeetCode | #2028 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have observations of `n + m` **6-sided** dice rolls with each face numbered from `1` to `6`. `n` of the observations went missing, and you only have the observations of `m` rolls. Fortunately, you have also calculated the **average value** of the `n + m` rolls.

You are given an integer array `rolls` of length `m` where `rolls[i]` is the value of the `i^th` observation. You are also given the two integers `mean` and `n`.

Return *an array of length *`n`* containing the missing observations such that the **average value **of the *`n + m`* rolls is **exactly** *`mean`. If there are multiple valid answers, return *any of them*. If no such array exists, return *an empty array*.

The **average value** of a set of `k` numbers is the sum of the numbers divided by `k`.

Note that `mean` is an integer, so the sum of the `n + m` rolls should be divisible by `n + m`.

## Constraints
- `m == rolls.length`
- `1 <= n, m <= 10^5`
- `1 <= rolls[i], mean <= 6`

## Examples
### Example 1
- **Input:** `rolls = [3,2,4,3], mean = 4, n = 2`
- **Output:** `[6,6]`
- **Explanation:** The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

### Example 2
- **Input:** `rolls = [1,5,6], mean = 3, n = 4`
- **Output:** `[2,3,2,2]`
- **Explanation:** The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.

### Example 3
- **Input:** `rolls = [1,2,3,4], mean = 6, n = 4`
- **Output:** `[]`
- **Explanation:** It is impossible for the mean to be 6 no matter what the 4 missing rolls are.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Missing Observations**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rolls = [3,2,4,3], mean = 4, n = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[6,6]`.
4. **Verification:** The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

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
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        missing = mean * (n + m) - sum(rolls)
        if missing < n or missing > 6 * n:
            return []
        q, r = divmod(missing, n)
        return [q + 1] * r + [q] * (n - r)
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
- [3471. Find the Largest Almost Missing Integer](../../3001-3500/3471-find-the-largest-almost-missing-integer/)
- [3731. Find Missing Elements](../../3501-4000/3731-find-missing-elements/)
- [41. First Missing Positive](../../0001-0500/0041-first-missing-positive/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-missing-observations/)
