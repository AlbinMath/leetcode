# LeetCode 1540: Can Convert String in K Moves

**LeetCode Problem #1540 — Can Convert String in K Moves**
Solve LeetCode Can Convert String in K Moves using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Can Convert String in K Moves |
| LeetCode | #1540 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings `s` and `t`, your goal is to convert `s` into `t` in `k`** **moves or less.

During the `i^th` ( `1 <= i <= k`) move you can:

Choose any index `j` (1-indexed) from `s`, such that `1 <= j <= s.length` and `j` has not been chosen in any previous move, and shift the character at that index `i` times. 
 Do nothing.

Shifting a character means replacing it by the next letter in the alphabet (wrapping around so that `'z'` becomes `'a'`). Shifting a character by `i` means applying the shift operations `i` times.

Remember that any index `j` can be picked at most once.

Return `true` if it's possible to convert `s` into `t` in no more than `k` moves, otherwise return `false`.

## Constraints
- `1 <= s.length, t.length <= 10^5`
- `0 <= k <= 10^9`
- `s`, `t` contain only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "input", t = "ouput", k = 9`
- **Output:** `true`

### Example 2
- **Input:** `s = "abc", t = "bcd", k = 10`
- **Output:** `false`
- **Explanation:** We need to shift each character in s one time to convert it into t. We can shift 'a' to 'b' during the 1st move. However, there is no way to shift the other characters in the remaining moves to obtain t from s.

### Example 3
- **Input:** `s = "aab", t = "bbb", k = 27`
- **Output:** `true`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Can Convert String in K Moves**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "input", t = "ouput", k = 9`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for a, b in zip(s, t):
            d = (ord(b) - ord(a)) % 26
            if d == 0:
                continue
            # the (count[d]+1)-th index needing shift d uses move d + 26 * count[d]
            if d + 26 * count[d] > k:
                return False
            count[d] += 1

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
- [2027. Minimum Moves to Convert String](../../2001-2500/2027-minimum-moves-to-convert-string/)
- [3086. Minimum Moves to Pick K Ones](../../3001-3500/3086-minimum-moves-to-pick-k-ones/)
- [1945. Sum of Digits of String After Convert](../../1501-2000/1945-sum-of-digits-of-string-after-convert/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/can-convert-string-in-k-moves/)
