# LeetCode 2949: Count Beautiful Substrings II

**LeetCode Problem #2949 — Count Beautiful Substrings II**
Solve LeetCode Count Beautiful Substrings II using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Beautiful Substrings II |
| LeetCode | #2949 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` and a positive integer `k`.

Let `vowels` and `consonants` be the number of vowels and consonants in a string.

A string is **beautiful** if:

`vowels == consonants`. 
 `(vowels * consonants) % k == 0`, in other terms the multiplication of `vowels` and `consonants` is divisible by `k`.

Return *the number of **non-empty beautiful substrings** in the given string* `s`.

A **substring** is a contiguous sequence of characters in a string.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

**Consonant letters** in English are every letter except vowels.

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `1 <= k <= 1000`
- `s` consists of only English lowercase letters.

## Examples
### Example 1
- **Input:** `s = "baeyh", k = 2`
- **Output:** `2`
- **Explanation:** There are 2 beautiful substrings in the given string.
- Substring "b aeyh ", vowels = 2 (["a",e"]), consonants = 2 (["y","h"]).
You can see that string "aeyh" is beautiful as vowels == consonants and vowels * consonants % k == 0.
- Substring " baey h", vowels = 2 (["a",e"]), consonants = 2 (["b","y"]).
You can see that string "baey" is beautiful as vowels == consonants and vowels * consonants % k == 0.
It can be shown that there are only 2 beautiful substrings in the given string.

### Example 2
- **Input:** `s = "abba", k = 1`
- **Output:** `3`
- **Explanation:** There are 3 beautiful substrings in the given string.
- Substring " ab ba", vowels = 1 (["a"]), consonants = 1 (["b"]).
- Substring "ab ba ", vowels = 1 (["a"]), consonants = 1 (["b"]).
- Substring " abba ", vowels = 2 (["a","a"]), consonants = 2 (["b","b"]).
It can be shown that there are only 3 beautiful substrings in the given string.

### Example 3
- **Input:** `s = "bcdf", k = 1`
- **Output:** `0`
- **Explanation:** There are no beautiful substrings in the given string.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Beautiful Substrings II**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "baeyh", k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are 2 beautiful substrings in the given string.
- Substring "b aeyh ", vowels = 2 (["a",e"]), consonants = 2 (["y","h"]).
You can see that string "aeyh" is beautiful as vowels == consonants and vowels * consonants % k == 0.
- Substring " baey h", vowels = 2 (["a",e"]), consonants = 2 (["b","y"]).
You can see that string "baey" is beautiful as vowels == consonants and vowels * consonants % k == 0.
It can be shown that there are only 2 beautiful substrings in the given string.

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
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var beautifulSubstrings = function(s, k) {
    // 1. Find smallest M > 0 such that (M * M) % (4 * k) === 0
    const target = 4 * k;
    let m = 1;
    while ((m * m) % target !== 0) {
        m++;
    }

    const isVowel = (ch) => ch === 'a' || ch === 'e' || ch === 'i' || ch === 'o' || ch === 'u';
    
    // Map tracks counts of (balance, index % m) pairs
    // Initial state at index -1: balance = 0, (-1 mod m) = m - 1
    const seen = new Map();
    const initialMod = (m - 1) % m;
    seen.set(`0,${initialMod}`, 1);

    let balance = 0;
    let count = 0;

    for (let i = 0; i < s.length; i++) {
        balance += isVowel(s[i]) ? 1 : -1;
        const mod = i % m;
        const key = `${balance},${mod}`;

        const prevCount = seen.get(key) || 0;
        count += prevCount;
        seen.set(key, prevCount + 1);
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
- [2947. Count Beautiful Substrings I](../../2501-3000/2947-count-beautiful-substrings-i/)
- [696. Count Binary Substrings](../../0501-1000/0696-count-binary-substrings/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0828-count-unique-characters-of-all-substrings-of-a-given-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-beautiful-substrings-ii/)
