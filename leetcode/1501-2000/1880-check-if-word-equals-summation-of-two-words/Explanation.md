# LeetCode 1880: Check if Word Equals Summation of Two Words

**LeetCode Problem #1880 — Check if Word Equals Summation of Two Words**
Solve LeetCode Check if Word Equals Summation of Two Words using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Word Equals Summation of Two Words |
| LeetCode | #1880 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **letter value** of a letter is its position in the alphabet **starting from 0** (i.e. `'a' -> 0`, `'b' -> 1`, `'c' -> 2`, etc.).

The **numerical value** of some string of lowercase English letters `s` is the **concatenation** of the **letter values** of each letter in `s`, which is then **converted** into an integer.

For example, if `s = "acb"`, we concatenate each letter's letter value, resulting in `"021"`. After converting it, we get `21`.

You are given three strings `firstWord`, `secondWord`, and `targetWord`, each consisting of lowercase English letters `'a'` through `'j'` **inclusive**.

Return `true` *if the **summation** of the **numerical values** of *`firstWord`* and *`secondWord`* equals the **numerical value** of *`targetWord`*, or *`false`* otherwise.*

## Constraints
- `1 <= firstWord.length, ``secondWord.length, ``targetWord.length <= 8`
- `firstWord`, `secondWord`, and `targetWord` consist of lowercase English letters from `'a'` to `'j'` **inclusive**.

## Examples
### Example 1
- **Input:** `firstWord = "acb", secondWord = "cba", targetWord = "cdb"`
- **Output:** `true`
- **Explanation:** The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.

### Example 2
- **Input:** `firstWord = "aaa", secondWord = "a", targetWord = "aab"`
- **Output:** `false`
- **Explanation:** The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.

### Example 3
- **Input:** `firstWord = "aaa", secondWord = "a", targetWord = "aaaa"`
- **Output:** `true`
- **Explanation:** The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if Word Equals Summation of Two Words**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `firstWord = "acb", secondWord = "cba", targetWord = "cdb"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.

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
    int getValue(string word) {
        int value = 0;

        for (char c : word) {
            value = value * 10 + (c - 'a');
        }

        return value;
    }

    bool isSumEqual(string firstWord, string secondWord, string targetWord) {
        int first = getValue(firstWord);
        int second = getValue(secondWord);
        int target = getValue(targetWord);

        return first + second == target;
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
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1003-check-if-word-is-valid-after-substitutions/)
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../../1001-1500/1455-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
- [1662. Check If Two String Arrays are Equivalent](../../1501-2000/1662-check-if-two-string-arrays-are-equivalent/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/)
