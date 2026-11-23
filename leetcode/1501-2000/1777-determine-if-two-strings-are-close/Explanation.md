# LeetCode 1657: Determine if Two Strings Are Close

**LeetCode Problem #1657 — Determine if Two Strings Are Close**
Solve LeetCode Determine if Two Strings Are Close using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Determine if Two Strings Are Close |
| LeetCode | #1657 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Two strings are considered **close** if you can attain one from the other using the following operations:

Operation 1: Swap any two **existing** characters.

For example, `a b cd e -> a e cd b ` 
 
 
 Operation 2: Transform **every** occurrence of one **existing** character into another **existing** character, and do the same with the other character.
 
 For example, ` aa c abb -> bb c baa ` (all `a`'s turn into `b`'s, and all `b`'s turn into `a`'s)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true`* if *`word1`* and *`word2`* are **close**, and *`false`* otherwise.*

## Constraints
- `1 <= word1.length, word2.length <= 10^5`
- `word1` and `word2` contain only lowercase English letters.

## Examples
### Example 1
- **Input:** `word1 = "abc", word2 = "bca"`
- **Output:** `true`
- **Explanation:** You can attain word2 from word1 in 2 operations.
Apply Operation 1: "a bc " -> "a cb "
Apply Operation 1: " a c b " -> " b c a "

### Example 2
- **Input:** `word1 = "a", word2 = "aa"`
- **Output:** `false`
- **Explanation:** It is impossible to attain word2 from word1, or vice versa, in any number of operations.

### Example 3
- **Input:** `word1 = "cabbba", word2 = "abbccc"`
- **Output:** `true`
- **Explanation:** You can attain word2 from word1 in 3 operations.
Apply Operation 1: "ca b bb a " -> "ca a bb b "
Apply Operation 2: " c aa bbb " -> " b aa ccc "
Apply Operation 2: " baa ccc" -> " abb ccc"

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Determine if Two Strings Are Close**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word1 = "abc", word2 = "bca"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** You can attain word2 from word1 in 2 operations.
Apply Operation 1: "a bc " -> "a cb "
Apply Operation 1: " a c b " -> " b c a "

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var closeStrings = function(word1, word2) {
    if (word1.length !== word2.length) {
        return false;
    }

    const freq1 = new Map();
    const freq2 = new Map();

    for (const ch of word1) {
        freq1.set(ch, (freq1.get(ch) || 0) + 1);
    }

    for (const ch of word2) {
        freq2.set(ch, (freq2.get(ch) || 0) + 1);
    }

    // Both strings must contain the same characters
    if (freq1.size !== freq2.size) {
        return false;
    }

    for (const ch of freq1.keys()) {
        if (!freq2.has(ch)) {
            return false;
        }
    }

    // Compare sorted character frequencies
    const counts1 = [...freq1.values()].sort((a, b) => a - b);
    const counts2 = [...freq2.values()].sort((a, b) => a - b);

    return counts1.every((count, i) => count === counts2[i]);
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
- [2068. Check Whether Two Strings are Almost Equivalent](../../2001-2500/2177-check-whether-two-strings-are-almost-equivalent/)
- [3327. Check if DFS Strings Are Palindromes](../../3501-4000/3603-check-if-dfs-strings-are-palindromes/)
- [1704. Determine if String Halves Are Alike](../../1501-2000/1823-determine-if-string-halves-are-alike/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/determine-if-two-strings-are-close/)
