# LeetCode 3805: Count Caesar Cipher Pairs

**LeetCode Problem #3805 — Count Caesar Cipher Pairs**
Solve LeetCode Count Caesar Cipher Pairs using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Caesar Cipher Pairs |
| LeetCode | #3805 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `words` of `n` strings. Each string has length `m` and contains only lowercase English letters.

Two strings `s` and `t` are **similar** if we can apply the following operation any number of times (possibly zero times) so that `s` and `t` become **equal**.

Choose either `s` or `t`. 
 Replace **every** letter in the chosen string with the next letter in the alphabet cyclically. The next letter after `'z'` is `'a'`.

Count the number of pairs of indices `(i, j)` such that:

`i < j` 
 `words[i]` and `words[j]` are **similar**.

Return an integer denoting the number of such pairs.

## Constraints
- `1 <= n == words.length <= 10^5`
- `1 <= m == words[i].length <= 10^5`
- `1 <= n * m <= 10^5`
- `words[i]` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `words = ["fusion","layout"]`
- **Output:** `1`
- **Explanation:** `words[0] = "fusion"` and `words[1] = "layout"` are similar because we can apply the operation to `"fusion"` 6 times. The string `"fusion"` changes as follows. 

 
 `"fusion"` 
 `"gvtjpo"` 
 `"hwukqp"` 
 `"ixvlrq"` 
 `"jywmsr"` 
 `"kzxnts"` 
 `"layout"`

### Example 2
- **Input:** `words = ["ab","aa","za","aa"]`
- **Output:** `2`
- **Explanation:** `words[0] = "ab"` and `words[2] = "za"` are similar. `words[1] = "aa"` and `words[3] = "aa"` are similar.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Caesar Cipher Pairs**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["fusion","layout"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** `words[0] = "fusion"` and `words[1] = "layout"` are similar because we can apply the operation to `"fusion"` 6 times. The string `"fusion"` changes as follows. 

 
 `"fusion"` 
 `"gvtjpo"` 
 `"hwukqp"` 
 `"ixvlrq"` 
 `"jywmsr"` 
 `"kzxnts"` 
 `"layout"`

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
var countPairs = function(words) {
    const map = new Map();
    let ans = 0;

    for (let word of words) {
        let key = "";
        const first = word.charCodeAt(0);

        // Normalize each character
        for (let ch of word) {
            let diff = (ch.charCodeAt(0) - first + 26) % 26;
            key += diff + ",";
        }

        // Count previous similar strings
        ans += map.get(key) || 0;

        // Update frequency
        map.set(key, (map.get(key) || 0) + 1);
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
- [1782. Count Pairs Of Nodes](../../1501-2000/1782-count-pairs-of-nodes/)
- [1803. Count Pairs With XOR in a Range](../../1501-2000/1803-count-pairs-with-xor-in-a-range/)
- [1814. Count Nice Pairs in an Array](../../1501-2000/1814-count-nice-pairs-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-caesar-cipher-pairs/)
