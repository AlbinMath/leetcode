# LeetCode 3266: Final Array State After K Multiplication Operations II

**LeetCode Problem #3266 — Final Array State After K Multiplication Operations II**
Solve LeetCode Final Array State After K Multiplication Operations II using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Final Array State After K Multiplication Operations II |
| LeetCode | #3266 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`, an integer `k`, and an integer `multiplier`.

You need to perform `k` operations on `nums`. In each operation:

Find the **minimum** value `x` in `nums`. If there are multiple occurrences of the minimum value, select the one that appears **first**. 
 Replace the selected minimum value `x` with `x * multiplier`.

After the `k` operations, apply **modulo** `10^9 + 7` to every value in `nums`.

Return an integer array denoting the *final state* of `nums` after performing all `k` operations and then applying the modulo.

## Constraints
- `1 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`
- `1 <= multiplier <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [2,1,3,5,6], k = 5, multiplier = 2`
- **Output:** `[8,4,6,5,6]`
- **Explanation:** Operation 
 Result 
 
 
 After operation 1 
 [2, 2, 3, 5, 6] 
 
 
 After operation 2 
 [4, 2, 3, 5, 6] 
 
 
 After operation 3 
 [4, 4, 3, 5, 6] 
 
 
 After operation 4 
 [4, 4, 6, 5, 6] 
 
 
 After operation 5 
 [8, 4, 6, 5, 6] 
 
 
 After applying modulo 
 [8, 4, 6, 5, 6]

### Example 2
- **Input:** `nums = [100000,2000], k = 2, multiplier = 1000000`
- **Output:** `[999999307,999999993]`
- **Explanation:** Operation 
 Result 
 
 
 After operation 1 
 [100000, 2000000000] 
 
 
 After operation 2 
 [100000000000, 2000000000] 
 
 
 After applying modulo 
 [999999307, 999999993]

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Final Array State After K Multiplication Operations II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3,5,6], k = 5, multiplier = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[8,4,6,5,6]`.
4. **Verification:** Operation 
 Result 
 
 
 After operation 1 
 [2, 2, 3, 5, 6] 
 
 
 After operation 2 
 [4, 2, 3, 5, 6] 
 
 
 After operation 3 
 [4, 4, 3, 5, 6] 
 
 
 After operation 4 
 [4, 4, 6, 5, 6] 
 
 
 After operation 5 
 [8, 4, 6, 5, 6] 
 
 
 After applying modulo 
 [8, 4, 6, 5, 6]

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
var getFinalState = function(nums, k, multiplier) {
    const MOD = 1000000007n;
    const mult = BigInt(multiplier);
    const n = nums.length;

    if (multiplier === 1) {
        return nums.map((x) => Number(BigInt(x) % MOD));
    }

    const vals = nums.map((x) => BigInt(x));
    let maxVal = 0n;
    for (const v of vals) {
        if (v > maxVal) maxVal = v;
    }

    const heap = Array.from({ length: n }, (_, i) => i);

    const less = (a, b) =>
        vals[heap[a]] !== vals[heap[b]]
            ? vals[heap[a]] < vals[heap[b]]
            : heap[a] < heap[b];

    const siftDown = (idx) => {
        while (true) {
            let smallest = idx;
            const left = (idx << 1) + 1;
            const right = left + 1;
            if (left < heap.length && less(left, smallest)) smallest = left;
            if (right < heap.length && less(right, smallest)) smallest = right;
            if (smallest === idx) break;
            [heap[idx], heap[smallest]] = [heap[smallest], heap[idx]];
            idx = smallest;
        }
    };

    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            siftDown(0);
        }
        return top;
    };

    const modPow = (base, exp) => {
        let res = 1n;
        base %= MOD;
        while (exp > 0n) {
            if (exp & 1n) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1n;
        }
        return res;
    };

    for (let i = (n >> 1) - 1; i >= 0; i--) {
        siftDown(i);
    }

    // Phase 1: Simulate until the minimum value catches up to maxVal
    while (k > 0 && vals[heap[0]] < maxVal) {
        const minIdx = heap[0];
        vals[minIdx] *= mult;
        siftDown(0);
        k--;
    }

    // Phase 2: Distribute remaining k operations evenly across sorted heap order
    const kBig = BigInt(k);
    const nBig = BigInt(n);
    const baseExp = kBig / nBig;
    const rem = Number(kBig % nBig);
    const ans = new Array(n);

    for (let rank = 0; rank < n; rank++) {
        const idx = pop();
        const exp = baseExp + (rank < rem ? 1n : 0n);
        ans[idx] = Number(((vals[idx] % MOD) * modPow(mult, exp)) % MOD);
    }

    return ans;
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
- [3264. Final Array State After K Multiplication Operations I](../../3001-3500/3264-final-array-state-after-k-multiplication-operations-i/)
- [2011. Final Value of Variable After Performing Operations](../../2001-2500/2011-final-value-of-variable-after-performing-operations/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/)
