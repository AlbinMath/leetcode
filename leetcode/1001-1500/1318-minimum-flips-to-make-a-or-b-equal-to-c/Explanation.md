# LeetCode 1318: Minimum Flips to Make a OR b Equal to c

**LeetCode Problem #1318 — Minimum Flips to Make a OR b Equal to c**
Solve LeetCode Minimum Flips to Make a OR b Equal to c using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Flips to Make a OR b Equal to c |
| LeetCode | #1318 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given 3 positives numbers `a`, `b` and `c`. Return the minimum flips required in some bits of `a` and `b` to make ( `a` OR `b` == `c` ). (bitwise OR operation). 
Flip operation consists of change **any** single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

## Constraints
- `1 <= a <= 10^9`
- `1 <= b <= 10^9`
- `1 <= c <= 10^9`

## Examples
### Example 1
- **Input:** `a = 2, b = 6, c = 5`
- **Output:** `3`
- **Explanation:** After flips a = 1 , b = 4 , c = 5 such that (`a` OR `b` == `c`)

### Example 2
- **Input:** `a = 4, b = 2, c = 7`
- **Output:** `1`

### Example 3
- **Input:** `a = 1, b = 2, c = 3`
- **Output:** `0`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Flips to Make a OR b Equal to c**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = 2, b = 6, c = 5`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** After flips a = 1 , b = 4 , c = 5 such that (`a` OR `b` == `c`)

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
var minFlips = function(a, b, c) {
    let flips = 0;

    while (a > 0 || b > 0 || c > 0) {
        const bitA = a & 1;
        const bitB = b & 1;
        const bitC = c & 1;

        if (bitC === 1) {
            if (bitA === 0 && bitB === 0) {
                flips++;
            }
        } else {
            flips += bitA + bitB;
        }

        a >>= 1;
        b >>= 1;
        c >>= 1;
    }

    return flips;
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
- [1247. Minimum Swaps to Make Strings Equal](../../1001-1500/1247-minimum-swaps-to-make-strings-equal/)
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../../1501-2000/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)
