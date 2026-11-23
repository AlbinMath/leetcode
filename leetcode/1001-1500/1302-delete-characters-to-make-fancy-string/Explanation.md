# LeetCode 1957: Delete Characters to Make Fancy String

**LeetCode Problem #1957 — Delete Characters to Make Fancy String**
Solve LeetCode Delete Characters to Make Fancy String using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Delete Characters to Make Fancy String |
| LeetCode | #1957 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **fancy string** is a string where no **three** **consecutive** characters are equal.

Given a string `s`, delete the **minimum** possible number of characters from `s` to make it **fancy**.

Return *the final string after the deletion*. It can be shown that the answer will always be **unique**.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "le e etcode"`
- **Output:** `"leetcode"`
- **Explanation:** Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

### Example 2
- **Input:** `s = " a aab aa aa"`
- **Output:** `"aabaa"`
- **Explanation:** Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

### Example 3
- **Input:** `s = "aab"`
- **Output:** `"aab"`
- **Explanation:** No three consecutive characters are equal, so return "aab".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Delete Characters to Make Fancy String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "le e etcode"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"leetcode"`.
4. **Verification:** Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

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
class Solution {
public:
    string makeFancyString(string s) {
        string result = "";

        for (char c : s) {
            int n = result.size();

            if (n >= 2 &&
                result[n - 1] == c &&
                result[n - 2] == c) {
                continue;
            }

            result += c;
        }

        return result;
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
- [2287. Rearrange Characters to Make Target String](../../2001-2500/2372-rearrange-characters-to-make-target-string/)
- [944. Delete Columns to Make Sorted](../../0501-1000/0981-delete-columns-to-make-sorted/)
- [955. Delete Columns to Make Sorted II](../../0501-1000/0992-delete-columns-to-make-sorted-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/delete-characters-to-make-fancy-string/)
