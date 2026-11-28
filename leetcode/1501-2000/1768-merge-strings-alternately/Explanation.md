# LeetCode 1768: Merge Strings Alternately

**LeetCode Problem #1768 — Merge Strings Alternately**
Solve LeetCode Merge Strings Alternately using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge Strings Alternately |
| LeetCode | #1768 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return *the merged string.*

## Constraints
- `1 <= word1.length, word2.length <= 100`
- `word1` and `word2` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `word1 = "abc", word2 = "pqr"`
- **Output:** `"apbqcr"`
- **Explanation:** The merged string will be merged as so:
word1: a b c
word2: p q r
merged: a p b q c r

### Example 2
- **Input:** `word1 = "ab", word2 = "pqrs"`
- **Output:** `"apbqrs"`
- **Explanation:** Notice that as word2 is longer, "rs" is appended to the end.
word1: a b 
word2: p q r s
merged: a p b q r s

### Example 3
- **Input:** `word1 = "abcd", word2 = "pq"`
- **Output:** `"apbqcd"`
- **Explanation:** Notice that as word1 is longer, "cd" is appended to the end.
word1: a b c d
word2: p q 
merged: a p b q c d

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Merge Strings Alternately**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word1 = "abc", word2 = "pqr"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"apbqcr"`.
4. **Verification:** The merged string will be merged as so:
word1: a b c
word2: p q r
merged: a p b q c r

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
    string mergeAlternately(string word1, string word2) {
        string result = "";
        int i = 0, j = 0;

        while (i < word1.size() || j < word2.size()) {
            if (i < word1.size()) {
                result += word1[i];
                i++;
            }

            if (j < word2.size()) {
                result += word2[j];
                j++;
            }
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
- [1754. Largest Merge Of Two Strings](../../1501-2000/1754-largest-merge-of-two-strings/)
- [1115. Print FooBar Alternately](../../1001-1500/1115-print-foobar-alternately/)
- [43. Multiply Strings](../../0001-0500/0043-multiply-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-strings-alternately/)
