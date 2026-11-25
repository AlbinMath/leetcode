# LeetCode 2131: Longest Palindrome by Concatenating Two Letter Words

**LeetCode Problem #2131 — Longest Palindrome by Concatenating Two Letter Words**
Solve LeetCode Longest Palindrome by Concatenating Two Letter Words using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Palindrome by Concatenating Two Letter Words |
| LeetCode | #2131 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of strings `words`. Each element of `words` consists of **two** lowercase English letters.

Create the **longest possible palindrome** by selecting some elements from `words` and concatenating them in **any order**. Each element can be selected **at most once**.

Return *the **length** of the longest palindrome that you can create*. If it is impossible to create any palindrome, return `0`.

A **palindrome** is a string that reads the same forward and backward.

## Constraints
- `1 <= words.length <= 10^5`
- `words[i].length == 2`
- `words[i]` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["lc","cl","gg"]`
- **Output:** `6`
- **Explanation:** One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

### Example 2
- **Input:** `words = ["ab","ty","yt","lc","cl","ab"]`
- **Output:** `8`
- **Explanation:** One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

### Example 3
- **Input:** `words = ["cc","ll","xx"]`
- **Output:** `2`
- **Explanation:** One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Palindrome by Concatenating Two Letter Words**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["lc","cl","gg"]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

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
from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        unpaired = defaultdict(int)
        length = 0
        sym_unpaired = 0
        
        for word in words:
            rev = word[1] + word[0]
            if unpaired[rev] > 0:
                unpaired[rev] -= 1
                length += 4
                if word == rev:
                    sym_unpaired -= 1
            else:
                unpaired[word] += 1
                if word == rev:
                    sym_unpaired += 1
                    
        if sym_unpaired > 0:
            length += 2
            
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
- [409. Longest Palindrome](../../0001-0500/0409-longest-palindrome/)
- [1147. Longest Chunked Palindrome Decomposition](../../1001-1500/1147-longest-chunked-palindrome-decomposition/)
- [3503. Longest Palindrome After Substring Concatenation I](../../3501-4000/3503-longest-palindrome-after-substring-concatenation-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/)
