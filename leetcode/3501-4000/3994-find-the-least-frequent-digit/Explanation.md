# LeetCode 3663: Find The Least Frequent Digit

**LeetCode Problem #3663 — Find The Least Frequent Digit**
Solve LeetCode Find The Least Frequent Digit using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find The Least Frequent Digit |
| LeetCode | #3663 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer `n`, find the digit that occurs **least** frequently in its decimal representation. If multiple digits have the same frequency, choose the **smallest** digit.

Return the chosen digit as an integer.

The **frequency** of a digit `x` is the number of times it appears in the decimal representation of `n`.

## Constraints
- `1 <= n <= 2^31​​​​​​​ - 1`

## Examples
### Example 1
- **Input:** `n = 1553322`
- **Output:** `1`
- **Explanation:** The least frequent digit in `n` is 1, which appears only once. All other digits appear twice.

### Example 2
- **Input:** `n = 723344511`
- **Output:** `2`
- **Explanation:** The least frequent digits in `n` are 7, 2, and 5; each appears only once.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find The Least Frequent Digit**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1553322`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The least frequent digit in `n` is 1, which appears only once. All other digits appear twice.

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
var getLeastFrequentDigit = function(n) {
    let freq = new Array(10).fill(0);

    // Count the frequency of each digit
    for (const digit of String(n)) {
        freq[Number(digit)]++;
    }

    let minFreq = Infinity;
    let result = 0;

    // Find the least frequent digit
    for (let i = 0; i <= 9; i++) {
        if (freq[i] > 0 && freq[i] < minFreq) {
            minFreq = freq[i];
            result = i;
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
- [3541. Find Most Frequent Vowel and Consonant](../../3501-4000/3872-find-most-frequent-vowel-and-consonant/)
- [395. Longest Substring with At Least K Repeating Characters](../../0001-0500/0395-longest-substring-with-at-least-k-repeating-characters/)
- [570. Managers with at Least 5 Direct Reports](../../0501-1000/0570-managers-with-at-least-5-direct-reports/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-least-frequent-digit/)
