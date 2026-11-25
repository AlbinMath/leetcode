# LeetCode 1160: Find Words That Can Be Formed by Characters

**LeetCode Problem #1160 — Find Words That Can Be Formed by Characters**
Solve LeetCode Find Words That Can Be Formed by Characters using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Words That Can Be Formed by Characters |
| LeetCode | #1160 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of strings `words` and a string `chars`.

A string is **good** if it can be formed by characters from `chars` (each character can only be used once for **each** word in `words`).

Return *the sum of lengths of all good strings in words*.

## Constraints
- `1 <= words.length <= 1000`
- `1 <= words[i].length, chars.length <= 100`
- `words[i]` and `chars` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["cat","bt","hat","tree"], chars = "atach"`
- **Output:** `6`
- **Explanation:** The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

### Example 2
- **Input:** `words = ["hello","world","leetcode"], chars = "welldonehoneyr"`
- **Output:** `10`
- **Explanation:** The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find Words That Can Be Formed by Characters**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["cat","bt","hat","tree"], chars = "atach"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

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
from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0

        for word in words:
            word_count = Counter(word)

            if all(word_count[c] <= char_count[c] for c in word_count):
                total += len(word)

        return total
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
- [1751. Maximum Number of Events That Can Be Attended II](../../1501-2000/1751-maximum-number-of-events-that-can-be-attended-ii/)
- [2201. Count Artifacts That Can Be Extracted](../../2001-2500/2201-count-artifacts-that-can-be-extracted/)
- [3011. Find if Array Can Be Sorted](../../3001-3500/3011-find-if-array-can-be-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)
