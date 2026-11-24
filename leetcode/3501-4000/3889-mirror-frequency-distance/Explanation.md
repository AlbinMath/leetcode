# LeetCode 3889: Mirror Frequency Distance

**LeetCode Problem #3889 — Mirror Frequency Distance**
Solve LeetCode Mirror Frequency Distance using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Mirror Frequency Distance |
| LeetCode | #3889 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters and digits.

For each character, its **mirror character** is defined by reversing the order of its character set:

For letters, the mirror of a character is the letter at the same position from the end of the alphabet.
 
 For example, the mirror of `'a'` is `'z'`, and the mirror of `'b'` is `'y'`, and so on. 
 
 
 For digits, the mirror of a character is the digit at the same position from the end of the range `'0'` to `'9'`.
 
 For example, the mirror of `'0'` is `'9'`, and the mirror of `'1'` is `'8'`, and so on.

For each **unique** character `c` in the string:

Let `m` be its **mirror** character. 
 Let `freq(x)` denote the number of times character `x` appears in the string. 
 Compute the **absolute difference** between their **frequencies**, defined as: `|freq(c) - freq(m)|`

The mirror pairs `(c, m)` and `(m, c)` are the same and must be counted **only once**.

Return an integer denoting the total sum of these values over all such **distinct mirror pairs**.

## Constraints
- `1 <= s.length <= 5 * 10^5`
- `s` consists only of lowercase English letters and digits.

## Examples
### Example 1
- **Input:** `s = "ab1z9"`
- **Output:** `3`
- **Explanation:** For every mirror pair: 

 
 
 
 `c` 
 `m` 
 `freq(c)` 
 `freq(m)` 
 `|freq(c) - freq(m)|` 
 
 
 
 
 a 
 z 
 1 
 1 
 0 
 
 
 b 
 y 
 1 
 0 
 1 
 
 
 1 
 8 
 1 
 0 
 1 
 
 
 9 
 0 
 1 
 0 
 1 
 
 
 

 Thus, the answer is `0 + 1 + 1 + 1 = 3`.

### Example 2
- **Input:** `s = "4m7n"`
- **Output:** `2`
- **Explanation:** `c` 
 `m` 
 `freq(c)` 
 `freq(m)` 
 `|freq(c) - freq(m)|` 
 
 
 
 
 4 
 5 
 1 
 0 
 1 
 
 
 m 
 n 
 1 
 1 
 0 
 
 
 7 
 2 
 1 
 0 
 1 
 
 
 

 Thus, the answer is `1 + 0 + 1 = 2`.​​​​​​​

### Example 3
- **Input:** `s = "byby"`
- **Output:** `0`
- **Explanation:** `c` 
 `m` 
 `freq(c)` 
 `freq(m)` 
 `|freq(c) - freq(m)|` 
 
 
 
 
 b 
 y 
 2 
 2 
 0 
 
 
 

 Thus, the answer is 0.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Mirror Frequency Distance**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "ab1z9"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** For every mirror pair: 

 
 
 
 `c` 
 `m` 
 `freq(c)` 
 `freq(m)` 
 `|freq(c) - freq(m)|` 
 
 
 
 
 a 
 z 
 1 
 1 
 0 
 
 
 b 
 y 
 1 
 0 
 1 
 
 
 1 
 8 
 1 
 0 
 1 
 
 
 9 
 0 
 1 
 0 
 1 
 
 
 

 Thus, the answer is `0 + 1 + 1 + 1 = 3`.

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
var mirrorFrequency = function(s) {
    const freq = new Array(36).fill(0);

    // Count character frequencies
    for (const ch of s) {
        let idx = ch >= 'a'
            ? ch.charCodeAt(0) - 97
            : ch.charCodeAt(0) - 48 + 26;

        freq[idx]++;
    }

    let ans = 0;

    // Calculate mirror frequency differences
    for (let i = 0; i < 36; i++) {
        let mirror = i < 26 ? 25 - i : 61 - i;

        // Count each pair only once
        if (i < mirror) {
            ans += Math.abs(freq[i] - freq[mirror]);
        }
    }

    return ans;
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
- [858. Mirror Reflection](../../0501-1000/0858-mirror-reflection/)
- [2081. Sum of k-Mirror Numbers](../../2001-2500/2081-sum-of-k-mirror-numbers/)
- [3412. Find Mirror Score of a String](../../3001-3500/3412-find-mirror-score-of-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/mirror-frequency-distance/)
