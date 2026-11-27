# LeetCode 4099: Minimum Operations to Sort With Locked Indices

**LeetCode Problem #4099 — Minimum Operations to Sort With Locked Indices**
Solve LeetCode Minimum Operations to Sort With Locked Indices using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Sort With Locked Indices |
| LeetCode | #4099 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`, where `nums` is a ** permutation ** of the integers in the range `[1, n]`.

You are also given a **binary** array `locked` of length `n` and an integer `k`.

`locked[i] = 1` means index `i` is locked. 
 `locked[i] = 0` means index `i` is unlocked.

You may perform the following operations in **any order**:

**Swap:** Choose an index `i` such that both indices `i` and `i + 1` are currently unlocked, and swap `nums[i]` and `nums[i + 1]`. 
 **Unlock:** Choose an index `i` such that `locked[i] = 1` and **permanently** unlock it by setting `locked[i] = 0`.

You may perform any number of swap operations but **at most** `k` unlock operations.

Return the **minimum total number of operations** required to sort `nums` in ** strictly increasing ** order. If it is impossible, return -1.

## Constraints
- `1 <= n == nums.length == locked.length <= 2000`
- `1 <= nums[i] <= n`
- `0 <= locked[i] <= 1`
- `nums` is a permutation of the integers in the range `[1, n]`.
- `0 <= k <= n`

## Examples
### Example 1
- **Input:** `nums = [2,1,3,4], locked = [0,1,0,1], k = 1`
- **Output:** `2`
- **Explanation:** Unlock index 1. The array `locked` becomes `[0,0,0,1]`. 
 Swap `nums[0]` and `nums[1]`. The array `nums` becomes `[1,2,3,4]`. 
 

 The total number of operations is `1 + 1 = 2`.

### Example 2
- **Input:** `nums = [3,1,2], locked = [1,0,1], k = 2`
- **Output:** `4`
- **Explanation:** Unlock indices 0 and 2. All indices are now unlocked. 
 Swap indices 0 and 1. The array `nums` becomes `[1,3,2]`. 
 Swap indices 1 and 2. The array `nums` becomes `[1,2,3]`. 
 

 The total number of operations is `2 + 2 = 4`.

### Example 3
- **Input:** `nums = [2,3,1], locked = [1,0,0], k = 0`
- **Output:** `-1`
- **Explanation:** Index 0 is locked, so its value cannot be moved. Since `k = 0`, no indices can be unlocked. Therefore, sorting the array is impossible.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Minimum Operations to Sort With Locked Indices**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3,4], locked = [0,1,0,1], k = 1`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Unlock index 1. The array `locked` becomes `[0,0,0,1]`. 
 Swap `nums[0]` and `nums[1]`. The array `nums` becomes `[1,2,3,4]`. 
 

 The total number of operations is `1 + 1 = 2`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minOperations = function(nums, locked, k) {
    const n = nums.length;

    let size = 1;
    while (size < n + 1) size *= 2;

    const INF = Infinity;
    const seg = new Array(2 * size).fill(INF);

    function update(value, index) {
        let p = value + size;
        seg[p] = index;

        while (p > 1) {
            p >>= 1;
            seg[p] = Math.min(seg[p * 2], seg[p * 2 + 1]);
        }
    }

    function query(left) {
        let l = left + size;
        let r = n + 1 + size;
        let result = INF;

        while (l < r) {
            if (l & 1) {
                result = Math.min(result, seg[l]);
                l++;
            }

            if (r & 1) {
                r--;
                result = Math.min(result, seg[r]);
            }

            l >>= 1;
            r >>= 1;
        }

        return result;
    }

    const diff = new Array(n + 1).fill(0);

    const bit = new Array(n + 1).fill(0);

    function bitQuery(index) {
        let sum = 0;

        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }

        return sum;
    }

    function bitUpdate(index) {
        while (index <= n) {
            bit[index]++;
            index += index & -index;
        }
    }

    let inversions = 0;

    for (let i = 0; i < n; i++) {
        const x = nums[i];

        const p = query(x + 1);

        if (p !== INF) {
            diff[p]++;
            diff[i + 1]--;
        }

        inversions += i - bitQuery(x);
        bitUpdate(x);

        update(x, i);
    }

    let active = 0;
    let unlocks = 0;

    for (let i = 0; i < n; i++) {
        active += diff[i];

        if (active > 0 && locked[i] === 1) {
            unlocks++;
        }
    }

    if (unlocks > k) {
        return -1;
    }

    return inversions + unlocks;
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../../2001-2500/2471-minimum-number-of-operations-to-sort-a-binary-tree-by-level/)
- [3863. Minimum Operations to Sort a String](../../3501-4000/3863-minimum-operations-to-sort-a-string/)
- [3942. Minimum Operations to Sort a Permutation](../../3501-4000/3942-minimum-operations-to-sort-a-permutation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-with-locked-indices/)
