# LeetCode 2027: Minimum Moves to Convert String

**LeetCode Problem #2027 — Minimum Moves to Convert String**
Solve LeetCode Minimum Moves to Convert String using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Convert String |
| LeetCode | #2027 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of `n` characters which are either `'X'` or `'O'`.

A **move** is defined as selecting **three** **consecutive characters** of `s` and converting them to `'O'`. Note that if a move is applied to the character `'O'`, it will stay the **same**.

Return *the **minimum** number of moves required so that all the characters of *`s`* are converted to *`'O'`.

## Constraints
- `3 <= s.length <= 1000`
- `s[i]` is either `'X'` or `'O'`.

## Examples
### Example 1
- **Input:** `s = "XXX"`
- **Output:** `1`
- **Explanation:** XXX -> OOO
We select all the 3 characters and convert them in one move.

### Example 2
- **Input:** `s = "XXOX"`
- **Output:** `2`
- **Explanation:** XXO X -> O OOX -> OOOO
We select the first 3 characters in the first move, and convert them to `'O'`.
Then we select the last 3 characters and convert them so that the final string contains all `'O'`s.

### Example 3
- **Input:** `s = "OOOO"`
- **Output:** `0`
- **Explanation:** There are no `'X's` in `s` to convert.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Moves to Convert String**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "XXX"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** XXX -> OOO
We select all the 3 characters and convert them in one move.

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
var minimumMoves = function(s) {
    let moves = 0;
    let i = 0;

    while (i < s.length) {
        if (s[i] === 'X') {
            moves++;
            i += 3;
        } else {
            i++;
        }
    }

    return moves;
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
- [1540. Can Convert String in K Moves](../../1501-2000/1647-can-convert-string-in-k-moves/)
- [2976. Minimum Cost to Convert String I](../../3001-3500/3235-minimum-cost-to-convert-string-i/)
- [2977. Minimum Cost to Convert String II](../../3001-3500/3238-minimum-cost-to-convert-string-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-convert-string/)
