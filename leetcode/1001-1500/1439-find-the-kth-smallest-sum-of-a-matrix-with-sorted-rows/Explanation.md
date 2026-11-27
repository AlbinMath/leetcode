# LeetCode 1439: Find the Kth Smallest Sum of a Matrix With Sorted Rows

**LeetCode Problem #1439 — Find the Kth Smallest Sum of a Matrix With Sorted Rows**
Solve LeetCode Find the Kth Smallest Sum of a Matrix With Sorted Rows using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Kth Smallest Sum of a Matrix With Sorted Rows |
| LeetCode | #1439 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` matrix `mat` that has its rows sorted in non-decreasing order and an integer `k`.

You are allowed to choose **exactly one element** from each row to form an array.

Return *the *`k^th`* smallest array sum among all possible arrays*.

## Constraints
- `m == mat.length`
- `n == mat.length[i]`
- `1 <= m, n <= 40`
- `1 <= mat[i][j] <= 5000`
- `1 <= k <= min(200, n^m)`
- `mat[i]` is a non-decreasing array.

## Examples
### Example 1
- **Input:** `mat = [[1,3,11],[2,4,6]], k = 5`
- **Output:** `7`
- **Explanation:** Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.

### Example 2
- **Input:** `mat = [[1,3,11],[2,4,6]], k = 9`
- **Output:** `17`

### Example 3
- **Input:** `mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7`
- **Output:** `9`
- **Explanation:** Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Kth Smallest Sum of a Matrix With Sorted Rows**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,3,11],[2,4,6]], k = 5`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
class PairMinHeap {
    constructor() {
        this.data = [];
    }
    size() {
        return this.data.length;
    }
    push(val) {
        this.data.push(val);
        let i = this.data.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.data[p][0] <= this.data[i][0]) break;
            [this.data[p], this.data[i]] = [this.data[i], this.data[p]];
            i = p;
        }
    }
    pop() {
        const top = this.data[0];
        const last = this.data.pop();
        if (this.data.length > 0) {
            this.data[0] = last;
            let i = 0;
            const n = this.data.length;
            while (true) {
                let smallest = i;
                const l = (i << 1) + 1;
                const r = (i << 1) + 2;
                if (l < n && this.data[l][0] < this.data[smallest][0]) smallest = l;
                if (r < n && this.data[r][0] < this.data[smallest][0]) smallest = r;
                if (smallest === i) break;
                [this.data[i], this.data[smallest]] = [this.data[smallest], this.data[i]];
                i = smallest;
            }
        }
        return top;
    }
}


var kthSmallest = function(mat, k) {
    const kSmallestPairSums = (nums1, nums2) => {
        const heap = new PairMinHeap();
        for (let i = 0; i < nums1.length; i++) {
            heap.push([nums1[i] + nums2[0], i, 0]);
        }

        const merged = [];
        while (heap.size() > 0 && merged.length < k) {
            const [currSum, i, j] = heap.pop();
            merged.push(currSum);
            if (j + 1 < nums2.length) {
                heap.push([nums1[i] + nums2[j + 1], i, j + 1]);
            }
        }
        return merged;
    };

    let currSums = mat[0].slice(0, k);
    for (let r = 1; r < mat.length; r++) {
        currSums = kSmallestPairSums(currSums, mat[r]);
    }

    return currSums[k - 1];
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [378. Kth Smallest Element in a Sorted Matrix](../../0001-0500/0378-kth-smallest-element-in-a-sorted-matrix/)
- [2040. Kth Smallest Product of Two Sorted Arrays](../../2001-2500/2040-kth-smallest-product-of-two-sorted-arrays/)
- [167. Two Sum II - Input Array Is Sorted](../../0001-0500/0167-two-sum-ii-input-array-is-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)
