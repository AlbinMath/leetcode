# LeetCode 2522: Partition String Into Substrings With Values at Most K

**LeetCode Problem #2522 — Partition String Into Substrings With Values at Most K**
Solve LeetCode Partition String Into Substrings With Values at Most K using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition String Into Substrings With Values at Most K |
| LeetCode | #2522 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of digits from `1` to `9` and an integer `k`.

A partition of a string `s` is called **good** if:

Each digit of `s` is part of **exactly** one substring. 
 The value of each substring is less than or equal to `k`.

Return *the **minimum** number of substrings in a **good** partition of* `s`. If no **good** partition of `s` exists, return `-1`.

Note that:

The **value** of a string is its result when interpreted as an integer. For example, the value of `"123"` is `123` and the value of `"1"` is `1`. 
 A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is a digit from `'1'` to `'9'`.
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `s = "165462", k = 60`
- **Output:** `4`
- **Explanation:** We can partition the string into substrings "16", "54", "6", and "2". Each substring has a value less than or equal to k = 60.
It can be shown that we cannot partition the string into less than 4 substrings.

### Example 2
- **Input:** `s = "238182", k = 5`
- **Output:** `-1`
- **Explanation:** There is no good partition for this string.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Partition String Into Substrings With Values at Most K**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "165462", k = 60`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can partition the string into substrings "16", "54", "6", and "2". Each substring has a value less than or equal to k = 60.
It can be shown that we cannot partition the string into less than 4 substrings.

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
    def minimumPartition(self, s: str, k: int) -> int:
        count = 1
        cur = 0
        for ch in s:
            d = int(ch)
            if d > k:
                return -1
            if cur * 10 + d <= k:
                cur = cur * 10 + d
            else:
                count += 1
                cur = d
        return count
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
- [2767. Partition String Into Minimum Beautiful Substrings](../../2501-3000/2767-partition-string-into-minimum-beautiful-substrings/)
- [2138. Divide a String Into Groups of Size k](../../2001-2500/2138-divide-a-string-into-groups-of-size-k/)
- [3365. Rearrange K Substrings to Form Target String](../../3001-3500/3365-rearrange-k-substrings-to-form-target-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/)
