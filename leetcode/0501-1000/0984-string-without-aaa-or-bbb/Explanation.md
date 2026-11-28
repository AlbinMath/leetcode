# LeetCode 984: String Without AAA or BBB

**LeetCode Problem #984 — String Without AAA or BBB**
Solve LeetCode String Without AAA or BBB using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | String Without AAA or BBB |
| LeetCode | #984 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers `a` and `b`, return **any** string `s` such that:

`s` has length `a + b` and contains exactly `a` `'a'` letters, and exactly `b` `'b'` letters, 
 The substring `'aaa'` does not occur in `s`, and 
 The substring `'bbb'` does not occur in `s`.

## Constraints
- `0 <= a, b <= 100`
- It is guaranteed such an `s` exists for the given `a` and `b`.

## Examples
### Example 1
- **Input:** `a = 1, b = 2`
- **Output:** `"abb"`
- **Explanation:** "abb", "bab" and "bba" are all correct answers.

### Example 2
- **Input:** `a = 4, b = 1`
- **Output:** `"aabaa"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **String Without AAA or BBB**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = 1, b = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"abb"`.
4. **Verification:** "abb", "bab" and "bba" are all correct answers.

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
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []

        while a > 0 or b > 0:
            # Would adding 'a' create "aaa"?
            if len(res) >= 2 and res[-1] == res[-2]:
                write_a = res[-1] == 'b'   # last two are equal: pick the other letter
            else:
                write_a = a >= b           # otherwise take the larger pile

            if write_a:
                res.append('a')
                a -= 1
            else:
                res.append('b')
                b -= 1

        return ''.join(res)
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
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [600. Non-negative Integers without Consecutive Ones](../../0501-1000/0600-non-negative-integers-without-consecutive-ones/)
- [2274. Maximum Consecutive Floors Without Special Floors](../../2001-2500/2274-maximum-consecutive-floors-without-special-floors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/string-without-aaa-or-bbb/)
