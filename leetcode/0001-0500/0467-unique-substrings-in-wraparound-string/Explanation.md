# LeetCode 467: Unique Substrings in Wraparound String

**LeetCode Problem #467 — Unique Substrings in Wraparound String**
Solve LeetCode Unique Substrings in Wraparound String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unique Substrings in Wraparound String |
| LeetCode | #467 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We define the string `base` to be the infinite wraparound string of `"abcdefghijklmnopqrstuvwxyz"`, so `base` will look like this:

`"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...."`.

Given a string `s`, return *the number of **unique non-empty substrings** of *`s`* are present in *`base`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "a"`
- **Output:** `1`
- **Explanation:** Only the substring "a" of s is in base.

### Example 2
- **Input:** `s = "cac"`
- **Output:** `2`
- **Explanation:** There are two substrings ("a", "c") of s in base.

### Example 3
- **Input:** `s = "zab"`
- **Output:** `6`
- **Explanation:** There are six substrings ("z", "a", "b", "za", "ab", and "zab") of s in base.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Unique Substrings in Wraparound String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "a"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Only the substring "a" of s is in base.

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
    def findSubstringInWraproundString(self, s: str) -> int:
        best = [0] * 26
        length = 0

        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                length += 1
            else:
                length = 1
            idx = ord(ch) - ord('a')
            best[idx] = max(best[idx], length)

        return sum(best)
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
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1593-split-a-string-into-the-max-number-of-unique-substrings/)
- [1016. Binary String With Substrings Representing 1 To N](../../1001-1500/1016-binary-string-with-substrings-representing-1-to-n/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/unique-substrings-in-wraparound-string/)
