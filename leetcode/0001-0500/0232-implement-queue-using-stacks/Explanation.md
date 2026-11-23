# LeetCode 232: Implement Queue using Stacks

**LeetCode Problem #232 — Implement Queue using Stacks**
Solve LeetCode Implement Queue using Stacks using JavaScript, PHP and Trie. This solution finds the optimal result using Prefix Tree Lookup in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Implement Queue using Stacks |
| LeetCode | #232 |
| Difficulty | Easy |
| Language | JavaScript, PHP |
| Algorithm | Prefix Tree Lookup |
| Data Structure | Trie Node |
| Pattern | Trie |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

`void push(int x)` Pushes element x to the back of the queue. 
 `int pop()` Removes the element from the front of the queue and returns it. 
 `int peek()` Returns the element at the front of the queue. 
 `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

**Notes:**

You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid. 
 Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

## Constraints
- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.
- All the calls to `pop` and `peek` are valid.

## Examples
### Example 1
- **Input:** `["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]`
- **Output:** `[null, null, null, 1, 1, false]`
- **Explanation:** MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

## Key Insight
Leverage **Trie** with **Trie Node** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Implement Queue using Stacks**, we observe the problem requirements and utilize the **Trie** technique. We iterate through the inputs using **Prefix Tree Lookup**, leveraging a **Trie Node** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Trie Node**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]`.
2. **Processing Steps:** We apply **Prefix Tree Lookup** using our **Trie Node**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, 1, 1, false]`.
4. **Verification:** MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Trie Node.

## Pattern
**Trie**

## Topics
- Trie
- String
- Prefix Search

## Language
JavaScript, PHP

## Source Code
- [solution.js](./solution.js)
- [solution.php](./solution.php)


### JavaScript
```javascript
var MyQueue = function() {
    this.input = [];
    this.output = [];
};

MyQueue.prototype.push = function(x) {
    this.input.push(x);
};

MyQueue.prototype.pop = function() {
    this.peek();
    return this.output.pop();
};

MyQueue.prototype.peek = function() {
    if (this.output.length === 0) {
        while (this.input.length > 0) {
            this.output.push(this.input.pop());
        }
    }

    return this.output[this.output.length - 1];
};

MyQueue.prototype.empty = function() {
    return this.input.length === 0 && this.output.length === 0;
};
```

### PHP
```php
class MyQueue {

    private $inStack = [];
    private $outStack = [];

    function __construct() {
    }

    function push($x) {
        // Always push new elements into inStack
        $this->inStack[] = $x;
    }

    function pop() {
        $this->moveToOutStack();

        return array_pop($this->outStack);
    }

    function peek() {
        $this->moveToOutStack();

        return $this->outStack[count($this->outStack) - 1];
    }

    function empty() {
        return empty($this->inStack) && empty($this->outStack);
    }

    private function moveToOutStack() {
        // Only transfer when outStack is empty
        if (empty($this->outStack)) {
            while (!empty($this->inStack)) {
                $this->outStack[] = array_pop($this->inStack);
            }
        }
    }
}
```

## Why This Works
By utilizing **Trie**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [225. Implement Stack using Queues](../../0001-0500/0225-implement-stack-using-queues/)
- [470. Implement Rand10() Using Rand7()](../../0501-1000/0903-implement-rand10-using-rand7/)
- [208. Implement Trie (Prefix Tree)](../../0001-0500/0208-implement-trie-prefix-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)
