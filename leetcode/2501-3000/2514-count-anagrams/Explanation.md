# LeetCode 2514: Count Anagrams

**LeetCode Problem #2514 — Count Anagrams**
Solve LeetCode Count Anagrams using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Anagrams |
| LeetCode | #2514 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` containing one or more words. Every consecutive pair of words is separated by a single space `' '`.

A string `t` is an **anagram** of string `s` if the `i^th` word of `t` is a **permutation** of the `i^th` word of `s`.

For example, `"acb dfe"` is an anagram of `"abc def"`, but `"def cab"` and `"adc bef"` are not.

Return *the number of **distinct anagrams** of *`s`. Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters and spaces `' '`.
- There is single space between consecutive words.

## Examples
### Example 1
- **Input:** `s = "too hot"`
- **Output:** `18`
- **Explanation:** Some of the anagrams of the given string are "too hot", "oot hot", "oto toh", "too toh", and "too oht".

### Example 2
- **Input:** `s = "aa"`
- **Output:** `1`
- **Explanation:** There is only one anagram possible for the given string.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Anagrams**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "too hot"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `18`.
4. **Verification:** Some of the anagrams of the given string are "too hot", "oot hot", "oto toh", "too toh", and "too oht".

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
var countAnagrams = function(s) {
    const MOD = 1000000007n;
    const n = s.length;

    const fact = Array(n + 1).fill(1n);
    const invFact = Array(n + 1).fill(1n);

    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * BigInt(i) % MOD;
    }

    function modPow(a, b) {
        let result = 1n;

        while (b > 0n) {
            if (b % 2n === 1n) {
                result = result * a % MOD;
            }
            a = a * a % MOD;
            b /= 2n;
        }

        return result;
    }

    invFact[n] = modPow(fact[n], MOD - 2n);

    for (let i = n; i >= 1; i--) {
        invFact[i - 1] = invFact[i] * BigInt(i) % MOD;
    }

    let answer = 1n;

    for (const word of s.split(' ')) {
        const freq = Array(26).fill(0);

        for (const ch of word) {
            freq[ch.charCodeAt(0) - 97]++;
        }

        let ways = fact[word.length];

        for (const count of freq) {
            ways = ways * invFact[count] % MOD;
        }

        answer = answer * ways % MOD;
    }

    return Number(answer);
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
- [49. Group Anagrams](../../0001-0500/0049-group-anagrams/)
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)
- [38. Count and Say](../../0001-0500/0038-count-and-say/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-anagrams/)
