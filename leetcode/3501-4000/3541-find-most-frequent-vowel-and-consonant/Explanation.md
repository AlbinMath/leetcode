# LeetCode 3541: Find Most Frequent Vowel and Consonant

**LeetCode Problem #3541 — Find Most Frequent Vowel and Consonant**
Solve LeetCode Find Most Frequent Vowel and Consonant using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Most Frequent Vowel and Consonant |
| LeetCode | #3541 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters (`'a'` to `'z'`).

Your task is to:

Find the vowel (one of `'a'`, `'e'`, `'i'`, `'o'`, or `'u'`) with the **maximum** frequency. 
 Find the consonant (all other letters excluding vowels) with the **maximum** frequency.

Return the sum of the two frequencies.

**Note**: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

The **frequency** of a letter `x` is the number of times it occurs in the string.

## Constraints
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters only.

## Examples
### Example 1
- **Input:** `s = "successes"`
- **Output:** `6`
- **Explanation:** The vowels are: `'u'` (frequency 1), `'e'` (frequency 2). The maximum frequency is 2. 
 The consonants are: `'s'` (frequency 4), `'c'` (frequency 2). The maximum frequency is 4. 
 The output is `2 + 4 = 6`.

### Example 2
- **Input:** `s = "aeiaeia"`
- **Output:** `3`
- **Explanation:** The vowels are: `'a'` (frequency 3), `'e'` ( frequency 2), `'i'` (frequency 2). The maximum frequency is 3. 
 There are no consonants in `s`. Hence, maximum consonant frequency = 0. 
 The output is `3 + 0 = 3`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find Most Frequent Vowel and Consonant**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "successes"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The vowels are: `'u'` (frequency 1), `'e'` (frequency 2). The maximum frequency is 2. 
 The consonants are: `'s'` (frequency 4), `'c'` (frequency 2). The maximum frequency is 4. 
 The output is `2 + 4 = 6`.

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
var maxFreqSum = function(s) {
    let freq = Array(26).fill(0);

    // Count frequency of each character
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    let maxVowel = 0;
    let maxConsonant = 0;

    const vowels = "aeiou";

    // Find maximum vowel and consonant frequencies
    for (let i = 0; i < 26; i++) {
        let ch = String.fromCharCode(i + 97);

        if (vowels.includes(ch)) {
            maxVowel = Math.max(maxVowel, freq[i]);
        } else {
            maxConsonant = Math.max(maxConsonant, freq[i]);
        }
    }

    return maxVowel + maxConsonant;
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
- [3813. Vowel-Consonant Score](../../3501-4000/3813-vowel-consonant-score/)
- [1606. Find Servers That Handled Most Number of Requests](../../1501-2000/1606-find-servers-that-handled-most-number-of-requests/)
- [1673. Find the Most Competitive Subsequence](../../1501-2000/1673-find-the-most-competitive-subsequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/)
