# LeetCode 1653: Minimum Deletions to Make String Balanced

**LeetCode Problem #1653 — Minimum Deletions to Make String Balanced**
Solve LeetCode Minimum Deletions to Make String Balanced using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Deletions to Make String Balanced |
| LeetCode | #1653 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting only of characters `'a'` and `'b'`​​​​.

You can delete any number of characters in `s` to make `s` **balanced**. `s` is **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] = 'b'` and `s[j]= 'a'`.

Return *the **minimum** number of deletions needed to make *`s`* **balanced***.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is `'a'` or `'b'`​​.

## Examples
### Example 1
- **Input:** `s = "aababbab"`
- **Output:** `2`
- **Explanation:** You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aa b abb a b" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aab a bb a b" -> "aabbbb").

### Example 2
- **Input:** `s = "bbaaaaabb"`
- **Output:** `2`
- **Explanation:** The only solution is to delete the first two characters.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Deletions to Make String Balanced**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aababbab"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aa b abb a b" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aab a bb a b" -> "aabbbb").

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minimumDeletions(string s) {
        int deletions = 0;
        int b_count = 0;
        
        for (char c : s) {
            if (c == 'b') {
                b_count++;
            } else {
                // Either delete this 'a' (deletions + 1) or delete all previous 'b's (b_count)
                deletions = min(deletions + 1, b_count);
            }
        }
        
        return deletions;
    }
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1963. Minimum Number of Swaps to Make the String Balanced](../../1501-2000/1963-minimum-number-of-swaps-to-make-the-string-balanced/)
- [3085. Minimum Deletions to Make String K-Special](../../3001-3500/3085-minimum-deletions-to-make-string-k-special/)
- [1312. Minimum Insertion Steps to Make a String Palindrome](../../1001-1500/1312-minimum-insertion-steps-to-make-a-string-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/)
