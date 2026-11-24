# LeetCode 1897: Redistribute Characters to Make All Strings Equal

**LeetCode Problem #1897 — Redistribute Characters to Make All Strings Equal**
Solve LeetCode Redistribute Characters to Make All Strings Equal using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Redistribute Characters to Make All Strings Equal |
| LeetCode | #1897 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of strings `words` (**0-indexed**).

In one operation, pick two **distinct** indices `i` and `j`, where `words[i]` is a non-empty string, and move **any** character from `words[i]` to **any** position in `words[j]`.

Return `true` *if you can make** every** string in *`words`* **equal **using **any** number of operations*,* and *`false` *otherwise*.

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["abc","aabc","bc"]`
- **Output:** `true`
- **Explanation:** Move the first 'a' in words[1] to the front of words[2],
to make `words[1]` = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return `true`.

### Example 2
- **Input:** `words = ["ab","a"]`
- **Output:** `false`
- **Explanation:** It is impossible to make all the strings equal using the operation.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Redistribute Characters to Make All Strings Equal**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["abc","aabc","bc"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Move the first 'a' in words[1] to the front of words[2],
to make `words[1]` = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return `true`.

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
    bool makeEqual(vector<string>& words) {
        int count[26] = {0};
        int n = words.size();

        for (string word : words) {
            for (char c : word) {
                count[c - 'a']++;
            }
        }

        for (int i = 0; i < 26; i++) {
            if (count[i] % n != 0) {
                return false;
            }
        }

        return true;
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
- [3784. Minimum Deletion Cost to Make All Characters Equal](../../3501-4000/3784-minimum-deletion-cost-to-make-all-characters-equal/)
- [1941. Check if All Characters Have Equal Number of Occurrences](../../1501-2000/1941-check-if-all-characters-have-equal-number-of-occurrences/)
- [2531. Make Number of Distinct Characters Equal](../../2501-3000/2531-make-number-of-distinct-characters-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/)
