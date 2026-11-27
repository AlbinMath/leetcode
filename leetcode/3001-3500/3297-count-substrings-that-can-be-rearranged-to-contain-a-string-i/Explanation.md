# LeetCode 3297: Count Substrings That Can Be Rearranged to Contain a String I

**LeetCode Problem #3297 — Count Substrings That Can Be Rearranged to Contain a String I**
Solve LeetCode Count Substrings That Can Be Rearranged to Contain a String I using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Substrings That Can Be Rearranged to Contain a String I |
| LeetCode | #3297 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `word1` and `word2`.

A string `x` is called **valid** if `x` can be rearranged to have `word2` as a prefix .

Return the total number of **valid** substrings of `word1`.

## Constraints
- `1 <= word1.length <= 10^5`
- `1 <= word2.length <= 10^4`
- `word1` and `word2` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `word1 = "bcca", word2 = "abc"`
- **Output:** `1`
- **Explanation:** The only valid substring is `"bcca"` which can be rearranged to `"abcc"` having `"abc"` as a prefix.

### Example 2
- **Input:** `word1 = "abcabc", word2 = "abc"`
- **Output:** `10`
- **Explanation:** All the substrings except substrings of size 1 and size 2 are valid.

### Example 3
- **Input:** `word1 = "abcabc", word2 = "aaabc"`
- **Output:** `0`

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Count Substrings That Can Be Rearranged to Contain a String I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word1 = "bcca", word2 = "abc"`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The only valid substring is `"bcca"` which can be rearranged to `"abcc"` having `"abc"` as a prefix.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        need = [0] * 26
        for ch in word2:
            need[ord(ch) - 97] += 1
        missing = sum(1 for x in need if x > 0)

        cnt = [0] * 26
        ans = 0
        r = 0  # window is [l, r)
        for l in range(n):
            while r < n and missing > 0:
                c = ord(word1[r]) - 97
                cnt[c] += 1
                if need[c] > 0 and cnt[c] == need[c]:
                    missing -= 1
                r += 1
            if missing == 0:
                ans += n - r + 1
            # remove word1[l]
            c = ord(word1[l]) - 97
            if need[c] > 0 and cnt[c] == need[c]:
                missing += 1
            cnt[c] -= 1
        return ans
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [3298. Count Substrings That Can Be Rearranged to Contain a String II](../../3001-3500/3298-count-substrings-that-can-be-rearranged-to-contain-a-string-ii/)
- [2930. Number of Strings Which Can Be Rearranged to Contain Substring](../../2501-3000/2930-number-of-strings-which-can-be-rearranged-to-contain-substring/)
- [2201. Count Artifacts That Can Be Extracted](../../2001-2500/2201-count-artifacts-that-can-be-extracted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/)
