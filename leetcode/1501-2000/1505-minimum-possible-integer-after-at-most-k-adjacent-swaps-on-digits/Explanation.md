# LeetCode 1505: Minimum Possible Integer After at Most K Adjacent Swaps On Digits

**LeetCode Problem #1505 — Minimum Possible Integer After at Most K Adjacent Swaps On Digits**
Solve LeetCode Minimum Possible Integer After at Most K Adjacent Swaps On Digits using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Possible Integer After at Most K Adjacent Swaps On Digits |
| LeetCode | #1505 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `num` representing **the digits** of a very large integer and an integer `k`. You are allowed to swap any two adjacent digits of the integer **at most** `k` times.

Return *the minimum integer you can obtain also as a string*.

## Constraints
- `1 <= num.length <= 3 * 10^4`
- `num` consists of only **digits** and does not contain **leading zeros**.
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `num = "4321", k = 4`
- **Output:** `"1342"`
- **Explanation:** The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.

### Example 2
- **Input:** `num = "100", k = 1`
- **Output:** `"010"`
- **Explanation:** It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.

### Example 3
- **Input:** `num = "36789", k = 1000`
- **Output:** `"36789"`
- **Explanation:** We can keep the number without any swaps.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Possible Integer After at Most K Adjacent Swaps On Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = "4321", k = 4`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"1342"`.
4. **Verification:** The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minInteger = function(num, k) {
    const n = num.length;

    // Store the original positions of each digit
    const positions = Array.from({ length: 10 }, () => []);

    for (let i = 0; i < n; i++) {
        positions[Number(num[i])].push(i);
    }

    // Fenwick Tree: tracks digits already removed
    const bit = new Array(n + 1).fill(0);

    function update(index, delta) {
        index++; // Convert to 1-based indexing

        while (index <= n) {
            bit[index] += delta;
            index += index & -index;
        }
    }

    function query(index) {
        // Count removed positions strictly before index
        let sum = 0;

        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }

        return sum;
    }

    const used = new Array(10).fill(0);
    let result = "";

    for (let step = 0; step < n; step++) {
        let chosen = false;

        // Try digits from smallest to largest
        for (let digit = 0; digit <= 9; digit++) {
            if (used[digit] >= positions[digit].length) {
                continue;
            }

            const originalIndex = positions[digit][used[digit]];

            // Remaining swaps needed to move this digit forward
            const cost = originalIndex - query(originalIndex);

            if (cost <= k) {
                k -= cost;
                result += digit;
                used[digit]++;
                update(originalIndex, 1);
                chosen = true;
                break;
            }
        }

        if (!chosen) break;
    }

    return result;
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](../../1501-2000/1703-minimum-adjacent-swaps-for-k-consecutive-ones/)
- [3962. Maximum Subarray Sum After at Most K Swaps](../../3501-4000/3962-maximum-subarray-sum-after-at-most-k-swaps/)
- [1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number](../../1501-2000/1850-minimum-adjacent-swaps-to-reach-the-kth-smallest-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
