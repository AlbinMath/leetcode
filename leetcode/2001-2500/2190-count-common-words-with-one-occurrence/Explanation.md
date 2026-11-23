# LeetCode 2085: Count Common Words With One Occurrence

**LeetCode Problem #2085 — Count Common Words With One Occurrence**
Solve LeetCode Count Common Words With One Occurrence using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Common Words With One Occurrence |
| LeetCode | #2085 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two string arrays `words1` and `words2`, return *the number of strings that appear **exactly once** in each of the two arrays.*

## Constraints
- `1 <= words1.length, words2.length <= 1000`
- `1 <= words1[i].length, words2[j].length <= 30`
- `words1[i]` and `words2[j]` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]`
- **Output:** `2`
- **Explanation:** - "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.

### Example 2
- **Input:** `words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]`
- **Output:** `0`
- **Explanation:** There are no strings that appear in each of the two arrays.

### Example 3
- **Input:** `words1 = ["a","ab"], words2 = ["a","a","a","ab"]`
- **Output:** `1`
- **Explanation:** The only string that appears exactly once in each of the two arrays is "ab".

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Common Words With One Occurrence**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** - "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.

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
var countWords = function(words1, words2) {
    const freq1 = new Map();
    const freq2 = new Map();

    for (const word of words1) {
        freq1.set(word, (freq1.get(word) || 0) + 1);
    }

    for (const word of words2) {
        freq2.set(word, (freq2.get(word) || 0) + 1);
    }

    let count = 0;

    for (const [word, frequency] of freq1) {
        if (frequency === 1 && freq2.get(word) === 1) {
            count++;
        }
    }

    return count;
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
- [1638. Count Substrings That Differ by One Character](../../1501-2000/1743-count-substrings-that-differ-by-one-character/)
- [2135. Count Words Obtained After Adding a Letter](../../2001-2500/2256-count-words-obtained-after-adding-a-letter/)
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-common-words-with-one-occurrence/)
