# LeetCode 1395: Count Number of Teams

**LeetCode Problem #1395 — Count Number of Teams**
Solve LeetCode Count Number of Teams using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Teams |
| LeetCode | #1395 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` soldiers standing in a line. Each soldier is assigned a **unique** `rating` value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (`i`, `j`, `k`) with rating (`rating[i]`, `rating[j]`, `rating[k]`). 
 A team is valid if: (`rating[i] < rating[j] < rating[k]`) or (`rating[i] > rating[j] > rating[k]`) where (`0 <= i < j < k < n`).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

## Constraints
- `n == rating.length`
- `3 <= n <= 1000`
- `1 <= rating[i] <= 10^5`
- All the integers in `rating` are **unique**.

## Examples
### Example 1
- **Input:** `rating = [2,5,3,4,1]`
- **Output:** `3`
- **Explanation:** We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

### Example 2
- **Input:** `rating = [2,1,3]`
- **Output:** `0`
- **Explanation:** We can't form any team given the conditions.

### Example 3
- **Input:** `rating = [1,2,3,4]`
- **Output:** `4`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Number of Teams**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `rating = [2,5,3,4,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var numTeams = function(rating) {
    const n = rating.length;
    let teams = 0;

    for (let j = 1; j < n - 1; j++) {
        let leftSmaller = 0;
        let leftGreater = 0;
        let rightSmaller = 0;
        let rightGreater = 0;

        // Count ratings to the left of j
        for (let i = 0; i < j; i++) {
            if (rating[i] < rating[j]) {
                leftSmaller++;
            } else {
                leftGreater++;
            }
        }

        // Count ratings to the right of j
        for (let k = j + 1; k < n; k++) {
            if (rating[k] < rating[j]) {
                rightSmaller++;
            } else {
                rightGreater++;
            }
        }

        // Increasing and decreasing teams
        teams += leftSmaller * rightGreater;
        teams += leftGreater * rightSmaller;
    }

    return teams;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)
- [1684. Count the Number of Consistent Strings](../../1501-2000/1786-count-the-number-of-consistent-strings/)
- [1759. Count Number of Homogenous Substrings](../../1501-2000/1885-count-number-of-homogenous-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-teams/)
