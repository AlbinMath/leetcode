# LeetCode 1647: Minimum Deletions to Make Character Frequencies Unique

**LeetCode Problem #1647 — Minimum Deletions to Make Character Frequencies Unique**
Solve LeetCode Minimum Deletions to Make Character Frequencies Unique using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Deletions to Make Character Frequencies Unique |
| LeetCode | #1647 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A string `s` is called **good** if there are no two different characters in `s` that have the same **frequency**.

Given a string `s`, return* the **minimum** number of characters you need to delete to make *`s`* **good**.*

The **frequency** of a character in a string is the number of times it appears in the string. For example, in the string `"aab"`, the **frequency** of `'a'` is `2`, while the **frequency** of `'b'` is `1`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aab"`
- **Output:** `0`
- **Explanation:** `s` is already good.

### Example 2
- **Input:** `s = "aaabbbcc"`
- **Output:** `2`
- **Explanation:** You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

### Example 3
- **Input:** `s = "ceabaacb"`
- **Output:** `2`
- **Explanation:** You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Deletions to Make Character Frequencies Unique**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aab"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** `s` is already good.

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
from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = sorted(Counter(s).values(), reverse=True)
        limit = freqs[0]
        deletions = 0

        for f in freqs:
            keep = min(f, limit)
            deletions += f - keep
            limit = max(0, keep - 1)

        return deletions
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
- [3389. Minimum Operations to Make Character Frequencies Equal](../../3501-4000/3638-minimum-operations-to-make-character-frequencies-equal/)
- [1653. Minimum Deletions to Make String Balanced](../../1501-2000/1756-minimum-deletions-to-make-string-balanced/)
- [2216. Minimum Deletions to Make Array Beautiful](../../1001-1500/1355-minimum-deletions-to-make-array-beautiful/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/)
