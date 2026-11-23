# LeetCode 395: Longest Substring with At Least K Repeating Characters

**LeetCode Problem #395 — Longest Substring with At Least K Repeating Characters**
Solve LeetCode Longest Substring with At Least K Repeating Characters using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Substring with At Least K Repeating Characters |
| LeetCode | #395 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` and an integer `k`, return *the length of the longest substring of* `s` *such that the frequency of each character in this substring is greater than or equal to* `k`.

if no such substring exists, return 0.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of only lowercase English letters.
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `s = "aaabb", k = 3`
- **Output:** `3`
- **Explanation:** The longest substring is "aaa", as 'a' is repeated 3 times.

### Example 2
- **Input:** `s = "ababbc", k = 2`
- **Output:** `5`
- **Explanation:** The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Longest Substring with At Least K Repeating Characters**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aaabb", k = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The longest substring is "aaa", as 'a' is repeated 3 times.

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
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        best = 0

        for t in range(1, 27):
            cnt = [0] * 26
            distinct = at_least_k = 0
            left = 0

            for right in range(n):
                r = ord(s[right]) - 97
                if cnt[r] == 0:
                    distinct += 1
                cnt[r] += 1
                if cnt[r] == k:
                    at_least_k += 1

                while distinct > t:
                    l = ord(s[left]) - 97
                    if cnt[l] == k:
                        at_least_k -= 1
                    cnt[l] -= 1
                    if cnt[l] == 0:
                        distinct -= 1
                    left += 1

                if distinct == t and at_least_k == t:
                    best = max(best, right - left + 1)

        return best
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
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [2213. Longest Substring of One Repeating Character](../../2001-2500/2319-longest-substring-of-one-repeating-character/)
- [424. Longest Repeating Character Replacement](../../0001-0500/0424-longest-repeating-character-replacement/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)
