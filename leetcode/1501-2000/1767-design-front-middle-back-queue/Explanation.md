# LeetCode 1670: Design Front Middle Back Queue

**LeetCode Problem #1670 — Design Front Middle Back Queue**
Solve LeetCode Design Front Middle Back Queue using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Front Middle Back Queue |
| LeetCode | #1670 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Design a queue that supports `push` and `pop` operations in the front, middle, and back.

Implement the `FrontMiddleBack` class:

`FrontMiddleBack()` Initializes the queue. 
 `void pushFront(int val)` Adds `val` to the **front** of the queue. 
 `void pushMiddle(int val)` Adds `val` to the **middle** of the queue. 
 `void pushBack(int val)` Adds `val` to the **back** of the queue. 
 `int popFront()` Removes the **front** element of the queue and returns it. If the queue is empty, return `-1`. 
 `int popMiddle()` Removes the **middle** element of the queue and returns it. If the queue is empty, return `-1`. 
 `int popBack()` Removes the **back** element of the queue and returns it. If the queue is empty, return `-1`.

**Notice** that when there are two middle position choices, the operation is performed on the **frontmost** middle position choice. For example:

Pushing `6` into the middle of `[1, 2, 3, 4, 5]` results in `[1, 2, 6 , 3, 4, 5]`. 
 Popping the middle from `[1, 2, 3 , 4, 5, 6]` returns `3` and results in `[1, 2, 4, 5, 6]`.

## Constraints
- `1 <= val <= 10^9`
- At most `1000` calls will be made to `pushFront`, `pushMiddle`, `pushBack`, `popFront`, `popMiddle`, and `popBack`.

## Examples
### Example 1
- **Input:** `["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]`
- **Output:** `[null, null, null, null, null, 1, 3, 4, 2, -1]`
- **Explanation:** FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1); // [ 1 ]
q.pushBack(2); // [1, 2 ]
q.pushMiddle(3); // [1, 3 , 2]
q.pushMiddle(4); // [1, 4 , 3, 2]
q.popFront(); // return 1 -> [4, 3, 2]
q.popMiddle(); // return 3 -> [4, 2]
q.popMiddle(); // return 4 -> [2]
q.popBack(); // return 2 -> []
q.popFront(); // return -1 -> [] (The queue is empty)

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Design Front Middle Back Queue**, we observe the problem requirements and utilize the **Stack & Queue** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, null, null, 1, 3, 4, 2, -1]`.
4. **Verification:** FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1); // [ 1 ]
q.pushBack(2); // [1, 2 ]
q.pushMiddle(3); // [1, 3 , 2]
q.pushMiddle(4); // [1, 4 , 3, 2]
q.popFront(); // return 1 -> [4, 3, 2]
q.popMiddle(); // return 3 -> [4, 2]
q.popMiddle(); // return 4 -> [2]
q.popBack(); // return 2 -> []
q.popFront(); // return -1 -> [] (The queue is empty)

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
from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def _balance(self):
        # invariant: len(left) <= len(right) <= len(left) + 1
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) == len(self.right):
            self.right.appendleft(val)
        else:
            self.left.append(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.right:
            return -1
        res = self.left.popleft() if self.left else self.right.popleft()
        self._balance()
        return res

    def popMiddle(self) -> int:
        if not self.right:
            return -1
        if len(self.left) == len(self.right):
            res = self.left.pop()
        else:
            res = self.right.popleft()
        self._balance()
        return res

    def popBack(self) -> int:
        if not self.right:
            return -1
        res = self.right.pop()
        self._balance()
        return res
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
- [622. Design Circular Queue](../../0501-1000/0860-design-circular-queue/)
- [876. Middle of the Linked List](../../0501-1000/0908-middle-of-the-linked-list/)
- [1991. Find the Middle Index in Array](../../2001-2500/2102-find-the-middle-index-in-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-front-middle-back-queue/)
