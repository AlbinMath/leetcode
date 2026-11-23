# LeetCode 381: Insert Delete GetRandom O(1) - Duplicates allowed

**LeetCode Problem #381 — Insert Delete GetRandom O(1) - Duplicates allowed**
Solve LeetCode Insert Delete GetRandom O(1) - Duplicates allowed using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Insert Delete GetRandom O(1) - Duplicates allowed |
| LeetCode | #381 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
`RandomizedCollection` is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.

Implement the `RandomizedCollection` class:

`RandomizedCollection()` Initializes the empty `RandomizedCollection` object. 
 `bool insert(int val)` Inserts an item `val` into the multiset, even if the item is already present. Returns `true` if the item is not present, `false` otherwise. 
 `bool remove(int val)` Removes an item `val` from the multiset if present. Returns `true` if the item is present, `false` otherwise. Note that if `val` has multiple occurrences in the multiset, we only remove one of them. 
 `int getRandom()` Returns a random element from the current multiset of elements. The probability of each element being returned is **linearly related** to the number of the same values the multiset contains.

You must implement the functions of the class such that each function works on **average** `O(1)` time complexity.

**Note:** The test cases are generated such that `getRandom` will only be called if there is **at least one** item in the `RandomizedCollection`.

## Constraints
- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls **in total** will be made to `insert`, `remove`, and `getRandom`.
- There will be **at least one** element in the data structure when `getRandom` is called.

## Examples
### Example 1
- **Input:** `["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]`
- **Output:** `[null, true, false, true, 2, true, 1]`
- **Explanation:** RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1); // return true since the collection does not contain 1.
 // Inserts 1 into the collection.
randomizedCollection.insert(1); // return false since the collection contains 1.
 // Inserts another 1 into the collection. Collection now contains [1,1].
randomizedCollection.insert(2); // return true since the collection does not contain 2.
 // Inserts 2 into the collection. Collection now contains [1,1,2].
randomizedCollection.getRandom(); // getRandom should:
 // - return 1 with probability 2/3, or
 // - return 2 with probability 1/3.
randomizedCollection.remove(1); // return true since the collection contains 1.
 // Removes 1 from the collection. Collection now contains [1,2].
randomizedCollection.getRandom(); // getRandom should return 1 or 2, both equally likely.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Insert Delete GetRandom O(1) - Duplicates allowed**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, true, false, true, 2, true, 1]`.
4. **Verification:** RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1); // return true since the collection does not contain 1.
 // Inserts 1 into the collection.
randomizedCollection.insert(1); // return false since the collection contains 1.
 // Inserts another 1 into the collection. Collection now contains [1,1].
randomizedCollection.insert(2); // return true since the collection does not contain 2.
 // Inserts 2 into the collection. Collection now contains [1,1,2].
randomizedCollection.getRandom(); // getRandom should:
 // - return 1 with probability 2/3, or
 // - return 2 with probability 1/3.
randomizedCollection.remove(1); // return true since the collection contains 1.
 // Removes 1 from the collection. Collection now contains [1,2].
randomizedCollection.getRandom(); // getRandom should return 1 or 2, both equally likely.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False
        i = self.idx[val].pop()
        last = self.nums[-1]
        last_pos = len(self.nums) - 1
        self.nums[i] = last
        self.idx[last].add(i)
        self.idx[last].discard(last_pos)
        self.nums.pop()
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
- [380. Insert Delete GetRandom O(1)](../../0001-0500/0380-insert-delete-getrandom-o1/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [80. Remove Duplicates from Sorted Array II](../../0001-0500/0080-remove-duplicates-from-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)
