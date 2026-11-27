# LeetCode 2622: Cache With Time Limit

**LeetCode Problem #2622 — Cache With Time Limit**
Solve LeetCode Cache With Time Limit using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cache With Time Limit |
| LeetCode | #2622 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Write a class that allows getting and setting key-value pairs, however a **time until expiration** is associated with each key.

The class has three public methods:

`set(key, value, duration)`: accepts an integer `key`, an integer `value`, and a `duration` in milliseconds. Once the `duration` has elapsed, the key should be inaccessible. The method should return `true` if the same un-expired key already exists and `false` otherwise. Both the value and duration should be overwritten if the key already exists.

`get(key)`: if an un-expired key exists, it should return the associated value. Otherwise it should return `-1`.

`count()`: returns the count of un-expired keys.

## Constraints
- `0 <= key, value <= 10^9`
- `0 <= duration <= 1000`
- `1 <= actions.length <= 100`
- `actions.length === values.length`
- `actions.length === timeDelays.length`
- `0 <= timeDelays[i] <= 1450`
- `actions[i]` is one of "TimeLimitedCache", "set", "get" and "count"
- First action is always "TimeLimitedCache" and must be executed immediately, with a 0-millisecond delay

## Examples
### Example 1
- **Input:** `actions = ["TimeLimitedCache", "set", "get", "count", "get"]
values = [[], [1, 42, 100], [1], [], [1]]
timeDelays = [0, 0, 50, 50, 150]`
- **Output:** `[null, false, 42, 1, -1]`
- **Explanation:** At t=0, the cache is constructed.
At t=0, a key-value pair (1: 42) is added with a time limit of 100ms. The value doesn't exist so false is returned.
At t=50, key=1 is requested and the value of 42 is returned.
At t=50, count() is called and there is one active key in the cache.
At t=100, key=1 expires.
At t=150, get(1) is called but -1 is returned because the cache is empty.

### Example 2
- **Input:** `actions = ["TimeLimitedCache", "set", "set", "get", "get", "get", "count"]
values = [[], [1, 42, 50], [1, 50, 100], [1], [1], [1], []]
timeDelays = [0, 0, 40, 50, 120, 200, 250]`
- **Output:** `[null, false, true, 50, 50, -1, 0]`
- **Explanation:** At t=0, the cache is constructed.
At t=0, a key-value pair (1: 42) is added with a time limit of 50ms. The value doesn't exist so false is returned.
At t=40, a key-value pair (1: 50) is added with a time limit of 100ms. A non-expired value already existed so true is returned and the old value was overwritten.
At t=50, get(1) is called which returned 50.
At t=120, get(1) is called which returned 50.
At t=140, key=1 expires.
At t=200, get(1) is called but the cache is empty so -1 is returned.
At t=250, count() returns 0 because the cache is empty.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
Uses a Map to store `{value, timer}` for each key. On `set`, clear any existing timer and create a new `setTimeout` that deletes the key after `duration` ms. On `get`, return the value if the key exists. On `count`, return the Map's size.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `actions = ["TimeLimitedCache", "set", "get", "count", "get"]
values = [[], [1, 42, 100], [1], [], [1]]
timeDelays = [0, 0, 50, 50, 150]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, false, 42, 1, -1]`.
4. **Verification:** At t=0, the cache is constructed.
At t=0, a key-value pair (1: 42) is added with a time limit of 100ms. The value doesn't exist so false is returned.
At t=50, key=1 is requested and the value of 42 is returned.
At t=50, count() is called and there is one active key in the cache.
At t=100, key=1 expires.
At t=150, get(1) is called but -1 is returned because the cache is empty.

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
var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration
 * @return {boolean}
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();

    // Check whether an unexpired key already exists
    const exists = this.cache.has(key) &&
                   this.cache.get(key).expiry > now;

    // Store/overwrite the value and expiration time
    this.cache.set(key, {
        value: value,
        expiry: now + duration
    });

    return exists;
};

/** 
 * @param {number} key
 * @return {number}
 */
TimeLimitedCache.prototype.get = function(key) {
    const now = Date.now();

    if (!this.cache.has(key)) {
        return -1;
    }

    const item = this.cache.get(key);

    // Expired
    if (item.expiry <= now) {
        this.cache.delete(key);
        return -1;
    }

    return item.value;
};

/** 
 * @return {number}
 */
TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    let count = 0;

    for (const [key, item] of this.cache) {
        if (item.expiry > now) {
            count++;
        } else {
            this.cache.delete(key);
        }
    }

    return count;
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
- [2637. Promise Time Limit](../../2501-3000/2637-promise-time-limit/)
- [146. LRU Cache](../../0001-0500/0146-lru-cache/)
- [460. LFU Cache](../../0001-0500/0460-lfu-cache/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cache-with-time-limit/)
