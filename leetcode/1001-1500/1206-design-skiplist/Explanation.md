# LeetCode 1206: Design Skiplist

**LeetCode Problem #1206 — Design Skiplist**
Solve LeetCode Design Skiplist using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Skiplist |
| LeetCode | #1206 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Design a **Skiplist** without using any built-in libraries.

A **skiplist** is a data structure that takes `O(log(n))` time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists is just simple linked lists.

For example, we have a Skiplist containing `[30,40,50,60,70,90]` and we want to add `80` and `45` into it. The Skiplist works this way:

Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, add, erase and search can be faster than `O(n)`. It can be proven that the average time complexity for each operation is `O(log(n))` and space complexity is `O(n)`.

See more about Skiplist: https://en.wikipedia.org/wiki/Skip_list

Implement the `Skiplist` class:

`Skiplist()` Initializes the object of the skiplist. 
 `bool search(int target)` Returns `true` if the integer `target` exists in the Skiplist or `false` otherwise. 
 `void add(int num)` Inserts the value `num` into the SkipList. 
 `bool erase(int num)` Removes the value `num` from the Skiplist and returns `true`. If `num` does not exist in the Skiplist, do nothing and return `false`. If there exist multiple `num` values, removing any one of them is fine.

Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

## Constraints
- `0 <= num, target <= 2 * 10^4`
- At most `5 * 10^4` calls will be made to `search`, `add`, and `erase`.

## Examples
### Example 1
- **Input:** `["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]`
- **Output:** `[null, null, null, null, false, null, true, false, true, false]`
- **Explanation:** Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0); // return False
skiplist.add(4);
skiplist.search(1); // return True
skiplist.erase(0); // return False, 0 is not in skiplist.
skiplist.erase(1); // return True
skiplist.search(1); // return False, 1 has already been erased.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Design Skiplist**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, null, false, null, true, false, true, false]`.
4. **Verification:** Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0); // return False
skiplist.add(4);
skiplist.search(1); // return True
skiplist.erase(0); // return False, 0 is not in skiplist.
skiplist.erase(1); // return True
skiplist.search(1); // return False, 1 has already been erased.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var Skiplist = function() {
    this.MAX_LEVEL = 16;
    this.P = 0.5;

    this.head = new SkipNode(-1, this.MAX_LEVEL);
    this.level = 1;
};

// Skiplist node
var SkipNode = function(val, level) {
    this.val = val;
    this.forward = new Array(level).fill(null);
};

// Generate random level
Skiplist.prototype.randomLevel = function() {
    let level = 1;

    while (
        Math.random() < this.P &&
        level < this.MAX_LEVEL
    ) {
        level++;
    }

    return level;
};

// Search
Skiplist.prototype.search = function(target) {
    let current = this.head;

    for (let i = this.level - 1; i >= 0; i--) {
        while (
            current.forward[i] &&
            current.forward[i].val < target
        ) {
            current = current.forward[i];
        }
    }

    current = current.forward[0];

    return current !== null && current.val === target;
};

// Add
Skiplist.prototype.add = function(num) {
    let update = new Array(this.MAX_LEVEL);
    let current = this.head;

    // Find insertion positions
    for (let i = this.level - 1; i >= 0; i--) {
        while (
            current.forward[i] &&
            current.forward[i].val < num
        ) {
            current = current.forward[i];
        }

        update[i] = current;
    }

    // Generate random level
    let newLevel = this.randomLevel();

    if (newLevel > this.level) {
        for (let i = this.level; i < newLevel; i++) {
            update[i] = this.head;
        }

        this.level = newLevel;
    }

    // Create and insert node
    let node = new SkipNode(num, newLevel);

    for (let i = 0; i < newLevel; i++) {
        node.forward[i] = update[i].forward[i];
        update[i].forward[i] = node;
    }
};

// Erase
Skiplist.prototype.erase = function(num) {
    let update = new Array(this.MAX_LEVEL);
    let current = this.head;

    // Find node and its predecessors
    for (let i = this.level - 1; i >= 0; i--) {
        while (
            current.forward[i] &&
            current.forward[i].val < num
        ) {
            current = current.forward[i];
        }

        update[i] = current;
    }

    current = current.forward[0];

    if (!current || current.val !== num) {
        return false;
    }

    // Remove node from every level where it exists
    for (let i = 0; i < this.level; i++) {
        if (update[i].forward[i] === current) {
            update[i].forward[i] = current.forward[i];
        }
    }

    // Reduce empty top levels
    while (
        this.level > 1 &&
        this.head.forward[this.level - 1] === null
    ) {
        this.level--;
    }

    return true;
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)
- [355. Design Twitter](../../0001-0500/0355-design-twitter/)
- [622. Design Circular Queue](../../0501-1000/0622-design-circular-queue/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-skiplist/)
