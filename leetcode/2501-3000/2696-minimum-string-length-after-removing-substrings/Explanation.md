# LeetCode 2696: Minimum String Length After Removing Substrings

**LeetCode Problem #2696 — Minimum String Length After Removing Substrings**
Solve LeetCode Minimum String Length After Removing Substrings using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum String Length After Removing Substrings |
| LeetCode | #2696 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting only of **uppercase** English letters.

You can apply some operations to this string where, in one operation, you can remove **any** occurrence of one of the substrings `"AB"` or `"CD"` from `s`.

Return *the **minimum** possible length of the resulting string that you can obtain*.

**Note** that the string concatenates after removing the substring and could produce new `"AB"` or `"CD"` substrings.

## Constraints
- `1 <= s.length <= 100`
- `s` consists only of uppercase English letters.

## Examples
### Example 1
- **Input:** `s = "ABFCACDB"`
- **Output:** `2`
- **Explanation:** We can do the following operations:
- Remove the substring " AB FCACDB", so s = "FCACDB".
- Remove the substring "FCA CD B", so s = "FCAB".
- Remove the substring "FC AB ", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.

### Example 2
- **Input:** `s = "ACBBD"`
- **Output:** `5`
- **Explanation:** We cannot do any operations on the string so the length remains the same.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum String Length After Removing Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "ABFCACDB"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can do the following operations:
- Remove the substring " AB FCACDB", so s = "FCACDB".
- Remove the substring "FCA CD B", so s = "FCAB".
- Remove the substring "FC AB ", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
#include <string>
using namespace std;

class Solution {
public:
    int minLength(string s) {
        int top = 0; // Acts as the size/write-pointer of our in-place stack
        
        for (char c : s) {
            if (top > 0 && ((c == 'B' && s[top - 1] == 'A') || 
                            (c == 'D' && s[top - 1] == 'C'))) {
                top--; // Pop matching 'A' or 'C'
            } else {
                s[top++] = c; // Push current character
            }
        }
        
        return top;
    }
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3170. Lexicographically Minimum String After Removing Stars](../../3001-3500/3170-lexicographically-minimum-string-after-removing-stars/)
- [1750. Minimum Length of String After Deleting Similar Ends](../../1501-2000/1750-minimum-length-of-string-after-deleting-similar-ends/)
- [3223. Minimum Length of String After Operations](../../3001-3500/3223-minimum-length-of-string-after-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/)
