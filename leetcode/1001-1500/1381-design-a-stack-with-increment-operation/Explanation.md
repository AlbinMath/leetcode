# LeetCode 1381: Design a Stack With Increment Operation

**LeetCode Problem #1381 — Design a Stack With Increment Operation**
Solve LeetCode Design a Stack With Increment Operation using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design a Stack With Increment Operation |
| LeetCode | #1381 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Design a stack that supports increment operations on its elements.

Implement the `CustomStack` class:

`CustomStack(int maxSize)` Initializes the object with `maxSize` which is the maximum number of elements in the stack. 
 `void push(int x)` Adds `x` to the top of the stack if the stack has not reached the `maxSize`. 
 `int pop()` Pops and returns the top of the stack or `-1` if the stack is empty. 
 `void inc(int k, int val)` Increments the bottom `k` elements of the stack by `val`. If there are less than `k` elements in the stack, increment all the elements in the stack.

## Constraints
- `1 <= maxSize, x, k <= 1000`
- `0 <= val <= 100`
- At most `1000` calls will be made to each method of `increment`, `push` and `pop` each separately.

## Examples
### Example 1
- **Input:** `["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]`
- **Output:** `[null,null,null,2,null,null,null,null,null,103,202,201,-1]`
- **Explanation:** CustomStack stk = new CustomStack(3); // Stack is Empty []
stk.push(1); // stack becomes [1]
stk.push(2); // stack becomes [1, 2]
stk.pop(); // return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2); // stack becomes [1, 2]
stk.push(3); // stack becomes [1, 2, 3]
stk.push(4); // stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100); // stack becomes [101, 102, 103]
stk.increment(2, 100); // stack becomes [201, 202, 103]
stk.pop(); // return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop(); // return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop(); // return 201 --> Return top of the stack 201, stack becomes []
stk.pop(); // return -1 --> Stack is empty return -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Design a Stack With Increment Operation**, we observe the problem requirements and utilize the **Stack & Queue** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null,null,null,2,null,null,null,null,null,103,202,201,-1]`.
4. **Verification:** CustomStack stk = new CustomStack(3); // Stack is Empty []
stk.push(1); // stack becomes [1]
stk.push(2); // stack becomes [1, 2]
stk.pop(); // return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2); // stack becomes [1, 2]
stk.push(3); // stack becomes [1, 2, 3]
stk.push(4); // stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100); // stack becomes [101, 102, 103]
stk.increment(2, 100); // stack becomes [201, 202, 103]
stk.pop(); // return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop(); // return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop(); // return 201 --> Return top of the stack 201, stack becomes []
stk.pop(); // return -1 --> Stack is empty return -1.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stk = []
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stk) < self.maxSize:
            self.stk.append(x)

    def pop(self) -> int:
        if not self.stk:
            return -1
        i = len(self.stk) - 1
        res = self.stk.pop() + self.inc[i]
        if i > 0:
            self.inc[i - 1] += self.inc[i]
        self.inc[i] = 0
        return res

    def increment(self, k: int, val: int) -> None:
        idx = min(k, len(self.stk)) - 1
        if idx >= 0:
            self.inc[idx] += val
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
- [945. Minimum Increment to Make Array Unique](../../0501-1000/0945-minimum-increment-to-make-array-unique/)
- [3806. Maximum Bitwise AND After Increment Operations](../../3501-4000/3806-maximum-bitwise-and-after-increment-operations/)
- [3943. Number of Pairs After Increment](../../3501-4000/3943-number-of-pairs-after-increment/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-a-stack-with-increment-operation/)
