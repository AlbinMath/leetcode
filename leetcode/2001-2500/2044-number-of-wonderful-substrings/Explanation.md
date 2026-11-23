# LeetCode 1915: Number of Wonderful Substrings

**LeetCode Problem #1915 — Number of Wonderful Substrings**
Solve LeetCode Number of Wonderful Substrings using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Wonderful Substrings |
| LeetCode | #1915 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A **wonderful** string is a string where **at most one** letter appears an **odd** number of times.

For example, `"ccjjc"` and `"abab"` are wonderful, but `"ab"` is not.

Given a string `word` that consists of the first ten lowercase English letters (`'a'` through `'j'`), return *the **number of wonderful non-empty substrings** in *`word`*. If the same substring appears multiple times in *`word`*, then count **each occurrence** separately.*

A **substring** is a contiguous sequence of characters in a string.

## Constraints
- `1 <= word.length <= 10^5`
- `word` consists of lowercase English letters from `'a'` to `'j'`.

## Examples
### Example 1
- **Input:** `word = "aba"`
- **Output:** `4`
- **Explanation:** The four wonderful substrings are underlined below:
- "

### Example 2
- **Input:** `word = "aabb"`
- **Output:** `9`
- **Explanation:** The nine wonderful substrings are underlined below:
- "

### Example 3
- **Input:** `word = "he"`
- **Output:** `2`
- **Explanation:** The two wonderful substrings are underlined below:
- " h e" -> "h"
- "h

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Wonderful Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "aba"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The four wonderful substrings are underlined below:
- "

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:

  def wonderfulSubstrings(self, word: str) -> int:
    count = [0] * 1024
    count[0] = 1
    mask = 0
    ans = 0

    for ch in word:
      mask ^= 1 << (ord(ch) - ord('a'))
      # Case 1: All characters have even frequencies
      ans += count[mask]
      # Case 2: Exactly one character has an odd frequency
      for bit in range(10):
        ans += count[mask ^ (1 << bit)]
      count[mask] += 1

    return ans
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1358. Number of Substrings Containing All Three Characters](../../1001-1500/1460-number-of-substrings-containing-all-three-characters/)
- [1513. Number of Substrings With Only 1s](../../1501-2000/1636-number-of-substrings-with-only-1s/)
- [1520. Maximum Number of Non-Overlapping Substrings](../../1501-2000/1644-maximum-number-of-non-overlapping-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-wonderful-substrings/)
