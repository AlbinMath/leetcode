# LeetCode 3365: Rearrange K Substrings to Form Target String

**LeetCode Problem #3365 — Rearrange K Substrings to Form Target String**
Solve LeetCode Rearrange K Substrings to Form Target String using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rearrange K Substrings to Form Target String |
| LeetCode | #3365 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two strings `s` and `t`, both of which are anagrams of each other, and an integer `k`.

Your task is to determine whether it is possible to split the string `s` into `k` equal-sized substrings, rearrange the substrings, and concatenate them in *any order* to create a new string that matches the given string `t`.

Return `true` if this is possible, otherwise, return `false`.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

A **substring** is a contiguous non-empty sequence of characters within a string.

## Constraints
- `1 <= s.length == t.length <= 2 * 10^5`
- `1 <= k <= s.length`
- `s.length` is divisible by `k`.
- `s` and `t` consist only of lowercase English letters.
- The input is generated such that `s` and `t` are anagrams of each other.

## Examples
### Example 1
- **Input:** `s = "abcd", t = "cdab", k = 2`
- **Output:** `true`
- **Explanation:** Split `s` into 2 substrings of length 2: `["ab", "cd"]`. 
 Rearranging these substrings as `["cd", "ab"]`, and then concatenating them results in `"cdab"`, which matches `t`.

### Example 2
- **Input:** `s = "aabbcc", t = "bbaacc", k = 3`
- **Output:** `true`
- **Explanation:** Split `s` into 3 substrings of length 2: `["aa", "bb", "cc"]`. 
 Rearranging these substrings as `["bb", "aa", "cc"]`, and then concatenating them results in `"bbaacc"`, which matches `t`.

### Example 3
- **Input:** `s = "aabbcc", t = "bbaacc", k = 2`
- **Output:** `false`
- **Explanation:** Split `s` into 2 substrings of length 3: `["aab", "bcc"]`. 
 These substrings cannot be rearranged to form `t = "bbaacc"`, so the output is `false`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Rearrange K Substrings to Form Target String**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcd", t = "cdab", k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Split `s` into 2 substrings of length 2: `["ab", "cd"]`. 
 Rearranging these substrings as `["cd", "ab"]`, and then concatenating them results in `"cdab"`, which matches `t`.

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
var isPossibleToRearrange = function(s, t, k) {
    const n = s.length;
    const len = n / k;

    const freq = new Map();

    for (let i = 0; i < n; i += len) {
        const part = s.substring(i, i + len);

        freq.set(part, (freq.get(part) || 0) + 1);
    }

    for (let i = 0; i < n; i += len) {
        const part = t.substring(i, i + len);

        if (!freq.has(part)) {
            return false;
        }

        const count = freq.get(part);

        if (count === 1) {
            freq.delete(part);
        } else {
            freq.set(part, count - 1);
        }
    }

    return true;
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
- [1639. Number of Ways to Form a Target String Given a Dictionary](../../1501-2000/1639-number-of-ways-to-form-a-target-string-given-a-dictionary/)
- [2287. Rearrange Characters to Make Target String](../../2001-2500/2287-rearrange-characters-to-make-target-string/)
- [2522. Partition String Into Substrings With Values at Most K](../../2501-3000/2522-partition-string-into-substrings-with-values-at-most-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/)
