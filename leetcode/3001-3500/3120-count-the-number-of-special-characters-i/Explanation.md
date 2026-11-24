# LeetCode 3120: Count the Number of Special Characters I

**LeetCode Problem #3120 — Count the Number of Special Characters I**
Solve LeetCode Count the Number of Special Characters I using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Special Characters I |
| LeetCode | #3120 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `word`. A letter is called **special** if it appears **both** in lowercase and uppercase in `word`.

Return the number of* ***special** letters in* *`word`.

## Constraints
- `1 <= word.length <= 50`
- `word` consists of only lowercase and uppercase English letters.

## Examples
### Example 1
- **Input:** `word = "aaAbcBC"`
- **Output:** `3`
- **Explanation:** The special characters in `word` are `'a'`, `'b'`, and `'c'`.

### Example 2
- **Input:** `word = "abc"`
- **Output:** `0`
- **Explanation:** No character in `word` appears in uppercase.

### Example 3
- **Input:** `word = "abBCab"`
- **Output:** `1`
- **Explanation:** The only special character in `word` is `'b'`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count the Number of Special Characters I**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "aaAbcBC"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The special characters in `word` are `'a'`, `'b'`, and `'c'`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int numberOfSpecialChars(string word) {
        bool lower[26] = {};
        bool upper[26] = {};

        for (char c : word) {
            if (c >= 'a' && c <= 'z')
                lower[c - 'a'] = true;
            else
                upper[c - 'A'] = true;
        }

        int count = 0;

        for (int i = 0; i < 26; i++) {
            if (lower[i] && upper[i])
                count++;
        }

        return count;
    }
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1358. Number of Substrings Containing All Three Characters](../../1001-1500/1358-number-of-substrings-containing-all-three-characters/)
- [1898. Maximum Number of Removable Characters](../../1501-2000/1898-maximum-number-of-removable-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-special-characters-i/)
