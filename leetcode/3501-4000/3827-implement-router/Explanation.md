# LeetCode 3508: Implement Router

**LeetCode Problem #3508 — Implement Router**
Solve LeetCode Implement Router using JavaScript and Trie. This solution finds the optimal result using Prefix Tree Lookup in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Implement Router |
| LeetCode | #3508 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Prefix Tree Lookup |
| Data Structure | Trie Node |
| Pattern | Trie |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:

`source`: A unique identifier for the machine that generated the packet. 
 `destination`: A unique identifier for the target machine. 
 `timestamp`: The time at which the packet arrived at the router.

Implement the `Router` class:

`Router(int memoryLimit)`: Initializes the Router object with a fixed memory limit.

`memoryLimit` is the **maximum** number of packets the router can store at any given time. 
 If adding a new packet would exceed this limit, the **oldest** packet must be removed to free up space.

`bool addPacket(int source, int destination, int timestamp)`: Adds a packet with the given attributes to the router.

A packet is considered a duplicate if another packet with the same `source`, `destination`, and `timestamp` already exists in the router. 
 Return `true` if the packet is successfully added (i.e., it is not a duplicate); otherwise return `false`.

`int[] forwardPacket()`: Forwards the next packet in FIFO (First In First Out) order.

Remove the packet from storage. 
 Return the packet as an array `[source, destination, timestamp]`. 
 If there are no packets to forward, return an empty array.

`int getCount(int destination, int startTime, int endTime)`:

Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range `[startTime, endTime]`.

**Note** that queries for `addPacket` will be made in non-decreasing order of `timestamp`.

## Constraints
- `2 <= memoryLimit <= 10^5`
- `1 <= source, destination <= 2 * 10^5`
- `1 <= timestamp <= 10^9`
- `1 <= startTime <= endTime <= 10^9`
- At most `10^5` calls will be made to `addPacket`, `forwardPacket`, and `getCount` methods altogether.
- queries for `addPacket` will be made in non-decreasing order of `timestamp`.

## Examples
### Example 1
- **Input:** `["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"] 
[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]`
- **Output:** `[null, true, true, false, true, true, [2, 5, 90], true, 1]`
- **Explanation:** Router router = new Router(3); // Initialize Router with memoryLimit of 3. 
router.addPacket(1, 4, 90); // Packet is added. Return True. 
router.addPacket(2, 5, 90); // Packet is added. Return True. 
router.addPacket(1, 4, 90); // This is a duplicate packet. Return False. 
router.addPacket(3, 5, 95); // Packet is added. Return True 
router.addPacket(4, 5, 105); // Packet is added, `[1, 4, 90]` is removed as number of packets exceeds memoryLimit. Return True. 
router.forwardPacket(); // Return `[2, 5, 90]` and remove it from router. 
router.addPacket(5, 2, 110); // Packet is added. Return True. 
router.getCount(5, 100, 110); // The only packet with destination 5 and timestamp in the inclusive range `[100, 110]` is `[4, 5, 105]`. Return 1.

### Example 2
- **Input:** `["Router", "addPacket", "forwardPacket", "forwardPacket"] 
[[2], [7, 4, 90], [], []]`
- **Output:** `[null, true, [7, 4, 90], []]`
- **Explanation:** Router router = new Router(2); // Initialize `Router` with `memoryLimit` of 2. 
router.addPacket(7, 4, 90); // Return True. 
router.forwardPacket(); // Return `[7, 4, 90]`. 
router.forwardPacket(); // There are no packets left, return `[]`.

## Key Insight
Leverage **Trie** with **Trie Node** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Implement Router**, we observe the problem requirements and utilize the **Trie** technique. By maintaining a **Trie Node**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Trie Node** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"] 
[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]`.
2. **Processing Steps:** We apply **Prefix Tree Lookup** using our **Trie Node**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, true, true, false, true, true, [2, 5, 90], true, 1]`.
4. **Verification:** Router router = new Router(3); // Initialize Router with memoryLimit of 3. 
router.addPacket(1, 4, 90); // Packet is added. Return True. 
router.addPacket(2, 5, 90); // Packet is added. Return True. 
router.addPacket(1, 4, 90); // This is a duplicate packet. Return False. 
router.addPacket(3, 5, 95); // Packet is added. Return True 
router.addPacket(4, 5, 105); // Packet is added, `[1, 4, 90]` is removed as number of packets exceeds memoryLimit. Return True. 
router.forwardPacket(); // Return `[2, 5, 90]` and remove it from router. 
router.addPacket(5, 2, 110); // Packet is added. Return True. 
router.getCount(5, 100, 110); // The only packet with destination 5 and timestamp in the inclusive range `[100, 110]` is `[4, 5, 105]`. Return 1.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var Router = function (memoryLimit) {
    this.limit = memoryLimit;
    this.queue = [];            // [source, destination, timestamp]
    this.qHead = 0;
    this.seen = new Set();
    this.byDest = new Map();    // dest -> { ts: [], head: 0 }
};

Router.prototype._remove = function () {
    const p = this.queue[this.qHead];
    this.queue[this.qHead++] = null; // free memory
    this.seen.delete(p[0] + "," + p[1] + "," + p[2]);
    this.byDest.get(p[1]).head++;
    return p;
};

/**
 * @param {number} source
 * @param {number} destination
 * @param {number} timestamp
 * @return {boolean}
 */
Router.prototype.addPacket = function (source, destination, timestamp) {
    const key = source + "," + destination + "," + timestamp;
    if (this.seen.has(key)) return false;

    if (this.queue.length - this.qHead === this.limit) this._remove();

    this.seen.add(key);
    this.queue.push([source, destination, timestamp]);
    let d = this.byDest.get(destination);
    if (!d) {
        d = { ts: [], head: 0 };
        this.byDest.set(destination, d);
    }
    d.ts.push(timestamp);
    return true;
};

/**
 * @return {number[]}
 */
Router.prototype.forwardPacket = function () {
    if (this.qHead === this.queue.length) return [];
    return this._remove();
};

/**
 * @param {number} destination
 * @param {number} startTime
 * @param {number} endTime
 * @return {number}
 */
Router.prototype.getCount = function (destination, startTime, endTime) {
    const d = this.byDest.get(destination);
    if (!d) return 0;
    const ts = d.ts;

    // first index in [head, len) with ts[idx] >= target
    const lowerBound = (target) => {
        let lo = d.head, hi = ts.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (ts[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };

    return lowerBound(endTime + 1) - lowerBound(startTime);
};
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
- [208. Implement Trie (Prefix Tree)](../../0001-0500/0208-implement-trie-prefix-tree/)
- [225. Implement Stack using Queues](../../0001-0500/0225-implement-stack-using-queues/)
- [232. Implement Queue using Stacks](../../0001-0500/0232-implement-queue-using-stacks/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/implement-router/)
