# LeetCode 3408: Design Task Manager

**LeetCode Problem #3408 — Design Task Manager**
Solve LeetCode Design Task Manager using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Task Manager |
| LeetCode | #3408 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

Implement the `TaskManager` class:

`TaskManager(vector<vector<int>>& tasks)` initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form `[userId, taskId, priority]`, which adds a task to the specified user with the given priority.

`void add(int userId, int taskId, int priority)` adds a task with the specified `taskId` and `priority` to the user with `userId`. It is **guaranteed** that `taskId` does not *exist* in the system.

`void edit(int taskId, int newPriority)` updates the priority of the existing `taskId` to `newPriority`. It is **guaranteed** that `taskId` *exists* in the system.

`void rmv(int taskId)` removes the task identified by `taskId` from the system. It is **guaranteed** that `taskId` *exists* in the system.

`int execTop()` executes the task with the **highest** priority across all users. If there are multiple tasks with the same **highest** priority, execute the one with the highest `taskId`. After executing, the** **`taskId`** **is **removed** from the system. Return the `userId` associated with the executed task. If no tasks are available, return -1.

**Note** that a user may be assigned multiple tasks.

## Constraints
- `1 <= tasks.length <= 10^5`
- `0 <= userId <= 10^5`
- `0 <= taskId <= 10^5`
- `0 <= priority <= 10^9`
- `0 <= newPriority <= 10^9`
- At most `2 * 10^5` calls will be made in **total** to `add`, `edit`, `rmv`, and `execTop` methods.
- The input is generated such that `taskId` will be valid.

## Examples
### Example 1
- **Input:** `["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"] 
[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]`
- **Output:** `[null, null, null, 3, null, null, 5]`
- **Explanation:** TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3. 
taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4. 
taskManager.edit(102, 8); // Updates priority of task 102 to 8. 
taskManager.execTop(); // return 3. Executes task 103 for User 3. 
taskManager.rmv(101); // Removes task 101 from the system. 
taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5. 
taskManager.execTop(); // return 5. Executes task 105 for User 5.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Design Task Manager**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"] 
[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, 3, null, null, 5]`.
4. **Verification:** TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3. 
taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4. 
taskManager.edit(102, 8); // Updates priority of task 102 to 8. 
taskManager.execTop(); // return 3. Executes task 103 for User 3. 
taskManager.rmv(101); // Removes task 101 from the system. 
taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5. 
taskManager.execTop(); // return 5. Executes task 105 for User 5.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
class TaskMaxHeap {
    constructor() {
        this.data = [];
    }
    size() {
        return this.data.length;
    }
    _higherPriority(a, b) {
        if (a[0] !== b[0]) return a[0] > b[0];
        return a[1] > b[1];
    }
    push(val) {
        this.data.push(val);
        let i = this.data.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this._higherPriority(this.data[p], this.data[i])) break;
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
                let best = i;
                const l = (i << 1) + 1;
                const r = (i << 1) + 2;
                if (l < n && this._higherPriority(this.data[l], this.data[best])) best = l;
                if (r < n && this._higherPriority(this.data[r], this.data[best])) best = r;
                if (best === i) break;
                [this.data[i], this.data[best]] = [this.data[best], this.data[i]];
                i = best;
            }
        }
        return top;
    }
}
var TaskManager = function(tasks) {
    this.taskInfo = new Map();
    this.heap = new TaskMaxHeap();
    
    for (const [userId, taskId, priority] of tasks) {
        this.taskInfo.set(taskId, [userId, priority]);
        this.heap.push([priority, taskId, userId]);
    }
};
TaskManager.prototype.add = function(userId, taskId, priority) {
    this.taskInfo.set(taskId, [userId, priority]);
    this.heap.push([priority, taskId, userId]);
};
TaskManager.prototype.edit = function(taskId, newPriority) {
    const [userId] = this.taskInfo.get(taskId);
    this.taskInfo.set(taskId, [userId, newPriority]);
    this.heap.push([newPriority, taskId, userId]);
};
TaskManager.prototype.rmv = function(taskId) {
    this.taskInfo.delete(taskId);
};
TaskManager.prototype.execTop = function() {
    while (this.heap.size() > 0) {
        const [priority, taskId, userId] = this.heap.pop();
        const current = this.taskInfo.get(taskId);
        if (current && current[0] === userId && current[1] === priority) {
            this.taskInfo.delete(taskId);
            return userId;
        }
    }
    return -1;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1797. Design Authentication Manager](../../1501-2000/1905-design-authentication-manager/)
- [3885. Design Event Manager](../../4001-4500/4267-design-event-manager/)
- [1845. Seat Reservation Manager](../../1501-2000/1955-seat-reservation-manager/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-task-manager/)
