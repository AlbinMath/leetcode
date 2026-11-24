# LeetCode 3692: Majority Frequency Characters

**LeetCode Problem #3692 — Majority Frequency Characters**
Solve LeetCode Majority Frequency Characters using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Majority Frequency Characters |
| LeetCode | #3692 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters.

The **frequency group** for a value `k` is the set of characters that appear exactly `k` times in s.

The **majority frequency group** is the frequency group that contains the largest number of **distinct** characters.

Return a string containing all characters in the majority frequency group, in **any** order. If two or more frequency groups tie for that largest size, pick the group whose frequency `k` is **larger**.

## Constraints
- `1 <= s.length <= 100`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aaabbbccdddde"`
- **Output:** `"ab"`
- **Explanation:** Frequency (k) 
 Distinct characters in group 
 Group size 
 Majority? 
 
 
 
 
 4 
 {d} 
 1 
 No 
 
 
 3 
 {a, b} 
 2

### Example 2
- **Input:** `s = "abcd"`
- **Output:** `"abcd"`
- **Explanation:** Frequency (k) 
 Distinct characters in group 
 Group size 
 Majority? 
 
 
 
 
 1 
 {a, b, c, d} 
 4

### Example 3
- **Input:** `s = "pfpfgi"`
- **Output:** `"fp"`
- **Explanation:** Frequency (k) 
 Distinct characters in group 
 Group size 
 Majority? 
 
 
 
 
 2 
 {p, f} 
 2

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Majority Frequency Characters**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aaabbbccdddde"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"ab"`.
4. **Verification:** Frequency (k) 
 Distinct characters in group 
 Group size 
 Majority? 
 
 
 
 
 4 
 {d} 
 1 
 No 
 
 
 3 
 {a, b} 
 2

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
var majorityFrequencyGroup = function(s) {
    const freq = new Array(26).fill(0);

    // Step 1: Count frequency of each character
    for (let ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    // Step 2: Group characters by their frequency
    const groups = new Map();

    for (let i = 0; i < 26; i++) {
        if (freq[i] > 0) {
            if (!groups.has(freq[i])) {
                groups.set(freq[i], []);
            }

            groups.get(freq[i]).push(String.fromCharCode(i + 97));
        }
    }

    // Step 3: Find the majority frequency group
    let result = "";
    let maxSize = 0;
    let maxFreq = 0;

    for (let [frequency, chars] of groups) {
        if (
            chars.length > maxSize ||
            (chars.length === maxSize && frequency > maxFreq)
        ) {
            maxSize = chars.length;
            maxFreq = frequency;
            result = chars.join("");
        }
    }

    return result;
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
- [3325. Count Substrings With K-Frequency Characters I](../../3001-3500/3325-count-substrings-with-k-frequency-characters-i/)
- [192. Word Frequency](../../0001-0500/0192-word-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/majority-frequency-characters/)
