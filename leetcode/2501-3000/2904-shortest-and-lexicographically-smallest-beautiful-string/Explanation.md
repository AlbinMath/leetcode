# LeetCode 2904: Shortest and Lexicographically Smallest Beautiful String

**LeetCode Problem #2904 — Shortest and Lexicographically Smallest Beautiful String**
Solve LeetCode Shortest and Lexicographically Smallest Beautiful String using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest and Lexicographically Smallest Beautiful String |
| LeetCode | #2904 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary string `s` and a positive integer `k`.

A substring of `s` is **beautiful** if the number of `1`'s in it is exactly `k`.

Let `len` be the length of the **shortest** beautiful substring.

Return *the lexicographically **smallest** beautiful substring of string *`s`* with length equal to *`len`. If `s` doesn't contain a beautiful substring, return *an **empty** string*.

A string `a` is lexicographically **larger** than a string `b` (of the same length) if in the first position where `a` and `b` differ, `a` has a character strictly larger than the corresponding character in `b`.

For example, `"abcd"` is lexicographically larger than `"abcc"` because the first position they differ is at the fourth character, and `d` is greater than `c`.

## Constraints
- `1 <= s.length <= 100`
- `1 <= k <= s.length`

## Examples
### Example 1
- **Input:** `s = "100011001", k = 3`
- **Output:** `"11001"`
- **Explanation:** There are 7 beautiful substrings in this example:
1. The substring " 100011 001".
2. The substring " 1000110 01".
3. The substring " 10001100 1".
4. The substring "1 00011001 ".
5. The substring "10 0011001 ".
6. The substring "100 011001 ".
7. The substring "1000 11001 ".
The length of the shortest beautiful substring is 5.
The lexicographically smallest beautiful substring with length 5 is the substring "11001".

### Example 2
- **Input:** `s = "1011", k = 2`
- **Output:** `"11"`
- **Explanation:** There are 3 beautiful substrings in this example:
1. The substring " 101 1".
2. The substring "1 011 ".
3. The substring "10 11 ".
The length of the shortest beautiful substring is 2.
The lexicographically smallest beautiful substring with length 2 is the substring "11".

### Example 3
- **Input:** `s = "000", k = 1`
- **Output:** `""`
- **Explanation:** There are no beautiful substrings in this example.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Shortest and Lexicographically Smallest Beautiful String**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "100011001", k = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"11001"`.
4. **Verification:** There are 7 beautiful substrings in this example:
1. The substring " 100011 001".
2. The substring " 1000110 01".
3. The substring " 10001100 1".
4. The substring "1 00011001 ".
5. The substring "10 0011001 ".
6. The substring "100 011001 ".
7. The substring "1000 11001 ".
The length of the shortest beautiful substring is 5.
The lexicographically smallest beautiful substring with length 5 is the substring "11001".

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
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.size();

        int ones = 0;
        int left = 0;

        int bestLen = INT_MAX;
        string ans = "";

        for (int right = 0; right < n; right++) {
            if (s[right] == '1')
                ones++;

            // Keep exactly k ones
            while (ones > k) {
                if (s[left] == '1')
                    ones--;
                left++;
            }

            // We have exactly k ones
            if (ones == k) {
                // Remove unnecessary leading zeros
                while (left <= right && s[left] == '0')
                    left++;

                int len = right - left + 1;
                string cur = s.substr(left, len);

                if (len < bestLen) {
                    bestLen = len;
                    ans = cur;
                }
                else if (len == bestLen && cur < ans) {
                    ans = cur;
                }
            }
        }

        return ans;
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
- [1061. Lexicographically Smallest Equivalent String](../../1001-1500/1061-lexicographically-smallest-equivalent-string/)
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)
- [2434. Using a Robot to Print the Lexicographically Smallest String](../../2001-2500/2434-using-a-robot-to-print-the-lexicographically-smallest-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/)
