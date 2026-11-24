# LeetCode 2844: Minimum Operations to Make a Special Number

**LeetCode Problem #2844 — Minimum Operations to Make a Special Number**
Solve LeetCode Minimum Operations to Make a Special Number using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make a Special Number |
| LeetCode | #2844 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string `num` representing a non-negative integer.

In one operation, you can pick any digit of `num` and delete it. Note that if you delete all the digits of `num`, `num` becomes `0`.

Return *the **minimum number of operations** required to make* `num` special .

An integer `x` is considered **special** if it is divisible by `25`.

## Constraints
- `1 <= num.length <= 100`
- `num` only consists of digits `'0'` through `'9'`.
- `num` does not contain any leading zeros.

## Examples
### Example 1
- **Input:** `num = "2245047"`
- **Output:** `2`
- **Explanation:** Delete digits num[5] and num[6]. The resulting number is "22450" which is special since it is divisible by 25.
It can be shown that 2 is the minimum number of operations required to get a special number.

### Example 2
- **Input:** `num = "2908305"`
- **Output:** `3`
- **Explanation:** Delete digits num[3], num[4], and num[6]. The resulting number is "2900" which is special since it is divisible by 25.
It can be shown that 3 is the minimum number of operations required to get a special number.

### Example 3
- **Input:** `num = "10"`
- **Output:** `1`
- **Explanation:** Delete digit num[0]. The resulting number is "0" which is special since it is divisible by 25.
It can be shown that 1 is the minimum number of operations required to get a special number.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Make a Special Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = "2245047"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Delete digits num[5] and num[6]. The resulting number is "22450" which is special since it is divisible by 25.
It can be shown that 2 is the minimum number of operations required to get a special number.

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
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        ans = n - 1 if '0' in num else n   # reduce to "0" or to empty (= 0)

        for p, q in ("00", "25", "50", "75"):
            j = num.rfind(q)
            if j <= 0:
                continue
            i = num.rfind(p, 0, j)
            if i != -1:
                ans = min(ans, n - i - 2)
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
- [1830. Minimum Number of Operations to Make String Sorted](../../1501-2000/1830-minimum-number-of-operations-to-make-string-sorted/)
- [2009. Minimum Number of Operations to Make Array Continuous](../../2001-2500/2009-minimum-number-of-operations-to-make-array-continuous/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-special-number/)
