# LeetCode 3517: Smallest Palindromic Rearrangement I

**LeetCode Problem #3517 — Smallest Palindromic Rearrangement I**
Solve LeetCode Smallest Palindromic Rearrangement I using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Palindromic Rearrangement I |
| LeetCode | #3517 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a ** palindromic ** string `s`.

Return the ** lexicographically smallest ** palindromic permutation of `s`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `s` is guaranteed to be palindromic.

## Examples
### Example 1
- **Input:** `s = "z"`
- **Output:** `"z"`
- **Explanation:** A string of only one character is already the lexicographically smallest palindrome.

### Example 2
- **Input:** `s = "babab"`
- **Output:** `"abbba"`
- **Explanation:** Rearranging `"babab"` &rarr; `"abbba"` gives the smallest lexicographic palindrome.

### Example 3
- **Input:** `s = "daccad"`
- **Output:** `"acddca"`
- **Explanation:** Rearranging `"daccad"` &rarr; `"acddca"` gives the smallest lexicographic palindrome.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Smallest Palindromic Rearrangement I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "z"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"z"`.
4. **Verification:** A string of only one character is already the lexicographically smallest palindrome.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    string smallestPalindrome(string s) {
        vector<int> freq(26, 0);

        for (char c : s) {
            freq[c - 'a']++;
        }

        string left = "";

        for (int i = 0; i < 26; i++) {
            left += string(freq[i] / 2, 'a' + i);
        }

        string right = left;
        reverse(right.begin(), right.end());

        char middle = 0;
        if (s.size() % 2 == 1) {
            for (int i = 0; i < 26; i++) {
                if (freq[i] % 2) {
                    middle = 'a' + i;
                    break;
                }
            }
        }

        return left + (middle ? string(1, middle) : "") + right;
    }
};
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
- [3518. Smallest Palindromic Rearrangement II](../../3501-4000/3813-smallest-palindromic-rearrangement-ii/)
- [3734. Lexicographically Smallest Palindromic Permutation Greater Than Target](../../4001-4500/4037-lexicographically-smallest-palindromic-permutation-greater-than-target/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-i/)
