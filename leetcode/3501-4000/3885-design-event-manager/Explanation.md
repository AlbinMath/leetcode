# LeetCode 3885: Design Event Manager

**LeetCode Problem #3885 — Design Event Manager**
Solve LeetCode Design Event Manager using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Event Manager |
| LeetCode | #3885 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an initial list of events, where each event has a unique `eventId` and a `priority`.

Implement the `EventManager` class:

`EventManager(int[][] events)` Initializes the manager with the given events, where `events[i] = [eventId_i, priority_​​​​​​​i]`. 
 `void updatePriority(int eventId, int newPriority)` Updates the priority of the **active** event with id `eventId` to `newPriority`. 
 `int pollHighest()` Removes and returns the `eventId` of the **active** event with the **highest** priority. If multiple active events have the same priority, return the **smallest** `eventId` among them. If there are no active events, return -1.

An event is called **active** if it has not been removed by `pollHighest()`.

## Constraints
- `1 <= events.length <= 10^5`
- `events[i] = [eventId, priority]`
- `1 <= eventId <= 10^9`
- `1 <= priority <= 10^9`
- All the values of `eventId` in `events` are **unique**.
- `1 <= newPriority <= 10^9`
- For every call to `updatePriority`, `eventId` refers to an **active** event.
- At most `10^5` calls in **total** will be made to `updatePriority` and `pollHighest`.

## Examples
### Example 1
- **Input:** `["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"] 
[[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]`
- **Output:** `[null, 2, null, 5, 9]`
- **Explanation:** EventManager eventManager = new EventManager([[5,7], [2,7], [9,4]]); // Initializes the manager with three events 
eventManager.pollHighest(); // both events 5 and 2 have priority 7, so return the smaller id 2 
eventManager.updatePriority(9, 7); // event 9 now has priority 7 
eventManager.pollHighest(); // remaining highest priority events are 5 and 9, return 5 
eventManager.pollHighest(); // return 9

### Example 2
- **Input:** `["EventManager", "pollHighest", "pollHighest", "pollHighest"] 
[[[[4, 1], [7, 2]]], [], [], []]`
- **Output:** `[null, 7, 4, -1]`
- **Explanation:** EventManager eventManager = new EventManager([[4,1], [7,2]]); // Initializes the manager with two events 
eventManager.pollHighest(); // return 7 
eventManager.pollHighest(); // return 4 
eventManager.pollHighest(); // no events remain, return -1

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Design Event Manager**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"] 
[[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 2, null, 5, 9]`.
4. **Verification:** EventManager eventManager = new EventManager([[5,7], [2,7], [9,4]]); // Initializes the manager with three events 
eventManager.pollHighest(); // both events 5 and 2 have priority 7, so return the smaller id 2 
eventManager.updatePriority(9, 7); // event 9 now has priority 7 
eventManager.pollHighest(); // remaining highest priority events are 5 and 9, return 5 
eventManager.pollHighest(); // return 9

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
class EventHeap {
    constructor() {
        this.data = [];
    }
    size() {
        return this.data.length;
    }
    _higherPriority(a, b) {
        if (a[0] !== b[0]) return a[0] > b[0];
        return a[1] < b[1];
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
var EventManager = function(events) {
    this.activePriority = new Map();
    this.heap = new EventHeap();
    
    for (const [eventId, priority] of events) {
        this.activePriority.set(eventId, priority);
        this.heap.push([priority, eventId]);
    }
};
EventManager.prototype.updatePriority = function(eventId, newPriority) {
    this.activePriority.set(eventId, newPriority);
    this.heap.push([newPriority, eventId]);
};
EventManager.prototype.pollHighest = function() {
    while (this.heap.size() > 0) {
        const [priority, eventId] = this.heap.pop();
        if (this.activePriority.get(eventId) === priority) {
            this.activePriority.delete(eventId);
            return eventId;
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
- [1797. Design Authentication Manager](../../1501-2000/1797-design-authentication-manager/)
- [3408. Design Task Manager](../../3001-3500/3408-design-task-manager/)
- [675. Cut Off Trees for Golf Event](../../0501-1000/0675-cut-off-trees-for-golf-event/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-event-manager/)
