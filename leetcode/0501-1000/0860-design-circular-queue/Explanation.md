# LeetCode 622: Design Circular Queue

**LeetCode Problem #622 — Design Circular Queue**
Solve LeetCode Design Circular Queue using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Circular Queue |
| LeetCode | #622 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the `MyCircularQueue` class:

`MyCircularQueue(k)` Initializes the object with the size of the queue to be `k`. 
 `int Front()` Gets the front item from the queue. If the queue is empty, return `-1`. 
 `int Rear()` Gets the last item from the queue. If the queue is empty, return `-1`. 
 `boolean enQueue(int value)` Inserts an element into the circular queue. Return `true` if the operation is successful. 
 `boolean deQueue()` Deletes an element from the circular queue. Return `true` if the operation is successful. 
 `boolean isEmpty()` Checks whether the circular queue is empty or not. 
 `boolean isFull()` Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language.

## Constraints
- `1 <= k <= 1000`
- `0 <= value <= 1000`
- At most `3000` calls will be made to `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull`.

## Examples
### Example 1
- **Input:** `["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]`
- **Output:** `[null, true, true, true, false, 3, true, true, true, 4]`
- **Explanation:** MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear(); // return 3
myCircularQueue.isFull(); // return True
myCircularQueue.deQueue(); // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear(); // return 4

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Design Circular Queue**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, true, true, true, false, 3, true, true, true, 4]`.
4. **Verification:** MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear(); // return 3
myCircularQueue.isFull(); // return True
myCircularQueue.deQueue(); // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear(); // return 4

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
/**
 * @param {number} k
 */
var MyCircularQueue = function (k) {
    this.data = new Array(k);
    this.cap = k;
    this.head = 0;
    this.size = 0;
};

/**
 * @param {number} value
 * @return {boolean}
 */
MyCircularQueue.prototype.enQueue = function (value) {
    if (this.isFull()) return false;
    this.data[(this.head + this.size) % this.cap] = value;
    this.size++;
    return true;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.deQueue = function () {
    if (this.isEmpty()) return false;
    this.head = (this.head + 1) % this.cap;
    this.size--;
    return true;
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Front = function () {
    return this.isEmpty() ? -1 : this.data[this.head];
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Rear = function () {
    return this.isEmpty() ? -1 : this.data[(this.head + this.size - 1) % this.cap];
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isEmpty = function () {
    return this.size === 0;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isFull = function () {
    return this.size === this.cap;
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
- [1670. Design Front Middle Back Queue](../../1501-2000/1767-design-front-middle-back-queue/)
- [641. Design Circular Deque](../../0501-1000/0859-design-circular-deque/)
- [232. Implement Queue using Stacks](../../0001-0500/0232-implement-queue-using-stacks/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-circular-queue/)
