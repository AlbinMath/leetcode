# LeetCode 2502: Design Memory Allocator

**LeetCode Problem #2502 — Design Memory Allocator**
Solve LeetCode Design Memory Allocator using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Memory Allocator |
| LeetCode | #2502 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` representing the size of a **0-indexed** memory array. All memory units are initially free.

You have a memory allocator with the following functionalities:

**Allocate **a block of `size` consecutive free memory units and assign it the id `mID`. 
 **Free** all memory units with the given id `mID`.

**Note** that:

Multiple blocks can be allocated to the same `mID`. 
 You should free all the memory units with `mID`, even if they were allocated in different blocks.

Implement the `Allocator` class:

`Allocator(int n)` Initializes an `Allocator` object with a memory array of size `n`. 
 `int allocate(int size, int mID)` Find the **leftmost** block of `size` **consecutive** free memory units and allocate it with the id `mID`. Return the block's first index. If such a block does not exist, return `-1`. 
 `int freeMemory(int mID)` Free all memory units with the id `mID`. Return the number of memory units you have freed.

## Constraints
- `1 <= n, size, mID <= 1000`
- At most `1000` calls will be made to `allocate` and `freeMemory`.

## Examples
### Example 1
- **Input:** `["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]`
- **Output:** `[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]`
- **Explanation:** Allocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory units are initially free.
loc.allocate(1, 1); // The leftmost block's first index is 0. The memory array becomes [

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Design Memory Allocator**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]`.
4. **Verification:** Allocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory units are initially free.
loc.allocate(1, 1); // The leftmost block's first index is 0. The memory array becomes [

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
var Allocator = function(n) {
    this.n = n;
    this.memory = new Int32Array(n);
    this.blocks = new Map();
};
Allocator.prototype.allocate = function(size, mID) {
    let freeRun = 0;
    
    for (let i = 0; i < this.n; i++) {
        if (this.memory[i] === 0) {
            freeRun++;
            if (freeRun === size) {
                const start = i - size + 1;
                this.memory.fill(mID, start, i + 1);
                if (!this.blocks.has(mID)) {
                    this.blocks.set(mID, []);
                }
                this.blocks.get(mID).push([start, size]);
                return start;
            }
        } else {
            freeRun = 0;
        }
    }
    
    return -1;
};
Allocator.prototype.freeMemory = function(mID) {
    const ranges = this.blocks.get(mID);
    if (!ranges) return 0;
    
    let freed = 0;
    for (const [start, size] of ranges) {
        this.memory.fill(0, start, start + size);
        freed += size;
    }
    
    this.blocks.delete(mID);
    return freed;
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
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)
- [355. Design Twitter](../../0001-0500/0355-design-twitter/)
- [622. Design Circular Queue](../../0501-1000/0860-design-circular-queue/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-memory-allocator/)
