# LeetCode 2272: Substring With Largest Variance

**LeetCode Problem #2272 — Substring With Largest Variance**
Solve LeetCode Substring With Largest Variance using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Substring With Largest Variance |
| LeetCode | #2272 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
The **variance** of a string is defined as the largest difference between the number of occurrences of **any** `2` characters present in the string. Note the two characters may or may not be the same.

Given a string `s` consisting of lowercase English letters only, return *the **largest variance** possible among all **substrings** of* `s`.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aababbb"`
- **Output:** `3`
- **Explanation:** All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.

### Example 2
- **Input:** `s = "abcde"`
- **Output:** `0`
- **Explanation:** No letter occurs more than once in s, so the variance of every substring is 0.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Substring With Largest Variance**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aababbb"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.

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
from collections import defaultdict

class Solution(object):
    def largestVariance(self, s):
        indices = defaultdict(list)
        for i, ch in enumerate(s):
            indices[ch].append(i)

        chars = list(indices.keys())
        max_var = 0

        for major in chars:
            for minor in chars:
                if major == minor:
                    continue

                pos_maj = indices[major]
                pos_min = indices[minor]
                rest_minor = len(pos_min)
                major_count = 0
                minor_count = 0

                i = j = 0
                while i < len(pos_maj) and j < len(pos_min):
                    if pos_maj[i] < pos_min[j]:
                        major_count += 1
                        i += 1
                    else:
                        minor_count += 1
                        rest_minor -= 1
                        j += 1

                    if minor_count > 0:
                        max_var = max(max_var, major_count - minor_count)

                    if major_count < minor_count and rest_minor > 0:
                        major_count = 0
                        minor_count = 0

                # Case 1: Trailing 'major' characters after all 'minor' characters were processed
                if minor_count > 0 and i < len(pos_maj):
                    major_count += len(pos_maj) - i
                    max_var = max(max_var, major_count - minor_count)

                # Case 2: All 'major' characters appeared before a remaining 'minor' (e.g., "bbc")
                if minor_count == 0 and j < len(pos_min):
                    max_var = max(max_var, major_count - 1)

        return max_var
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
- [1624. Largest Substring Between Two Equal Characters](../../1501-2000/1624-largest-substring-between-two-equal-characters/)
- [1946. Largest Number After Mutating Substring](../../1501-2000/1946-largest-number-after-mutating-substring/)
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/substring-with-largest-variance/)
