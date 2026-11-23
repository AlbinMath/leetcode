# LeetCode 3044: Most Frequent Prime

**LeetCode Problem #3044 — Most Frequent Prime**
Solve LeetCode Most Frequent Prime using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Frequent Prime |
| LeetCode | #3044 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a `m x n` **0-indexed **2D** **matrix `mat`. From every cell, you can create numbers in the following way:

There could be at most `8` paths from the cells namely: east, south-east, south, south-west, west, north-west, north, and north-east. 
 Select a path from them and append digits in this path to the number being formed by traveling in this direction. 
 Note that numbers are generated at every step, for example, if the digits along the path are `1, 9, 1`, then there will be three numbers generated along the way: `1, 19, 191`.

Return *the most frequent prime number **greater** than *`10`* out of all the numbers created by traversing the matrix or *`-1`* if no such prime number exists. If there are multiple prime numbers with the highest frequency, then return the largest among them.*

**Note:** It is invalid to change the direction during the move.

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 6`
- `1 <= mat[i][j] <= 9`

## Examples
### Example 1
- **Input:** `mat = [[1,1],[9,9],[1,1]]`
- **Output:** `19`
- **Explanation:** From cell (0,0) there are 3 possible directions and the numbers greater than 10 which can be created in those directions are:
East: [11], South-East: [19], South: [19,191].
Numbers greater than 10 created from the cell (0,1) in all possible directions are: [19,191,19,11].
Numbers greater than 10 created from the cell (1,0) in all possible directions are: [99,91,91,91,91].
Numbers greater than 10 created from the cell (1,1) in all possible directions are: [91,91,99,91,91].
Numbers greater than 10 created from the cell (2,0) in all possible directions are: [11,19,191,19].
Numbers greater than 10 created from the cell (2,1) in all possible directions are: [11,19,19,191].
The most frequent prime number among all the created numbers is 19.

### Example 2
- **Input:** `mat = [[7]]`
- **Output:** `-1`
- **Explanation:** The only number which can be formed is 7. It is a prime number however it is not greater than 10, so return -1.

### Example 3
- **Input:** `mat = [[9,7,8],[4,6,5],[2,8,6]]`
- **Output:** `97`
- **Explanation:** Numbers greater than 10 created from the cell (0,0) in all possible directions are: [97,978,96,966,94,942].
Numbers greater than 10 created from the cell (0,1) in all possible directions are: [78,75,76,768,74,79].
Numbers greater than 10 created from the cell (0,2) in all possible directions are: [85,856,86,862,87,879].
Numbers greater than 10 created from the cell (1,0) in all possible directions are: [46,465,48,42,49,47].
Numbers greater than 10 created from the cell (1,1) in all possible directions are: [65,66,68,62,64,69,67,68].
Numbers greater than 10 created from the cell (1,2) in all possible directions are: [56,58,56,564,57,58].
Numbers greater than 10 created from the cell (2,0) in all possible directions are: [28,286,24,249,26,268].
Numbers greater than 10 created from the cell (2,1) in all possible directions are: [86,82,84,86,867,85].
Numbers greater than 10 created from the cell (2,2) in all possible directions are: [68,682,66,669,65,658].
The most frequent prime number among all the created numbers is 97.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Most Frequent Prime**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,1],[9,9],[1,1]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `19`.
4. **Verification:** From cell (0,0) there are 3 possible directions and the numbers greater than 10 which can be created in those directions are:
East: [11], South-East: [19], South: [19,191].
Numbers greater than 10 created from the cell (0,1) in all possible directions are: [19,191,19,11].
Numbers greater than 10 created from the cell (1,0) in all possible directions are: [99,91,91,91,91].
Numbers greater than 10 created from the cell (1,1) in all possible directions are: [91,91,99,91,91].
Numbers greater than 10 created from the cell (2,0) in all possible directions are: [11,19,191,19].
Numbers greater than 10 created from the cell (2,1) in all possible directions are: [11,19,19,191].
The most frequent prime number among all the created numbers is 19.

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
var mostFrequentPrime = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const freq = new Map();

    const directions = [
        [0, 1],   // East
        [1, 1],   // South-east
        [1, 0],   // South
        [1, -1],  // South-west
        [0, -1],  // West
        [-1, -1], // North-west
        [-1, 0],  // North
        [-1, 1]   // North-east
    ];

    const isPrime = (num) => {
        if (num < 2) return false;
        if (num === 2) return true;
        if (num % 2 === 0) return false;

        for (let i = 3; i * i <= num; i += 2) {
            if (num % i === 0) return false;
        }

        return true;
    };

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            for (const [dr, dc] of directions) {
                let row = r;
                let col = c;
                let num = 0;

                while (
                    row >= 0 && row < m &&
                    col >= 0 && col < n
                ) {
                    num = num * 10 + mat[row][col];

                    if (num > 10 && isPrime(num)) {
                        freq.set(num, (freq.get(num) || 0) + 1);
                    }

                    row += dr;
                    col += dc;
                }
            }
        }
    }

    let answer = -1;
    let maxFrequency = 0;

    for (const [prime, count] of freq) {
        if (
            count > maxFrequency ||
            (count === maxFrequency && prime > answer)
        ) {
            answer = prime;
            maxFrequency = count;
        }
    }

    return answer;
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
- [508. Most Frequent Subtree Sum](../../0501-1000/0508-most-frequent-subtree-sum/)
- [1838. Frequency of the Most Frequent Element](../../1501-2000/1966-frequency-of-the-most-frequent-element/)
- [4032. Longest Subarray With at Most K Distinct Prime Factors](../../4001-4500/4370-longest-subarray-with-at-most-k-distinct-prime-factors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-frequent-prime/)
