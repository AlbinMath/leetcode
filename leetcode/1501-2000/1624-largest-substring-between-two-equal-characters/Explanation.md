# LeetCode 1624: Largest Substring Between Two Equal Characters

**LeetCode Problem #1624 — Largest Substring Between Two Equal Characters**
Solve LeetCode Largest Substring Between Two Equal Characters using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Substring Between Two Equal Characters |
| LeetCode | #1624 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, return *the length of the longest substring between two equal characters, excluding the two characters.* If there is no such substring return `-1`.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= s.length <= 300`
- `s` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aa"`
- **Output:** `0`
- **Explanation:** The optimal substring here is an empty substring between the two `'a's`.

### Example 2
- **Input:** `s = "abca"`
- **Output:** `2`
- **Explanation:** The optimal substring here is "bc".

### Example 3
- **Input:** `s = "cbzxy"`
- **Output:** `-1`
- **Explanation:** There are no characters that appear twice in s.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Substring Between Two Equal Characters**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aa"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** The optimal substring here is an empty substring between the two `'a's`.

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
    int maxLengthBetweenEqualCharacters(string s) {
        int first[26];
        fill(first, first + 26, -1);

        int maxLen = -1;

        for (int i = 0; i < s.size(); i++) {
            int index = s[i] - 'a';

            if (first[index] == -1) {
                first[index] = i;
            } else {
                maxLen = max(maxLen, i - first[index] - 1);
            }
        }

        return maxLen;
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
- [1360. Number of Days Between Two Dates](../../1001-1500/1360-number-of-days-between-two-dates/)
- [1385. Find the Distance Value Between Two Arrays](../../1001-1500/1385-find-the-distance-value-between-two-arrays/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-substring-between-two-equal-characters/)
