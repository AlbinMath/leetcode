# LeetCode 820: Short Encoding of Words

**LeetCode Problem #820 — Short Encoding of Words**
Solve LeetCode Short Encoding of Words using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Short Encoding of Words |
| LeetCode | #820 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **valid encoding** of an array of `words` is any reference string `s` and array of indices `indices` such that:

`words.length == indices.length` 
 The reference string `s` ends with the `'#'` character. 
 For each index `indices[i]`, the **substring** of `s` starting from `indices[i]` and up to (but not including) the next `'#'` character is equal to `words[i]`.

Given an array of `words`, return *the **length of the shortest reference string** *`s`* possible of any **valid encoding** of *`words`*.*

## Constraints
- `1 <= words.length <= 2000`
- `1 <= words[i].length <= 7`
- `words[i]` consists of only lowercase letters.

## Examples
### Example 1
- **Input:** `words = ["time", "me", "bell"]`
- **Output:** `10`
- **Explanation:** A valid encoding would be s = `"time#bell#" and indices = [0, 2, 5`].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in " time #bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "ti me #bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time# bell #"

### Example 2
- **Input:** `words = ["t"]`
- **Output:** `2`
- **Explanation:** A valid encoding would be s = "t#" and indices = [0].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Short Encoding of Words**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["time", "me", "bell"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** A valid encoding would be s = `"time#bell#" and indices = [0, 2, 5`].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in " time #bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "ti me #bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time# bell #"

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
from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        keep = set(words)
        for w in words:
            for i in range(1, len(w)):
                keep.discard(w[i:])
        return sum(len(w) + 1 for w in keep)
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
- [30. Substring with Concatenation of All Words](../../0001-0500/0030-substring-with-concatenation-of-all-words/)
- [151. Reverse Words in a String](../../0001-0500/0151-reverse-words-in-a-string/)
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/short-encoding-of-words/)
