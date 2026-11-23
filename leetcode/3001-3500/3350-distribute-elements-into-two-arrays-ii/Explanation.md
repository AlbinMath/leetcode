# LeetCode 3072: Distribute Elements Into Two Arrays II

**LeetCode Problem #3072 — Distribute Elements Into Two Arrays II**
Solve LeetCode Distribute Elements Into Two Arrays II using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distribute Elements Into Two Arrays II |
| LeetCode | #3072 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **1-indexed** array of integers `nums` of length `n`.

We define a function `greaterCount` such that `greaterCount(arr, val)` returns the number of elements in `arr` that are **strictly greater** than `val`.

You need to distribute all the elements of `nums` between two arrays `arr1` and `arr2` using `n` operations. In the first operation, append `nums[1]` to `arr1`. In the second operation, append `nums[2]` to `arr2`. Afterwards, in the `i^th` operation:

If `greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i])`, append `nums[i]` to `arr1`. 
 If `greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i])`, append `nums[i]` to `arr2`. 
 If `greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i])`, append `nums[i]` to the array with a **lesser** number of elements. 
 If there is still a tie, append `nums[i]` to `arr1`.

The array `result` is formed by concatenating the arrays `arr1` and `arr2`. For example, if `arr1 == [1,2,3]` and `arr2 == [4,5,6]`, then `result = [1,2,3,4,5,6]`.

Return *the integer array* `result`.

## Constraints
- `3 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,1,3,3]`
- **Output:** `[2,3,1,3]`
- **Explanation:** After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3^rd operation, the number of elements greater than 3 is zero in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
In the 4^th operation, the number of elements greater than 3 is zero in both arrays. As the length of arr2 is lesser, hence, append nums[4] to arr2.
After 4 operations, arr1 = [2,3] and arr2 = [1,3].
Hence, the array result formed by concatenation is [2,3,1,3].

### Example 2
- **Input:** `nums = [5,14,3,1,2]`
- **Output:** `[5,3,1,2,14]`
- **Explanation:** After the first 2 operations, arr1 = [5] and arr2 = [14].
In the 3^rd operation, the number of elements greater than 3 is one in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
In the 4^th operation, the number of elements greater than 1 is greater in arr1 than arr2 (2 > 1). Hence, append nums[4] to arr1.
In the 5^th operation, the number of elements greater than 2 is greater in arr1 than arr2 (2 > 1). Hence, append nums[5] to arr1.
After 5 operations, arr1 = [5,3,1,2] and arr2 = [14].
Hence, the array result formed by concatenation is [5,3,1,2,14].

### Example 3
- **Input:** `nums = [3,3,3,3]`
- **Output:** `[3,3,3,3]`
- **Explanation:** At the end of 4 operations, arr1 = [3,3] and arr2 = [3,3].
Hence, the array result formed by concatenation is [3,3,3,3].

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Distribute Elements Into Two Arrays II**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3,1,3]`.
4. **Verification:** After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3^rd operation, the number of elements greater than 3 is zero in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
In the 4^th operation, the number of elements greater than 3 is zero in both arrays. As the length of arr2 is lesser, hence, append nums[4] to arr2.
After 4 operations, arr1 = [2,3] and arr2 = [1,3].
Hence, the array result formed by concatenation is [2,3,1,3].

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
var resultArray = function(nums) {
    const sorted = [...new Set(nums)].sort((a, b) => a - b);
    const rank = new Map();

    for (let i = 0; i < sorted.length; i++) {
        rank.set(sorted[i], i + 1);
    }

    const m = sorted.length;

    function createBIT() {
        const bit = new Array(m + 1).fill(0);

        return {
            query(i) {
                let count = 0;

                while (i > 0) {
                    count += bit[i];
                    i -= i & -i;
                }

                return count;
            },

            update(i) {
                while (i <= m) {
                    bit[i]++;
                    i += i & -i;
                }
            }
        };
    }

    const bit1 = createBIT();
    const bit2 = createBIT();

    const arr1 = [nums[0]];
    const arr2 = [nums[1]];

    bit1.update(rank.get(nums[0]));
    bit2.update(rank.get(nums[1]));

    for (let i = 2; i < nums.length; i++) {
        const r = rank.get(nums[i]);

        const greater1 = arr1.length - bit1.query(r);
        const greater2 = arr2.length - bit2.query(r);

        if (
            greater1 > greater2 ||
            (greater1 === greater2 && arr1.length <= arr2.length)
        ) {
            arr1.push(nums[i]);
            bit1.update(r);
        } else {
            arr2.push(nums[i]);
            bit2.update(r);
        }
    }

    return arr1.concat(arr2);
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
- [3069. Distribute Elements Into Two Arrays I](../../3001-3500/3347-distribute-elements-into-two-arrays-i/)
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2162-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [1305. All Elements in Two Binary Search Trees](../../1001-1500/1427-all-elements-in-two-binary-search-trees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/)
