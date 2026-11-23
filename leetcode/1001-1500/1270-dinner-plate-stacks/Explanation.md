# LeetCode 1172: Dinner Plate Stacks

**LeetCode Problem #1172 — Dinner Plate Stacks**
Solve LeetCode Dinner Plate Stacks using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Dinner Plate Stacks |
| LeetCode | #1172 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have an infinite number of stacks arranged in a row and numbered (left to right) from `0`, each of the stacks has the same maximum capacity.

Implement the `DinnerPlates` class:

`DinnerPlates(int capacity)` Initializes the object with the maximum capacity of the stacks `capacity`. 
 `void push(int val)` Pushes the given integer `val` into the leftmost stack with a size less than `capacity`. 
 `int pop()` Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns `-1` if all the stacks are empty. 
 `int popAtStack(int index)` Returns the value at the top of the stack with the given index `index` and removes it from that stack or returns `-1` if the stack with that given index is empty.

## Constraints
- `1 <= capacity <= 2 * 10^4`
- `1 <= val <= 2 * 10^4`
- `0 <= index <= 10^5`
- At most `2 * 10^5` calls will be made to `push`, `pop`, and `popAtStack`.

## Examples
### Example 1
- **Input:** `["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
[[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]`
- **Output:** `[null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]`
- **Explanation:** DinnerPlates D = DinnerPlates(2); // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5); // The stacks are now: 2 4
 1 3 5
 ﹈ ﹈ ﹈
D.popAtStack(0); // Returns 2. The stacks are now: 4
 1 3 5
 ﹈ ﹈ ﹈
D.push(20); // The stacks are now: 20 4
 1 3 5
 ﹈ ﹈ ﹈
D.push(21); // The stacks are now: 20 4 21
 1 3 5
 ﹈ ﹈ ﹈
D.popAtStack(0); // Returns 20. The stacks are now: 4 21
 1 3 5
 ﹈ ﹈ ﹈
D.popAtStack(2); // Returns 21. The stacks are now: 4
 1 3 5
 ﹈ ﹈ ﹈ 
D.pop() // Returns 5. The stacks are now: 4
 1 3 
 ﹈ ﹈ 
D.pop() // Returns 4. The stacks are now: 1 3 
 ﹈ ﹈ 
D.pop() // Returns 3. The stacks are now: 1 
 ﹈ 
D.pop() // Returns 1. There are no stacks.
D.pop() // Returns -1. There are still no stacks.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Dinner Plate Stacks**, we observe the problem requirements and utilize the **Stack & Queue** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
[[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]`.
4. **Verification:** DinnerPlates D = DinnerPlates(2); // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5); // The stacks are now: 2 4
 1 3 5
 ﹈ ﹈ ﹈
D.popAtStack(0); // Returns 2. The stacks are now: 4
 1 3 5
 ﹈ ﹈ ﹈
D.push(20); // The stacks are now: 20 4
 1 3 5
 ﹈ ﹈ ﹈
D.push(21); // The stacks are now: 20 4 21
 1 3 5
 ﹈ ﹈ ﹈
D.popAtStack(0); // Returns 20. The stacks are now: 4 21
 1 3 5
 ﹈ ﹈ ﹈
D.popAtStack(2); // Returns 21. The stacks are now: 4
 1 3 5
 ﹈ ﹈ ﹈ 
D.pop() // Returns 5. The stacks are now: 4
 1 3 
 ﹈ ﹈ 
D.pop() // Returns 4. The stacks are now: 1 3 
 ﹈ ﹈ 
D.pop() // Returns 3. The stacks are now: 1 
 ﹈ 
D.pop() // Returns 1. There are no stacks.
D.pop() // Returns -1. There are still no stacks.

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
var DinnerPlates = function(capacity) {
    this.capacity = capacity;
    this.stacks = [];
    this.heap = [];
    this.right = -1;
};

// Insert into min heap
DinnerPlates.prototype.heapPush = function(val) {
    const heap = this.heap;
    heap.push(val);

    let i = heap.length - 1;

    while (i > 0) {
        let p = Math.floor((i - 1) / 2);

        if (heap[p] <= heap[i]) break;

        [heap[p], heap[i]] = [heap[i], heap[p]];
        i = p;
    }
};

// Remove minimum from min heap
DinnerPlates.prototype.heapPop = function() {
    const heap = this.heap;
    const min = heap[0];
    const last = heap.pop();

    if (heap.length > 0) {
        heap[0] = last;
        let i = 0;

        while (true) {
            let smallest = i;
            let left = 2 * i + 1;
            let right = 2 * i + 2;

            if (left < heap.length &&
                heap[left] < heap[smallest]) {
                smallest = left;
            }

            if (right < heap.length &&
                heap[right] < heap[smallest]) {
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

// Push value
DinnerPlates.prototype.push = function(val) {
    // Create a new stack if no available stack exists
    if (this.heap.length === 0) {
        const index = this.stacks.length;

        this.stacks.push([]);
        this.heapPush(index);
    }

    // Always use the leftmost available stack
    const index = this.heap[0];

    this.stacks[index].push(val);

    this.right = Math.max(this.right, index);

    // Remove from heap if stack becomes full
    if (this.stacks[index].length === this.capacity) {
        this.heapPop();
    }
};

// Pop from rightmost non-empty stack
DinnerPlates.prototype.pop = function() {
    while (
        this.right >= 0 &&
        this.stacks[this.right].length === 0
    ) {
        this.right--;
    }

    if (this.right < 0) return -1;

    return this.popAtStack(this.right);
};

// Pop from a specific stack
DinnerPlates.prototype.popAtStack = function(index) {
    if (
        index < 0 ||
        index >= this.stacks.length ||
        this.stacks[index].length === 0
    ) {
        return -1;
    }

    const stack = this.stacks[index];
    const wasFull = stack.length === this.capacity;

    const val = stack.pop();

    // Add index only if it was previously full
    if (wasFull) {
        this.heapPush(index);
    }

    // Update rightmost non-empty stack
    while (
        this.right >= 0 &&
        this.stacks[this.right].length === 0
    ) {
        this.right--;
    }

    return val;
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
- [232. Implement Queue using Stacks](../../0001-0500/0232-implement-queue-using-stacks/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/dinner-plate-stacks/)
