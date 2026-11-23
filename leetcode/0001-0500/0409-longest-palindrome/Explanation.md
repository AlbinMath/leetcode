# LeetCode 409: Longest Palindrome

**LeetCode Problem #409 — Longest Palindrome**
Solve LeetCode Longest Palindrome using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Palindrome |
| LeetCode | #409 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest palindrome ** that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome.

## Constraints
- `1 <= s.length <= 2000`
- `s` consists of lowercase **and/or** uppercase English letters only.

## Examples
### Example 1
- **Input:** `s = "abccccdd"`
- **Output:** `7`
- **Explanation:** One longest palindrome that can be built is "dccaccd", whose length is 7.

### Example 2
- **Input:** `s = "a"`
- **Output:** `1`
- **Explanation:** The longest palindrome that can be built is "a", whose length is 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Palindrome**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abccccdd"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** One longest palindrome that can be built is "dccaccd", whose length is 7.

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
class Solution:
    def longestPalindrome(self, s):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        length = 0
        has_odd = False

        for value in count.values():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                has_odd = True

        if has_odd:
            length += 1

        return length
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
- [1147. Longest Chunked Palindrome Decomposition](../../1001-1500/1251-longest-chunked-palindrome-decomposition/)
- [2131. Longest Palindrome by Concatenating Two Letter Words](../../2001-2500/2237-longest-palindrome-by-concatenating-two-letter-words/)
- [3503. Longest Palindrome After Substring Concatenation I](../../3501-4000/3793-longest-palindrome-after-substring-concatenation-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-palindrome/)
