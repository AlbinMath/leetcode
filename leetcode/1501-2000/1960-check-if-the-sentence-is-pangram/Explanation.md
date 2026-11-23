# LeetCode 1832: Check if the Sentence Is Pangram

**LeetCode Problem #1832 — Check if the Sentence Is Pangram**
Solve LeetCode Check if the Sentence Is Pangram using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if the Sentence Is Pangram |
| LeetCode | #1832 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **pangram** is a sentence where every letter of the English alphabet appears at least once.

Given a string `sentence` containing only lowercase English letters, return* *`true`* if *`sentence`* is a **pangram**, or *`false`* otherwise.*

## Constraints
- `1 <= sentence.length <= 1000`
- `sentence` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `sentence = "thequickbrownfoxjumpsoverthelazydog"`
- **Output:** `true`
- **Explanation:** sentence contains at least one of every letter of the English alphabet.

### Example 2
- **Input:** `sentence = "leetcode"`
- **Output:** `false`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if the Sentence Is Pangram**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `sentence = "thequickbrownfoxjumpsoverthelazydog"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** sentence contains at least one of every letter of the English alphabet.

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
    bool checkIfPangram(string sentence) {
        bool seen[26] = {false};
        int count = 0;

        for (char c : sentence) {
            int index = c - 'a';

            if (!seen[index]) {
                seen[index] = true;
                count++;
            }
        }

        return count == 26;
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../../1501-2000/1566-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
- [2042. Check if Numbers Are Ascending in a Sentence](../../2001-2500/2168-check-if-numbers-are-ascending-in-a-sentence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-the-sentence-is-pangram/)
