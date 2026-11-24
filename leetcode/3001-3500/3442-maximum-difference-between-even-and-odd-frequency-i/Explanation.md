# LeetCode 3442: Maximum Difference Between Even and Odd Frequency I

**LeetCode Problem #3442 — Maximum Difference Between Even and Odd Frequency I**
Solve LeetCode Maximum Difference Between Even and Odd Frequency I using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Difference Between Even and Odd Frequency I |
| LeetCode | #3442 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters.

Your task is to find the **maximum** difference `diff = freq(a_1) - freq(a_2)` between the frequency of characters `a_1` and `a_2` in the string such that:

`a_1` has an **odd frequency** in the string. 
 `a_2` has an **even frequency** in the string.

Return this **maximum** difference.

## Constraints
- `3 <= s.length <= 100`
- `s` consists only of lowercase English letters.
- `s` contains at least one character with an odd frequency and one with an even frequency.

## Examples
### Example 1
- **Input:** `s = "aaaaabbc"`
- **Output:** `3`
- **Explanation:** The character `'a'` has an

### Example 2
- **Input:** `s = "abcabcab"`
- **Output:** `1`
- **Explanation:** The character `'a'` has an

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Difference Between Even and Odd Frequency I**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aaaaabbc"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The character `'a'` has an

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
var maxDifference = function(s) {
    let freq = Array(26).fill(0);

    // Count character frequencies
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    let maxOdd = 0;
    let minEven = Infinity;

    // Find maximum odd frequency and minimum even frequency
    for (const f of freq) {
        if (f === 0) continue;

        if (f % 2 === 1) {
            maxOdd = Math.max(maxOdd, f);
        } else {
            minEven = Math.min(minEven, f);
        }
    }

    return maxOdd - minEven;
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
- [3445. Maximum Difference Between Even and Odd Frequency II](../../3001-3500/3445-maximum-difference-between-even-and-odd-frequency-ii/)
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1026-maximum-difference-between-node-and-ancestor/)
- [1913. Maximum Product Difference Between Two Pairs](../../1501-2000/1913-maximum-product-difference-between-two-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)
