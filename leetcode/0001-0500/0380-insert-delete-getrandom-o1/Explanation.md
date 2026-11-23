# LeetCode 380: Insert Delete GetRandom O(1)

**LeetCode Problem #380 — Insert Delete GetRandom O(1)**
Solve LeetCode Insert Delete GetRandom O(1) using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Insert Delete GetRandom O(1) |
| LeetCode | #380 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Implement the `RandomizedSet` class:

`RandomizedSet()` Initializes the `RandomizedSet` object. 
 `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise. 
 `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise. 
 `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in **average** `O(1)` time complexity.

## Constraints
- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be **at least one** element in the data structure when `getRandom` is called.

## Examples
### Example 1
- **Input:** `["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]`
- **Output:** `[null, true, false, true, 2, true, false, 2]`
- **Explanation:** RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Insert Delete GetRandom O(1)**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, true, false, true, 2, true, false, 2]`.
4. **Verification:** RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var RandomizedSet = function() {
    this.nums = [];
    this.indices = new Map();
};

RandomizedSet.prototype.insert = function(val) {
    if (this.indices.has(val)) {
        return false;
    }

    this.indices.set(val, this.nums.length);
    this.nums.push(val);

    return true;
};

RandomizedSet.prototype.remove = function(val) {
    if (!this.indices.has(val)) {
        return false;
    }

    const index = this.indices.get(val);
    const lastVal = this.nums[this.nums.length - 1];

    this.nums[index] = lastVal;
    this.indices.set(lastVal, index);

    this.nums.pop();
    this.indices.delete(val);

    return true;
};

RandomizedSet.prototype.getRandom = function() {
    const randomIndex = Math.floor(Math.random() * this.nums.length);
    return this.nums[randomIndex];
};
```

### Python
```python
import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        # Get the index of the value to remove
        idx = self.indices[val]

        # Get the last element
        last = self.nums[-1]

        # Move the last element into the removed element's position
        self.nums[idx] = last
        self.indices[last] = idx

        # Remove the last element
        self.nums.pop()
        del self.indices[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [381. Insert Delete GetRandom O(1) - Duplicates allowed](../../0001-0500/0381-insert-delete-getrandom-o1---duplicates-allowed/)
- [196. Delete Duplicate Emails](../../0001-0500/0196-delete-duplicate-emails/)
- [237. Delete Node in a Linked List](../../0001-0500/0237-delete-node-in-a-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/)
