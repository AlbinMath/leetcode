# LeetCode 3913: Sort Vowels by Frequency

**LeetCode Problem #3913 — Sort Vowels by Frequency**
Solve LeetCode Sort Vowels by Frequency using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Vowels by Frequency |
| LeetCode | #3913 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of lowercase English characters.

Rearrange only the **vowels** in the string so that they appear in **non-increasing** order of their frequency.

If multiple vowels have the same **frequency**, order them by the position of their **first occurrence** in `s`.

Return the modified string.

Vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

The **frequency** of a letter is the number of times it occurs in the string.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters

## Examples
### Example 1
- **Input:** `s = "leetcode"`
- **Output:** `"leetcedo"`
- **Explanation:** ​​​​​​​ 

 
 Vowels in the string are `['e', 'e', 'o', 'e']` with frequencies: `e = 3`, `o = 1`. 
 Sorting in non-increasing order of frequency and placing them back into the vowel positions results in `"leetcedo"`.

### Example 2
- **Input:** `s = "aeiaaioooa"`
- **Output:** `"aaaaoooiie"`
- **Explanation:** ​​​​​​​ 

 
 Vowels in the string are `['a', 'e', 'i', 'a', 'a', 'i', 'o', 'o', 'o', 'a']` with frequencies: `a = 4`, `o = 3`, `i = 2`, `e = 1`. 
 Sorting them in non-increasing order of frequency and placing them back into the vowel positions results in `"aaaaoooiie"`.

### Example 3
- **Input:** `s = "baeiou"`
- **Output:** `"baeiou"`
- **Explanation:** Each vowel appears exactly once, so all have the same frequency. 
 Thus, they retain their relative order based on first occurrence, and the string remains unchanged.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Sort Vowels by Frequency**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "leetcode"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"leetcedo"`.
4. **Verification:** ​​​​​​​ 

 
 Vowels in the string are `['e', 'e', 'o', 'e']` with frequencies: `e = 3`, `o = 1`. 
 Sorting in non-increasing order of frequency and placing them back into the vowel positions results in `"leetcedo"`.

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
var sortVowels = function(s) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    const freq = new Map();

    // Count vowel frequencies
    for (const ch of s) {
        if (vowels.has(ch)) {
            freq.set(ch, (freq.get(ch) || 0) + 1);
        }
    }

    // Sort vowels by frequency (descending)
    // Stable tie-breaking: first occurrence in original string
    const sorted = [...freq.keys()].sort((a, b) => {
        return freq.get(b) - freq.get(a);
    });

    // Build sorted vowel sequence
    let vowelString = '';

    for (const ch of sorted) {
        vowelString += ch.repeat(freq.get(ch));
    }

    // Replace only vowel positions
    let index = 0;
    const result = [];

    for (const ch of s) {
        if (vowels.has(ch)) {
            result.push(vowelString[index++]);
        } else {
            result.push(ch);
        }
    }

    return result.join('');
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
- [451. Sort Characters By Frequency](../../0001-0500/0451-sort-characters-by-frequency/)
- [1636. Sort Array by Increasing Frequency](../../1501-2000/1636-sort-array-by-increasing-frequency/)
- [75. Sort Colors](../../0001-0500/0075-sort-colors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-vowels-by-frequency/)
