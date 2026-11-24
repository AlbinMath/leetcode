# LeetCode 1400: Construct K Palindrome Strings

**LeetCode Problem #1400 — Construct K Palindrome Strings**
Solve LeetCode Construct K Palindrome Strings using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct K Palindrome Strings |
| LeetCode | #1400 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` and an integer `k`, return `true` if you can use all the characters in `s` to construct **non-empty** `k` palindrome strings or `false` otherwise.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `s = "annabelle", k = 2`
- **Output:** `true`
- **Explanation:** You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

### Example 2
- **Input:** `s = "leetcode", k = 3`
- **Output:** `false`
- **Explanation:** It is impossible to construct 3 palindromes using all the characters of s.

### Example 3
- **Input:** `s = "true", k = 4`
- **Output:** `true`
- **Explanation:** The only possible solution is to put each character in a separate string.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Construct K Palindrome Strings**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "annabelle", k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        odd = sum(v % 2 for v in Counter(s).values())
        return odd <= k
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1616. Split Two Strings to Make Palindrome](../../1501-2000/1739-split-two-strings-to-make-palindrome/)
- [3260. Find the Largest Palindrome Divisible by K](../../3501-4000/3552-find-the-largest-palindrome-divisible-by-k/)
- [854. K-Similar Strings](../../0501-1000/0884-k-similar-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-k-palindrome-strings/)
