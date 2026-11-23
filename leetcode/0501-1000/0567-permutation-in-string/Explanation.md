# LeetCode 567: Permutation in String

**LeetCode Problem #567 — Permutation in String**
Solve LeetCode Permutation in String using C++ and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Permutation in String |
| LeetCode | #567 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

## Constraints
- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s1 = "ab", s2 = "eidbaooo"`
- **Output:** `true`
- **Explanation:** s2 contains one permutation of s1 ("ba").

### Example 2
- **Input:** `s1 = "ab", s2 = "eidboaoo"`
- **Output:** `false`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Permutation in String**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s1 = "ab", s2 = "eidbaooo"`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** s2 contains one permutation of s1 ("ba").

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
#include <string>
using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = s1.length(), n2 = s2.length();
        if (n1 > n2) return false;
        
        int cnt1[26] = {0}, cnt2[26] = {0};
        for (int i = 0; i < n1; ++i) {
            cnt1[s1[i] - 'a']++;
            cnt2[s2[i] - 'a']++;
        }
        
        int matches = 0;
        for (int c = 0; c < 26; ++c) {
            if (cnt1[c] == cnt2[c]) matches++;
        }
        if (matches == 26) return true;
        
        for (int i = n1; i < n2; ++i) {
            int r = s2[i] - 'a';       // Incoming right character
            int l = s2[i - n1] - 'a';  // Outgoing left character
            
            if (cnt2[r] == cnt1[r]) matches--;
            cnt2[r]++;
            if (cnt2[r] == cnt1[r]) matches++;
            
            if (cnt2[l] == cnt1[l]) matches--;
            cnt2[l]--;
            if (cnt2[l] == cnt1[l]) matches++;
            
            if (matches == 26) return true;
        }
        
        return false;
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [31. Next Permutation](../../0001-0500/0031-next-permutation/)
- [60. Permutation Sequence](../../0001-0500/0060-permutation-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/permutation-in-string/)
