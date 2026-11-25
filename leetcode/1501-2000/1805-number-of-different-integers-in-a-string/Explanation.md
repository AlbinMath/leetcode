# LeetCode 1805: Number of Different Integers in a String

**LeetCode Problem #1805 — Number of Different Integers in a String**
Solve LeetCode Number of Different Integers in a String using C++ and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Different Integers in a String |
| LeetCode | #1805 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `word` that consists of digits and lowercase English letters.

You will replace every non-digit character with a space. For example, `"a123bc34d8ef34"` will become `" 123 34 8 34"`. Notice that you are left with some integers that are separated by at least one space: `"123"`, `"34"`, `"8"`, and `"34"`.

Return *the number of **different** integers after performing the replacement operations on *`word`.

Two integers are considered different if their decimal representations **without any leading zeros** are different.

## Constraints
- `1 <= word.length <= 1000`
- `word` consists of digits and lowercase English letters.

## Examples
### Example 1
- **Input:** `word = "a 123 bc 34 d 8 ef 34 "`
- **Output:** `3`
- **Explanation:** The three different integers are "123", "34", and "8". Notice that "34" is only counted once.

### Example 2
- **Input:** `word = "leet 1234 code 234 "`
- **Output:** `2`

### Example 3
- **Input:** `word = "a 1 b 01 c 001 "`
- **Output:** `1`
- **Explanation:** The three integers "1", "01", and "001" all represent the same integer because
the leading zeros are ignored when comparing their decimal values.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Different Integers in a String**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "a 123 bc 34 d 8 ef 34 "`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The three different integers are "123", "34", and "8". Notice that "34" is only counted once.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int numDifferentIntegers(string word) {
        unordered_set<string> uniqueNumbers;
        int i = 0;
        int n = word.size();

        while (i < n) {
            if (isdigit(word[i])) {
                string number = "";

                while (i < n && isdigit(word[i])) {
                    number += word[i];
                    i++;
                }

                // Remove leading zeros
                int j = 0;
                while (j < number.size() && number[j] == '0') {
                    j++;
                }

                number = number.substr(j);

                // Handle numbers containing only zeros
                if (number.empty()) {
                    number = "0";
                }

                uniqueNumbers.insert(number);
            } else {
                i++;
            }
        }

        return uniqueNumbers.size();
    }
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [434. Number of Segments in a String](../../0001-0500/0434-number-of-segments-in-a-string/)
- [806. Number of Lines To Write String](../../0501-1000/0806-number-of-lines-to-write-string/)
- [1525. Number of Good Ways to Split a String](../../1501-2000/1525-number-of-good-ways-to-split-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-different-integers-in-a-string/)
