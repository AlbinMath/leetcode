# LeetCode 3306: Count of Substrings Containing Every Vowel and K Consonants II

**LeetCode Problem #3306 — Count of Substrings Containing Every Vowel and K Consonants II**
Solve LeetCode Count of Substrings Containing Every Vowel and K Consonants II using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count of Substrings Containing Every Vowel and K Consonants II |
| LeetCode | #3306 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `word` and a **non-negative** integer `k`.

Return the total number of substrings of `word` that contain every vowel (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) **at least** once and **exactly** `k` consonants.

## Constraints
- `5 <= word.length <= 2 * 10^5`
- `word` consists only of lowercase English letters.
- `0 <= k <= word.length - 5`

## Examples
### Example 1
- **Input:** `word = "aeioqq", k = 1`
- **Output:** `0`
- **Explanation:** There is no substring with every vowel.

### Example 2
- **Input:** `word = "aeiou", k = 0`
- **Output:** `1`
- **Explanation:** The only substring with every vowel and zero consonants is `word[0..4]`, which is `"aeiou"`.

### Example 3
- **Input:** `word = " ieaouqqieaouqq ", k = 1`
- **Output:** `3`
- **Explanation:** The substrings with every vowel and one consonant are: 

 
 `word[0..5]`, which is `"ieaouq"`. 
 `word[6..11]`, which is `"qieaou"`. 
 `word[7..12]`, which is `"ieaouq"`.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Count of Substrings Containing Every Vowel and K Consonants II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "aeioqq", k = 1`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** There is no substring with every vowel.

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
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        def at_least(m: int) -> int:
            cnt = [0] * 5
            have = 0       # distinct vowels in window
            cons = 0       # consonants in window
            r = 0          # window is [l, r)
            res = 0
            for l in range(n):
                while r < n and (have < 5 or cons < m):
                    ch = word[r]
                    if ch in idx:
                        v = idx[ch]
                        if cnt[v] == 0:
                            have += 1
                        cnt[v] += 1
                    else:
                        cons += 1
                    r += 1
                if have == 5 and cons >= m:
                    res += n - r + 1
                else:
                    break
                ch = word[l]
                if ch in idx:
                    v = idx[ch]
                    cnt[v] -= 1
                    if cnt[v] == 0:
                        have -= 1
                else:
                    cons -= 1
            return res

        return at_least(k) - at_least(k + 1)
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
- [3305. Count of Substrings Containing Every Vowel and K Consonants I](../../3001-3500/3305-count-of-substrings-containing-every-vowel-and-k-consonants-i/)
- [3258. Count Substrings That Satisfy K-Constraint I](../../3001-3500/3258-count-substrings-that-satisfy-k-constraint-i/)
- [3261. Count Substrings That Satisfy K-Constraint II](../../3001-3500/3261-count-substrings-that-satisfy-k-constraint-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/)
