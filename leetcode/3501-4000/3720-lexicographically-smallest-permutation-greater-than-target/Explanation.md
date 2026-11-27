# LeetCode 3720: Lexicographically Smallest Permutation Greater Than Target

**LeetCode Problem #3720 — Lexicographically Smallest Permutation Greater Than Target**
Solve LeetCode Lexicographically Smallest Permutation Greater Than Target using C++ and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest Permutation Greater Than Target |
| LeetCode | #3720 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `s` and `target`, both having length `n`, consisting of lowercase English letters.

Return the **lexicographically smallest permutation ** of `s` that is **strictly** greater than `target`. If no permutation of `s` is lexicographically strictly greater than `target`, return an empty string.

A string `a` is **lexicographically strictly greater **than a string `b` (of the same length) if in the first position where `a` and `b` differ, string `a` has a letter that appears later in the alphabet than the corresponding letter in `b`.

## Constraints
- `1 <= s.length == target.length <= 300`
- `s` and `target` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abc", target = "bba"`
- **Output:** `"bca"`
- **Explanation:** The permutations of `s` (in lexicographical order) are `"abc"`, `"acb"`, `"bac"`, `"bca"`, `"cab"`, and `"cba"`. 
 The lexicographically smallest permutation that is strictly greater than `target` is `"bca"`.

### Example 2
- **Input:** `s = "leet", target = "code"`
- **Output:** `"eelt"`
- **Explanation:** The permutations of `s` (in lexicographical order) are `"eelt"`, `"eetl"`, `"elet"`, `"elte"`, `"etel"`, `"etle"`, `"leet"`, `"lete"`, `"ltee"`, `"teel"`, `"tele"`, and `"tlee"`. 
 The lexicographically smallest permutation that is strictly greater than `target` is `"eelt"`.

### Example 3
- **Input:** `s = "baba", target = "bbaa"`
- **Output:** `""`
- **Explanation:** The permutations of `s` (in lexicographical order) are `"aabb"`, `"abab"`, `"abba"`, `"baab"`, `"baba"`, and `"bbaa"`. 
 None of them is lexicographically strictly greater than `target`. Therefore, the answer is `""`.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Lexicographically Smallest Permutation Greater Than Target**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abc", target = "bba"`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"bca"`.
4. **Verification:** The permutations of `s` (in lexicographical order) are `"abc"`, `"acb"`, `"bac"`, `"bca"`, `"cab"`, and `"cba"`. 
 The lexicographically smallest permutation that is strictly greater than `target` is `"bca"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        vector<int> cnt(26, 0);

        for (char c : s) {
            cnt[c - 'a']++;
        }

        string ans;

        // Try to construct a permutation that is
        // strictly greater than target.
        for (int i = 0; i < (int)target.size(); i++) {

            // Try to put target[i] here first.
            int t = target[i] - 'a';

            // Case 1: We can continue equal to target.
            if (cnt[t] > 0) {
                cnt[t]--;
                ans += target[i];
                continue;
            }

            // Case 2: Cannot stay equal.
            // We need a character greater than target[i].
            for (int c = t + 1; c < 26; c++) {
                if (cnt[c] > 0) {
                    ans += char('a' + c);
                    cnt[c]--;

                    // Fill the rest with smallest characters.
                    for (int x = 0; x < 26; x++) {
                        while (cnt[x] > 0) {
                            ans += char('a' + x);
                            cnt[x]--;
                        }
                    }

                    return ans;
                }
            }

            // No greater character at this position.
            // We must backtrack.
            break;
        }

        /*
         * We reached a point where matching target is impossible.
         * Backtrack through ans and find the rightmost position
         * where we can replace the chosen character with something
         * larger.
         */
        for (int i = (int)ans.size() - 1; i >= 0; i--) {
            cnt[ans[i] - 'a']++;

            int cur = ans[i] - 'a';

            for (int c = cur + 1; c < 26; c++) {
                if (cnt[c] > 0) {
                    string res = ans.substr(0, i);
                    res += char('a' + c);
                    cnt[c]--;

                    // Fill remaining positions minimally.
                    for (int x = 0; x < 26; x++) {
                        while (cnt[x] > 0) {
                            res += char('a' + x);
                            cnt[x]--;
                        }
                    }

                    return res;
                }
            }
        }

        return "";
    }
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3734. Lexicographically Smallest Palindromic Permutation Greater Than Target](../../3501-4000/3734-lexicographically-smallest-palindromic-permutation-greater-than-target/)
- [3752. Lexicographically Smallest Negated Permutation that Sums to Target](../../3501-4000/3752-lexicographically-smallest-negated-permutation-that-sums-to-target/)
- [744. Find Smallest Letter Greater Than Target](../../0501-1000/0744-find-smallest-letter-greater-than-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/)
