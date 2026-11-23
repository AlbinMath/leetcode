# LeetCode 3734: Lexicographically Smallest Palindromic Permutation Greater Than Target

**LeetCode Problem #3734 — Lexicographically Smallest Palindromic Permutation Greater Than Target**
Solve LeetCode Lexicographically Smallest Palindromic Permutation Greater Than Target using Java and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest Palindromic Permutation Greater Than Target |
| LeetCode | #3734 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `s` and `target`, each of length `n`, consisting of lowercase English letters.

Return the ** lexicographically smallest string** that is **both** a ** palindromic permutation ** of `s` and **strictly** greater than `target`. If no such permutation exists, return an empty string.

## Constraints
- `1 <= n == s.length == target.length <= 300`
- `s` and `target` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "baba", target = "abba"`
- **Output:** `"baab"`
- **Explanation:** The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`. 
 The lexicographically smallest permutation that is strictly greater than `target` is `"baab"`.

### Example 2
- **Input:** `s = "baba", target = "bbaa"`
- **Output:** `""`
- **Explanation:** The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`. 
 None of them is lexicographically strictly greater than `target`. Therefore, the answer is `""`.

### Example 3
- **Input:** `s = "abc", target = "abb"`
- **Output:** `""`
- **Explanation:** `s` has no palindromic permutations. Therefore, the answer is `""`.

### Example 4
- **Input:** `s = "aac", target = "abb"`
- **Output:** `"aca"`
- **Explanation:** The only palindromic permutation of `s` is `"aca"`. 
 `"aca"` is strictly greater than `target`. Therefore, the answer is `"aca"`.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Lexicographically Smallest Palindromic Permutation Greater Than Target**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "baba", target = "abba"`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"baab"`.
4. **Verification:** The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`. 
 The lexicographically smallest permutation that is strictly greater than `target` is `"baab"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public String lexPalindromicPermutation(String s, String target) {
        int n = s.length();

        // Count characters
        int[] freq = new int[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        // A palindrome can have at most one character with odd frequency
        int odd = -1;
        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 == 1) {
                if (odd != -1) {
                    return "";
                }
                odd = i;
            }
        }

        char middle = odd == -1 ? 0 : (char) ('a' + odd);

        // Frequencies for the first half
        int[] halfFreq = new int[26];
        int halfLen = 0;

        for (int i = 0; i < 26; i++) {
            halfFreq[i] = freq[i] / 2;
            halfLen += halfFreq[i];
        }

        String bound = target.substring(0, halfLen);

        // Try to make the first half exactly equal to target's first half
        int[] remaining = halfFreq.clone();
        boolean possible = true;

        for (int i = 0; i < halfLen; i++) {
            int x = bound.charAt(i) - 'a';

            if (remaining[x] == 0) {
                possible = false;
                break;
            }

            remaining[x]--;
        }

        // If exact half is possible, check its palindrome
        if (possible) {
            String half = bound;
            String palindrome = makePalindrome(half, middle);

            if (palindrome.compareTo(target) > 0) {
                return palindrome;
            }

            // Need the next permutation of the half
            char[] arr = half.toCharArray();

            int i = arr.length - 2;
            while (i >= 0 && arr[i] >= arr[i + 1]) {
                i--;
            }

            if (i < 0) {
                return "";
            }

            int j = arr.length - 1;
            while (arr[j] <= arr[i]) {
                j--;
            }

            char temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

            reverse(arr, i + 1, arr.length - 1);

            return makePalindrome(new String(arr), middle);
        }

        /*
         * Exact target prefix is impossible.
         * Find the smallest half that is lexicographically greater
         * than target.substring(0, halfLen).
         */

        remaining = halfFreq.clone();

        // states[i] = remaining frequencies after matching first i chars
        int[][] states = new int[halfLen + 1][26];

        int matched = 0;

        for (int i = 0; i < halfLen; i++) {
            states[i] = remaining.clone();

            int x = bound.charAt(i) - 'a';

            if (remaining[x] == 0) {
                break;
            }

            remaining[x]--;
            matched++;
        }

        states[matched] = remaining.clone();

        // Work backwards to find the rightmost position we can increase
        for (int pos = matched; pos >= 0; pos--) {
            if (pos >= halfLen) {
                continue;
            }

            remaining = states[pos].clone();

            int current = bound.charAt(pos) - 'a';

            // Choose the smallest available character greater than target[pos]
            for (int c = current + 1; c < 26; c++) {
                if (remaining[c] > 0) {
                    remaining[c]--;

                    StringBuilder half = new StringBuilder();
                    half.append(bound, 0, pos);
                    half.append((char) ('a' + c));

                    // Fill remaining positions with smallest characters
                    for (int k = 0; k < 26; k++) {
                        while (remaining[k] > 0) {
                            half.append((char) ('a' + k));
                            remaining[k]--;
                        }
                    }

                    return makePalindrome(half.toString(), middle);
                }
            }
        }

        return "";
    }

    private String makePalindrome(String half, char middle) {
        StringBuilder result = new StringBuilder();

        result.append(half);

        if (middle != 0) {
            result.append(middle);
        }

        result.append(new StringBuilder(half).reverse());

        return result.toString();
    }

    private void reverse(char[] arr, int left, int right) {
        while (left < right) {
            char temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
}
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
- [3720. Lexicographically Smallest Permutation Greater Than Target](../../4001-4500/4020-lexicographically-smallest-permutation-greater-than-target/)
- [744. Find Smallest Letter Greater Than Target](../../0501-1000/0745-find-smallest-letter-greater-than-target/)
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../../3001-3500/3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/)
