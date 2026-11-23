# LeetCode 1668: Maximum Repeating Substring

**LeetCode Problem #1668 — Maximum Repeating Substring**
Solve LeetCode Maximum Repeating Substring using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Repeating Substring |
| LeetCode | #1668 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
For a string `sequence`, a string `word` is **`k`-repeating** if `word` concatenated `k` times is a substring of `sequence`. The `word`'s **maximum `k`-repeating value** is the highest value `k` where `word` is `k`-repeating in `sequence`. If `word` is not a substring of `sequence`, `word`'s maximum `k`-repeating value is `0`.

Given strings `sequence` and `word`, return *the **maximum `k`-repeating value** of `word` in `sequence`*.

## Constraints
- `1 <= sequence.length <= 100`
- `1 <= word.length <= 100`
- `sequence` and `word` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `sequence = "ababc", word = "ab"`
- **Output:** `2`
- **Explanation:** "abab" is a substring in " abab c".

### Example 2
- **Input:** `sequence = "ababc", word = "ba"`
- **Output:** `1`
- **Explanation:** "ba" is a substring in "a ba bc". "baba" is not a substring in "ababc".

### Example 3
- **Input:** `sequence = "ababc", word = "ac"`
- **Output:** `0`
- **Explanation:** "ac" is not a substring in "ababc".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Repeating Substring**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `sequence = "ababc", word = "ab"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** "abab" is a substring in " abab c".

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
    int maxRepeating(string sequence, string word) {
        int k = 0;
        string repeated = word;

        while (sequence.find(repeated) != string::npos) {
            k++;
            repeated += word;
        }

        return k;
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
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [395. Longest Substring with At Least K Repeating Characters](../../0001-0500/0395-longest-substring-with-at-least-k-repeating-characters/)
- [2213. Longest Substring of One Repeating Character](../../2001-2500/2319-longest-substring-of-one-repeating-character/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-repeating-substring/)
