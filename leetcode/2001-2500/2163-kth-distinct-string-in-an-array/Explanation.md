# LeetCode 2053: Kth Distinct String in an Array

**LeetCode Problem #2053 — Kth Distinct String in an Array**
Solve LeetCode Kth Distinct String in an Array using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Distinct String in an Array |
| LeetCode | #2053 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A **distinct string** is a string that is present only **once** in an array.

Given an array of strings `arr`, and an integer `k`, return *the *`k^th`* **distinct string** present in *`arr`. If there are **fewer** than `k` distinct strings, return *an **empty string ***`""`.

Note that the strings are considered in the **order in which they appear** in the array.

## Constraints
- `1 <= k <= arr.length <= 1000`
- `1 <= arr[i].length <= 5`
- `arr[i]` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `arr = ["d","b","c","b","c","a"], k = 2`
- **Output:** `"a"`
- **Explanation:** The only distinct strings in arr are "d" and "a".
"d" appears 1^st, so it is the 1^st distinct string.
"a" appears 2^nd, so it is the 2^nd distinct string.
Since k == 2, "a" is returned.

### Example 2
- **Input:** `arr = ["aaa","aa","a"], k = 1`
- **Output:** `"aaa"`
- **Explanation:** All strings in arr are distinct, so the 1^st string "aaa" is returned.

### Example 3
- **Input:** `arr = ["a","b","a"], k = 3`
- **Output:** `""`
- **Explanation:** The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Kth Distinct String in an Array**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = ["d","b","c","b","c","a"], k = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"a"`.
4. **Verification:** The only distinct strings in arr are "d" and "a".
"d" appears 1^st, so it is the 1^st distinct string.
"a" appears 2^nd, so it is the 2^nd distinct string.
Since k == 2, "a" is returned.

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
var kthDistinct = function(arr, k) {
    const freq = new Map();

    // Count the frequency of each string.
    for (const str of arr) {
        freq.set(str, (freq.get(str) || 0) + 1);
    }

    // Find the kth distinct string in original order.
    for (const str of arr) {
        if (freq.get(str) === 1) {
            k--;

            if (k === 0) {
                return str;
            }
        }
    }

    return "";
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
- [2521. Distinct Prime Factors of Product of Array](../../2501-3000/2609-distinct-prime-factors-of-product-of-array/)
- [3659. Partition Array Into K-Distinct Groups](../../3501-4000/3979-partition-array-into-k-distinct-groups/)
- [4065. Rearrange Array by Removing Distinct Values](../../4001-4500/4429-rearrange-array-by-removing-distinct-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-distinct-string-in-an-array/)
