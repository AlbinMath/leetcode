# LeetCode 835: Image Overlap

**LeetCode Problem #835 — Image Overlap**
Solve LeetCode Image Overlap using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n²) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Image Overlap |
| LeetCode | #835 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n²) |
| Space Complexity | O(1) |

## Problem Statement
You are given two images, `img1` and `img2`, represented as binary, square matrices of size `n x n`. A binary matrix has only `0`s and `1`s as values.

We **translate** one image however we choose by sliding all the `1` bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the **overlap** by counting the number of positions that have a `1` in **both** images.

Note also that a translation does **not** include any kind of rotation. Any `1` bits that are translated outside of the matrix borders are erased.

Return *the largest possible overlap*.

## Constraints
- `n == img1.length == img1[i].length`
- `n == img2.length == img2[i].length`
- `1 <= n <= 30`
- `img1[i][j]` is either `0` or `1`.
- `img2[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]`
- **Output:** `3`
- **Explanation:** We translate img1 to right by 1 unit and down by 1 unit.
 
The number of positions that have a 1 in both images is 3 (shown in red).

### Example 2
- **Input:** `img1 = [[1]], img2 = [[1]]`
- **Output:** `1`

### Example 3
- **Input:** `img1 = [[0]], img2 = [[0]]`
- **Output:** `0`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **brute force** approach, trying every possible translation.

1. It iterates over all possible row shifts `dr` from `-(n-1)` to `(n-1)` and column shifts `dc` from `-(n-1)` to `(n-1)`.
2. For each translation `(dr, dc)`, it counts how many positions `(i, j)` in `img1` have `img1[i][j] == 1` and `img2[i+dr][j+dc] == 1` (only when the translated position is within bounds).
3. It tracks the maximum overlap across all translations.

Time complexity is $O(N^4)$ (trying $O(N^2)$ translations, each requiring an $O(N^2)$ comparison) and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We translate img1 to right by 1 unit and down by 1 unit.
 
The number of positions that have a 1 in both images is 3 (shown in red).

## Complexity Analysis
- **Time Complexity:** O(n²) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[][]} img1
 * @param {number[][]} img2
 * @return {number}
 */
var largestOverlap = function(img1, img2) {
    const n = img1.length;
    let maxOverlap = 0;

    // Try every possible translation
    for (let dr = -(n - 1); dr <= n - 1; dr++) {
        for (let dc = -(n - 1); dc <= n - 1; dc++) {

            let overlap = 0;

            for (let i = 0; i < n; i++) {
                for (let j = 0; j < n; j++) {

                    let x = i + dr;
                    let y = j + dc;

                    // Check if translated position is inside img2
                    if (x >= 0 && x < n && y >= 0 && y < n) {
                        if (img1[i][j] === 1 && img2[x][y] === 1) {
                            overlap++;
                        }
                    }
                }
            }

            maxOverlap = Math.max(maxOverlap, overlap);
        }
    }

    return maxOverlap;
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [48. Rotate Image](../../0001-0500/0048-rotate-image/)
- [661. Image Smoother](../../0501-1000/0661-image-smoother/)
- [832. Flipping an Image](../../0501-1000/0832-flipping-an-image/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/image-overlap/)
