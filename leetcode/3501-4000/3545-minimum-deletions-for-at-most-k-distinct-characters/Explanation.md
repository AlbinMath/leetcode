# LeetCode 3545: Minimum Deletions for At Most K Distinct Characters

**LeetCode Problem #3545 — Minimum Deletions for At Most K Distinct Characters**
Solve LeetCode Minimum Deletions for At Most K Distinct Characters using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Deletions for At Most K Distinct Characters |
| LeetCode | #3545 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters, and an integer `k`.

Your task is to delete some (possibly none) of the characters in the string so that the number of **distinct** characters in the resulting string is **at most** `k`.

Return the **minimum** number of deletions required to achieve this.

## Constraints
- `1 <= s.length <= 16`
- `1 <= k <= 16`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abc", k = 2`
- **Output:** `1`
- **Explanation:** `s` has three distinct characters: `'a'`, `'b'` and `'c'`, each with a frequency of 1. 
 Since we can have at most `k = 2` distinct characters, remove all occurrences of any one character from the string. 
 For example, removing all occurrences of `'c'` results in at most `k` distinct characters. Thus, the answer is 1.

### Example 2
- **Input:** `s = "aabb", k = 2`
- **Output:** `0`
- **Explanation:** `s` has two distinct characters (`'a'` and `'b'`) with frequencies of 2 and 2, respectively. 
 Since we can have at most `k = 2` distinct characters, no deletions are required. Thus, the answer is 0.

### Example 3
- **Input:** `s = "yyyzz", k = 1`
- **Output:** `2`
- **Explanation:** `s` has two distinct characters (`'y'` and `'z'`) with frequencies of 3 and 2, respectively. 
 Since we can have at most `k = 1` distinct character, remove all occurrences of any one character from the string. 
 Removing all `'z'` results in at most `k` distinct characters. Thus, the answer is 2.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Deletions for At Most K Distinct Characters**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abc", k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** `s` has three distinct characters: `'a'`, `'b'` and `'c'`, each with a frequency of 1. 
 Since we can have at most `k = 2` distinct characters, remove all occurrences of any one character from the string. 
 For example, removing all occurrences of `'c'` results in at most `k` distinct characters. Thus, the answer is 1.

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
var minDeletion = function(s, k) {
    let freq = {};

    // Count character frequencies
    for (const ch of s) {
        freq[ch] = (freq[ch] || 0) + 1;
    }

    // Get all frequencies and sort ascending
    let arr = Object.values(freq).sort((a, b) => a - b);

    let deletions = 0;
    let remove = arr.length - k;

    // Remove least frequent characters
    for (let i = 0; i < remove; i++) {
        deletions += arr[i];
    }

    return deletions;
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
- [3970. Shortest Path With At Most K Consecutive Identical Characters](../../3501-4000/3970-shortest-path-with-at-most-k-consecutive-identical-characters/)
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1505-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [3085. Minimum Deletions to Make String K-Special](../../3001-3500/3085-minimum-deletions-to-make-string-k-special/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/)
