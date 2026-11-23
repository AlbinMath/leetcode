# LeetCode 1717: Maximum Score From Removing Substrings

**LeetCode Problem #1717 — Maximum Score From Removing Substrings**
Solve LeetCode Maximum Score From Removing Substrings using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score From Removing Substrings |
| LeetCode | #1717 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times.

Remove substring `"ab"` and gain `x` points.

For example, when removing `"ab"` from `"c ab xbae"` it becomes `"cxbae"`. 
 
 
 Remove substring `"ba"` and gain `y` points.
 
 For example, when removing `"ba"` from `"cabx ba e"` it becomes `"cabxe"`.

Return *the maximum points you can gain after applying the above operations on* `s`.

## Constraints
- `1 <= s.length <= 10^5`
- `1 <= x, y <= 10^4`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "cdbcbbaaabab", x = 4, y = 5`
- **Output:** `19`
- **Explanation:** - Remove the "ba" underlined in "cdbcbbaaa ba b". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaa ab ". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcb ba a". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbc ba ". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

### Example 2
- **Input:** `s = "aabbaaxybbaabb", x = 5, y = 4`
- **Output:** `20`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Score From Removing Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "cdbcbbaaabab", x = 4, y = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `19`.
4. **Verification:** - Remove the "ba" underlined in "cdbcbbaaa ba b". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaa ab ". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcb ba a". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbc ba ". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

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
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumGain(string s, int x, int y) {
        char first = 'a', second = 'b';
        // Ensure `first + second` is always the higher-scoring pair
        if (y > x) {
            swap(x, y);
            swap(first, second);
        }
        
        int total_score = 0;
        int first_cnt = 0;
        int second_cnt = 0;
        
        for (char c : s) {
            if (c == first) {
                first_cnt++;
            } else if (c == second) {
                if (first_cnt > 0) {
                    // Greedily form the high-value pair immediately
                    first_cnt--;
                    total_score += x;
                } else {
                    second_cnt++;
                }
            } else {
                // Non-'a'/'b' character acts as a wall; pair leftover characters for `y`
                total_score += min(first_cnt, second_cnt) * y;
                first_cnt = 0;
                second_cnt = 0;
            }
        }
        
        // Pair any remaining characters after the last wall
        total_score += min(first_cnt, second_cnt) * y;
        
        return total_score;
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
- [2091. Removing Minimum and Maximum From Array](../../2001-2500/2212-removing-minimum-and-maximum-from-array/)
- [2975. Maximum Square Area by Removing Fences From a Field](../../3001-3500/3250-maximum-square-area-by-removing-fences-from-a-field/)
- [2390. Removing Stars From a String](../../2001-2500/2470-removing-stars-from-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-from-removing-substrings/)
