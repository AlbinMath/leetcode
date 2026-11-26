# LeetCode 1910: Remove All Occurrences of a Substring

**LeetCode Problem #1910 — Remove All Occurrences of a Substring**
Solve LeetCode Remove All Occurrences of a Substring using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove All Occurrences of a Substring |
| LeetCode | #1910 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings `s` and `part`, perform the following operation on `s` until **all** occurrences of the substring `part` are removed:

Find the **leftmost** occurrence of the substring `part` and **remove** it from `s`.

Return `s`* after removing all occurrences of *`part`.

A **substring** is a contiguous sequence of characters in a string.

## Constraints
- `1 <= s.length <= 1000`
- `1 <= part.length <= 1000`
- `s`​​​​​​ and `part` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "daabcbaabcbc", part = "abc"`
- **Output:** `"dab"`
- **Explanation:** : The following operations are done:
- s = "da

### Example 2
- **Input:** `s = "axxxxyyyyb", part = "xy"`
- **Output:** `"ab"`
- **Explanation:** : The following operations are done:
- s = "axxx

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove All Occurrences of a Substring**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "daabcbaabcbc", part = "abc"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"dab"`.
4. **Verification:** : The following operations are done:
- s = "da

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
using namespace std;

class Solution {
public:
    string removeOccurrences(string s, string part) {
        string res;
        res.reserve(s.size());
        int m = part.size();
        char last_char = part.back();
        
        for (char c : s) {
            res.push_back(c);
            // Quick check on the last character before comparing the full suffix
            if (c == last_char && (int)res.size() >= m) {
                if (res.compare(res.size() - m, m, part) == 0) {
                    res.resize(res.size() - m);
                }
            }
        }
        
        return res;
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
- [1297. Maximum Number of Occurrences of a Substring](../../1001-1500/1297-maximum-number-of-occurrences-of-a-substring/)
- [1941. Check if All Characters Have Equal Number of Occurrences](../../1501-2000/1941-check-if-all-characters-have-equal-number-of-occurrences/)
- [3090. Maximum Length Substring With Two Occurrences](../../3001-3500/3090-maximum-length-substring-with-two-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-all-occurrences-of-a-substring/)
