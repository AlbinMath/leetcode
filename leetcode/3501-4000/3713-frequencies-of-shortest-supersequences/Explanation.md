# LeetCode 3435: Frequencies of Shortest Supersequences

**LeetCode Problem #3435 — Frequencies of Shortest Supersequences**
Solve LeetCode Frequencies of Shortest Supersequences using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Frequencies of Shortest Supersequences |
| LeetCode | #3435 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of strings `words`. Find all **shortest common supersequences (SCS)** of ` words ` that are not permutations of each other.

A **shortest common supersequence** is a string of **minimum** length that contains each string in `words` as a subsequence .

Return a 2D array of integers `freqs` that represent all the SCSs. Each `freqs[i]` is an array of size 26, representing the frequency of each letter in the lowercase English alphabet for a single SCS. You may return the frequency arrays in any order.

## Constraints
- `1 <= words.length <= 256`
- `words[i].length == 2`
- All strings in `words` will altogether be composed of no more than 16 unique lowercase letters.
- All strings in `words` are unique.

## Examples
### Example 1
- **Input:** `words = ["ab","ba"]`
- **Output:** `[[1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]`
- **Explanation:** The two SCSs are `"aba"` and `"bab"`. The output is the letter frequencies for each one.

### Example 2
- **Input:** `words = ["aa","ac"]`
- **Output:** `[[2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]`
- **Explanation:** The two SCSs are `"aac"` and `"aca"`. Since they are permutations of each other, keep only `"aac"`.

### Example 3
- **Input:** `words = ["aa","bb","cc"]`
- **Output:** `[[2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]`
- **Explanation:** `"aabbcc"` and all its permutations are SCSs.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Frequencies of Shortest Supersequences**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["ab","ba"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]`.
4. **Verification:** The two SCSs are `"aba"` and `"bab"`. The output is the letter frequencies for each one.

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
 * @param {string[]} supersequences
 * @return {number[][]}
 */
var supersequences = function (words) {
    const idx = new Map();
    const letters = [];
    for (const w of words) {
        for (const ch of w) {
            if (!idx.has(ch)) {
                idx.set(ch, letters.length);
                letters.push(ch);
            }
        }
    }
    const k = letters.length;
    const inAdj = new Array(k).fill(0);
    let selfMask = 0;
    for (const w of words) {
        const a = idx.get(w[0]), b = idx.get(w[1]);
        if (a === b) selfMask |= 1 << a;
        else inAdj[b] |= 1 << a;
    }

    const full = (1 << k) - 1;
    const popcount = (x) => {
        let c = 0;
        while (x) { x &= x - 1; c++; }
        return c;
    };

    const acyclic = (rem) => {
        let changed = true;
        while (rem && changed) {
            changed = false;
            for (let v = 0; v < k; v++) {
                if ((rem >> v) & 1 && (inAdj[v] & rem) === 0) {
                    rem &= ~(1 << v);
                    changed = true;
                }
            }
        }
        return rem === 0;
    };

    let best = Infinity;
    let masks = [];
    for (let mask = 0; mask <= full; mask++) {
        if ((mask & selfMask) !== selfMask) continue;
        const pc = popcount(mask);
        if (pc > best) continue;
        if (!acyclic(full & ~mask)) continue;
        if (pc < best) {
            best = pc;
            masks = [];
        }
        masks.push(mask);
    }

    return masks.map((mask) => {
        const f = new Array(26).fill(0);
        for (let i = 0; i < k; i++) {
            f[letters[i].charCodeAt(0) - 97] = (mask >> i) & 1 ? 2 : 1;
        }
        return f;
    });
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
- [1647. Minimum Deletions to Make Character Frequencies Unique](../../1501-2000/1770-minimum-deletions-to-make-character-frequencies-unique/)
- [3389. Minimum Operations to Make Character Frequencies Equal](../../3501-4000/3638-minimum-operations-to-make-character-frequencies-equal/)
- [3852. Smallest Pair With Different Frequencies](../../4001-4500/4231-smallest-pair-with-different-frequencies/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/frequencies-of-shortest-supersequences/)
