# LeetCode 307: Range Sum Query - Mutable

**LeetCode Problem #307 — Range Sum Query - Mutable**
Solve LeetCode Range Sum Query - Mutable using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Range Sum Query - Mutable |
| LeetCode | #307 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, handle multiple queries of the following types:

**Update** the value of an element in `nums`. 
 Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

`NumArray(int[] nums)` Initializes the object with the integer array `nums`. 
 `void update(int index, int val)` **Updates** the value of `nums[index]` to be `val`. 
 `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `0 <= index < nums.length`
- `-100 <= val <= 100`
- `0 <= left <= right < nums.length`
- At most `3 * 10^4` calls will be made to `update` and `sumRange`.

## Examples
### Example 1
- **Input:** `["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]`
- **Output:** `[null, 9, null, 8]`
- **Explanation:** NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2); // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Range Sum Query - Mutable**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 9, null, 8]`.
4. **Verification:** NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2); // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var NumArray = function(nums) {
    this.n = nums.length;
    this.tree = new Array(2 * this.n).fill(0);

    // Build the segment tree
    for (let i = 0; i < this.n; i++) {
        this.tree[this.n + i] = nums[i];
    }

    for (let i = this.n - 1; i > 0; i--) {
        this.tree[i] = this.tree[2 * i] + this.tree[2 * i + 1];
    }
};

NumArray.prototype.update = function(index, val) {
    let pos = index + this.n;

    // Update the leaf node
    this.tree[pos] = val;

    // Update all parent nodes
    while (pos > 1) {
        pos = Math.floor(pos / 2);
        this.tree[pos] = this.tree[2 * pos] + this.tree[2 * pos + 1];
    }
};

NumArray.prototype.sumRange = function(left, right) {
    let sum = 0;

    left += this.n;
    right += this.n;

    // Query the inclusive range [left, right]
    while (left <= right) {
        if (left % 2 === 1) {
            sum += this.tree[left];
            left++;
        }

        if (right % 2 === 0) {
            sum += this.tree[right];
            right--;
        }

        left = Math.floor(left / 2);
        right = Math.floor(right / 2);
    }

    return sum;
};
```

### Python
```python
class NumArray:
    def __init__(self, nums: List[int]):
        self.a = nums[:]
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        for i, x in enumerate(nums):
            self.add(i + 1, x)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.a[index])
        self.a[index] = val

    def sumRange(self, left: int, right: int) -> int:
        def query(i):
            s = 0
            while i:
                s += self.bit[i]
                i -= i & -i
            return s
        return query(right + 1) - query(left)
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
- [303. Range Sum Query - Immutable](../../0001-0500/0303-range-sum-query-immutable/)
- [304. Range Sum Query 2D - Immutable](../../0001-0500/0304-range-sum-query-2d-immutable/)
- [327. Count of Range Sum](../../0001-0500/0327-count-of-range-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/range-sum-query-mutable/)
