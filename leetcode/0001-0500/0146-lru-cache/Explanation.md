# LeetCode 146: LRU Cache

**LeetCode Problem #146 — LRU Cache**
Solve LeetCode LRU Cache using JavaScript, Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | LRU Cache |
| LeetCode | #146 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design a data structure that follows the constraints of a ** Least Recently Used (LRU) cache **.

Implement the `LRUCache` class:

`LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`. 
 `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`. 
 `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

## Constraints
- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls will be made to `get` and `put`.

## Examples
### Example 1
- **Input:** `["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]`
- **Output:** `[null, null, null, 1, null, -1, null, -1, 3, 4]`
- **Explanation:** LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1); // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2); // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1); // return -1 (not found)
lRUCache.get(3); // return 3
lRUCache.get(4); // return 4

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **LRU Cache**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, 1, null, -1, null, -1, 3, 4]`.
4. **Verification:** LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1); // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2); // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1); // return -1 (not found)
lRUCache.get(3); // return 3
lRUCache.get(4); // return 4

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var LRUCache = function(capacity) {
    this.capacity = capacity;
    this.cache = new Map();

    this.head = { key: 0, value: 0, prev: null, next: null };
    this.tail = { key: 0, value: 0, prev: null, next: null };

    this.head.next = this.tail;
    this.tail.prev = this.head;
};

// Remove a node from the list
LRUCache.prototype.remove = function(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
};

// Insert a node right after the head (most recently used)
LRUCache.prototype.insertFront = function(node) {
    node.next = this.head.next;
    node.prev = this.head;

    this.head.next.prev = node;
    this.head.next = node;
};

// Move an existing node to the front
LRUCache.prototype.moveToFront = function(node) {
    this.remove(node);
    this.insertFront(node);
};

LRUCache.prototype.get = function(key) {
    if (!this.cache.has(key)) {
        return -1;
    }

    const node = this.cache.get(key);
    this.moveToFront(node);

    return node.value;
};

LRUCache.prototype.put = function(key, value) {
    if (this.cache.has(key)) {
        const node = this.cache.get(key);
        node.value = value;
        this.moveToFront(node);
        return;
    }

    const node = {
        key,
        value,
        prev: null,
        next: null
    };

    this.cache.set(key, node);
    this.insertFront(node);

    if (this.cache.size > this.capacity) {
        const lru = this.tail.prev;

        this.remove(lru);
        this.cache.delete(lru.key);
    }
};
```

### Python
```python
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Mark this key as most recently used
        self.remove(node)
        self.add_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.value = value
            self.add_to_front(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_front(node)

            if len(self.cache) > self.capacity:
                # Remove the least recently used node
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
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
- [460. LFU Cache](../../0001-0500/0460-lfu-cache/)
- [2622. Cache With Time Limit](../../2501-3000/2622-cache-with-time-limit/)
- [1. Two Sum](../../0001-0500/0001-two-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lru-cache/)
