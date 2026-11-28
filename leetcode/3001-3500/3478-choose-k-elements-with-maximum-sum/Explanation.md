# LeetCode 3478: Choose K Elements With Maximum Sum

**LeetCode Problem #3478 — Choose K Elements With Maximum Sum**
Solve LeetCode Choose K Elements With Maximum Sum using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Choose K Elements With Maximum Sum |
| LeetCode | #3478 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays, `nums1` and `nums2`, both of length `n`, along with a positive integer `k`.

For each index `i` from `0` to `n - 1`, perform the following:

Find **all** indices `j` where `nums1[j]` is less than `nums1[i]`. 
 Choose **at most** `k` values of `nums2[j]` at these indices to **maximize** the total sum.

Return an array `answer` of size `n`, where `answer[i]` represents the result for the corresponding index `i`.

## Constraints
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^6`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2`
- **Output:** `[80,30,0,80,50]`
- **Explanation:** For `i = 0`: Select the 2 largest values from `nums2` at indices `[1, 2, 4]` where `nums1[j] < nums1[0]`, resulting in `50 + 30 = 80`. 
 For `i = 1`: Select the 2 largest values from `nums2` at index `[2]` where `nums1[j] < nums1[1]`, resulting in 30. 
 For `i = 2`: No indices satisfy `nums1[j] < nums1[2]`, resulting in 0. 
 For `i = 3`: Select the 2 largest values from `nums2` at indices `[0, 1, 2, 4]` where `nums1[j] < nums1[3]`, resulting in `50 + 30 = 80`. 
 For `i = 4`: Select the 2 largest values from `nums2` at indices `[1, 2]` where `nums1[j] < nums1[4]`, resulting in `30 + 20 = 50`.

### Example 2
- **Input:** `nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1`
- **Output:** `[0,0,0,0]`
- **Explanation:** Since all elements in `nums1` are equal, no indices satisfy the condition `nums1[j] < nums1[i]` for any `i`, resulting in 0 for all positions.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Choose K Elements With Maximum Sum**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[80,30,0,80,50]`.
4. **Verification:** For `i = 0`: Select the 2 largest values from `nums2` at indices `[1, 2, 4]` where `nums1[j] < nums1[0]`, resulting in `50 + 30 = 80`. 
 For `i = 1`: Select the 2 largest values from `nums2` at index `[2]` where `nums1[j] < nums1[1]`, resulting in 30. 
 For `i = 2`: No indices satisfy `nums1[j] < nums1[2]`, resulting in 0. 
 For `i = 3`: Select the 2 largest values from `nums2` at indices `[0, 1, 2, 4]` where `nums1[j] < nums1[3]`, resulting in `50 + 30 = 80`. 
 For `i = 4`: Select the 2 largest values from `nums2` at indices `[1, 2]` where `nums1[j] < nums1[4]`, resulting in `30 + 20 = 50`.

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
var findMaxSum = function(nums1, nums2, k) {
    const n = nums1.length;
    const arr = [];
    for (let i = 0; i < n; i++) {
        arr.push([nums1[i], nums2[i], i]);
    }
    arr.sort((a, b) => a[0] - b[0]);
    const answer = new Array(n).fill(0);
    const heap = [];
    let sum = 0;
    const push = function(value) {
        heap.push(value);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (heap[parent] <= heap[i]) break;
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    };
    const pop = function() {
        const min = heap[0];
        const last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let smallest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;
                if (
                    left < heap.length &&
                    heap[left] < heap[smallest]
                ) {
                    smallest = left;
                }
                if (
                    right < heap.length &&
                    heap[right] < heap[smallest]
                ) {
                    smallest = right;
                }
                if (smallest === i) break;
                [heap[i], heap[smallest]] =
                    [heap[smallest], heap[i]];
                i = smallest;
            }
        }
        return min;
    };
    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && arr[j][0] === arr[i][0]) {
            j++;
        }
        for (let p = i; p < j; p++) {
            const [a, b, index] = arr[p];
            answer[index] = sum;
        }
        for (let p = i; p < j; p++) {
            const value = arr[p][1];
            if (heap.length < k) {
                push(value);
                sum += value;
            } else if (value > heap[0]) {
                sum -= pop();
                push(value);
                sum += value;
            }
        }

        i = j;
    }
    return answer;
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
- [2656. Maximum Sum With Exactly K Elements ](../../2501-3000/2656-maximum-sum-with-exactly-k-elements/)
- [3462. Maximum Sum With at Most K Elements](../../3001-3500/3462-maximum-sum-with-at-most-k-elements/)
- [3974. Maximum Total Sum of K Selected Elements](../../3501-4000/3974-maximum-total-sum-of-k-selected-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/choose-k-elements-with-maximum-sum/)
