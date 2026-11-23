# LeetCode 1081: Smallest Subsequence of Distinct Characters

**LeetCode Problem #1081 — Smallest Subsequence of Distinct Characters**
Solve LeetCode Smallest Subsequence of Distinct Characters using C++ and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Subsequence of Distinct Characters |
| LeetCode | #1081 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s`, return *the * *lexicographically smallest* *subsequence* * of* `s` *that contains all the distinct characters of* `s` *exactly once*.

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "bcabc"`
- **Output:** `"abc"`

### Example 2
- **Input:** `s = "cbacdcbc"`
- **Output:** `"acdb"`

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
The code uses a **Monotonic Stack** (greedy) approach.

1. **Last Occurrence:** It records the last index of each character in the string.
2. **Used Array:** Tracks which characters are currently in the result to avoid duplicates.
3. **Build the Result String:** For each character `c` at index `i`:
   - If `c` is already in the result (`used[c]` is true), skip it.
   - While the last character in the result (`st.back()`) is greater than `c` AND that character appears again later (`last[st.back()] > i`): remove it from the result and mark it as unused. This ensures we keep the smallest characters first when possible.
   - Add `c` to the result and mark it as used.
4. The result is the lexicographically smallest subsequence containing all distinct characters.

Time complexity is $O(N)$ and space complexity is $O(1)$ (at most 26 characters in the stack).

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "bcabc"`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"abc"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    string smallestSubsequence(string s) {
        vector<int> last(26, 0);
        vector<bool> used(26, false);

        // Store the last occurrence of each character
        for (int i = 0; i < s.size(); i++) {
            last[s[i] - 'a'] = i;
        }

        string st;

        for (int i = 0; i < s.size(); i++) {
            char c = s[i];

            // Already included
            if (used[c - 'a'])
                continue;

            // Remove larger characters if they appear again later
            while (!st.empty() &&
                   st.back() > c &&
                   last[st.back() - 'a'] > i) {
                
                used[st.back() - 'a'] = false;
                st.pop_back();
            }

            st.push_back(c);
            used[c - 'a'] = true;
        }

        return st;
    }
};
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [1876. Substrings of Size Three with Distinct Characters](../../1501-2000/1987-substrings-of-size-three-with-distinct-characters/)
- [3398. Smallest Substring With Identical Characters I](../../3501-4000/3690-smallest-substring-with-identical-characters-i/)
- [3816. Lexicographically Smallest String After Deleting Duplicate Characters](../../4001-4500/4086-lexicographically-smallest-string-after-deleting-duplicate-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)
