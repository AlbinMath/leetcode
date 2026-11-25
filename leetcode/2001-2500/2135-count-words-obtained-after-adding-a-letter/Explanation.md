# LeetCode 2135: Count Words Obtained After Adding a Letter

**LeetCode Problem #2135 — Count Words Obtained After Adding a Letter**
Solve LeetCode Count Words Obtained After Adding a Letter using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Words Obtained After Adding a Letter |
| LeetCode | #2135 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** arrays of strings `startWords` and `targetWords`. Each string consists of **lowercase English letters** only.

For each string in `targetWords`, check if it is possible to choose a string from `startWords` and perform a **conversion operation** on it to be equal to that from `targetWords`.

The **conversion operation** is described in the following two steps:

**Append** any lowercase letter that is **not present** in the string to its end.

For example, if the string is `"abc"`, the letters `'d'`, `'e'`, or `'y'` can be added to it, but not `'a'`. If `'d'` is added, the resulting string will be `"abcd"`. 
 
 
 **Rearrange** the letters of the new string in **any** arbitrary order.
 
 For example, `"abcd"` can be rearranged to `"acbd"`, `"bacd"`, `"cbda"`, and so on. Note that it can also be rearranged to `"abcd"` itself.

Return *the **number of strings** in *`targetWords`* that can be obtained by performing the operations on **any** string of *`startWords`.

**Note** that you will only be verifying if the string in `targetWords` can be obtained from a string in `startWords` by performing the operations. The strings in `startWords` **do not** actually change during this process.

## Constraints
- `1 <= startWords.length, targetWords.length <= 5 * 10^4`
- `1 <= startWords[i].length, targetWords[j].length <= 26`
- Each string of `startWords` and `targetWords` consists of lowercase English letters only.
- No letter occurs more than once in any string of `startWords` or `targetWords`.

## Examples
### Example 1
- **Input:** `startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]`
- **Output:** `2`
- **Explanation:** - In order to form targetWords[0] = "tack", we use startWords[1] = "act", append 'k' to it, and rearrange "actk" to "tack".
- There is no string in startWords that can be used to obtain targetWords[1] = "act".
 Note that "act" does exist in startWords, but we

### Example 2
- **Input:** `startWords = ["ab","a"], targetWords = ["abc","abcd"]`
- **Output:** `1`
- **Explanation:** - In order to form targetWords[0] = "abc", we use startWords[0] = "ab", add 'c' to it, and rearrange it to "abc".
- There is no string in startWords that can be used to obtain targetWords[1] = "abcd".

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Words Obtained After Adding a Letter**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** - In order to form targetWords[0] = "tack", we use startWords[1] = "act", append 'k' to it, and rearrange "actk" to "tack".
- There is no string in startWords that can be used to obtain targetWords[1] = "act".
 Note that "act" does exist in startWords, but we

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
from typing import List


class Solution:

  def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
    def get_mask(word: str) -> int:
      mask = 0
      for ch in word:
        mask |= 1 << (ord(ch) - ord('a'))
      return mask

    # Step 1: Store bitmasks of all startWords
    start_masks = {get_mask(w) for w in startWords}

    # Step 2: For each targetWord, try removing one character at a time
    ans = 0
    for w in targetWords:
      t_mask = get_mask(w)
      for ch in w:
        candidate = t_mask ^ (1 << (ord(ch) - ord('a')))
        if candidate in start_masks:
          ans += 1
          break

    return ans
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
- [2131. Longest Palindrome by Concatenating Two Letter Words](../../2001-2500/2131-longest-palindrome-by-concatenating-two-letter-words/)
- [2085. Count Common Words With One Occurrence](../../2001-2500/2085-count-common-words-with-one-occurrence/)
- [3775. Reverse Words With Same Vowel Count](../../3501-4000/3775-reverse-words-with-same-vowel-count/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/)
