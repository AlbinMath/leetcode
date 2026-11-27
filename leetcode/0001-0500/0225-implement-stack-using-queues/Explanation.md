# LeetCode 225: Implement Stack using Queues

**LeetCode Problem #225 — Implement Stack using Queues**
Solve LeetCode Implement Stack using Queues using PHP and Trie. This solution finds the optimal result using Prefix Tree Lookup in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Implement Stack using Queues |
| LeetCode | #225 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Prefix Tree Lookup |
| Data Structure | Trie Node |
| Pattern | Trie |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:

`void push(int x)` Pushes element x to the top of the stack. 
 `int pop()` Removes the element on the top of the stack and returns it. 
 `int top()` Returns the element on the top of the stack. 
 `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

Notes:

You must use **only** standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid. 
 Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

## Constraints
- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.
- All the calls to `pop` and `top` are valid.

## Examples
### Example 1
- **Input:** `["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]`
- **Output:** `[null, null, null, 2, 2, false]`
- **Explanation:** MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

## Key Insight
Leverage **Trie** with **Trie Node** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Implement Stack using Queues**, we observe the problem requirements and utilize the **Trie** technique. We iterate through the inputs using **Prefix Tree Lookup**, leveraging a **Trie Node** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Trie Node**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]`.
2. **Processing Steps:** We apply **Prefix Tree Lookup** using our **Trie Node**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, 2, 2, false]`.
4. **Verification:** MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

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
PHP

## Source Code
- [solution.php](./solution.php)


```php
class MyStack {

    private $queue1;
    private $queue2;

    function __construct() {
        $this->queue1 = [];
        $this->queue2 = [];
    }

    function push($x) {
        // Add new element to the temporary queue
        $this->queue2[] = $x;

        // Move all existing elements behind it
        while (!empty($this->queue1)) {
            $this->queue2[] = array_shift($this->queue1);
        }

        // Swap the queues
        $temp = $this->queue1;
        $this->queue1 = $this->queue2;
        $this->queue2 = $temp;
    }

    function pop() {
        return array_shift($this->queue1);
    }

    function top() {
        return $this->queue1[0];
    }

    function empty() {
        return empty($this->queue1);
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
- [232. Implement Queue using Stacks](../../0001-0500/0232-implement-queue-using-stacks/)
- [470. Implement Rand10() Using Rand7()](../../0001-0500/0470-implement-rand10-using-rand7/)
- [155. Min Stack](../../0001-0500/0155-min-stack/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/implement-stack-using-queues/)
