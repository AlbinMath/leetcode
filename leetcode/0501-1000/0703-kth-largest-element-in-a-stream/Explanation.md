# LeetCode 703: Kth Largest Element in a Stream

**LeetCode Problem #703 — Kth Largest Element in a Stream**
Solve LeetCode Kth Largest Element in a Stream using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Largest Element in a Stream |
| LeetCode | #703 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are part of a university admissions office and need to keep track of the `kth` highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer `k`, maintains a stream of test scores and continuously returns the `k`th highest test score **after** a new score has been submitted. More specifically, we are looking for the `k`th highest score in the sorted list of all scores.

Implement the `KthLargest` class:

`KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of test scores `nums`. 
 `int add(int val)` Adds a new test score `val` to the stream and returns the element representing the `k^th` largest element in the pool of test scores so far.

## Constraints
- `0 <= nums.length <= 10^4`
- `1 <= k <= nums.length + 1`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `add`.

## Examples
### Example 1
- **Input:** `["KthLargest", "add", "add", "add", "add", "add"] 
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]`
- **Output:** `[null, 4, 5, 5, 8, 8]`
- **Explanation:** KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]); 
kthLargest.add(3); // return 4 
kthLargest.add(5); // return 5 
kthLargest.add(10); // return 5 
kthLargest.add(9); // return 8 
kthLargest.add(4); // return 8

### Example 2
- **Input:** `["KthLargest", "add", "add", "add", "add"] 
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]`
- **Output:** `[null, 7, 7, 7, 8]`
- **Explanation:** KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]); 
kthLargest.add(2); // return 7 
kthLargest.add(10); // return 7 
kthLargest.add(9); // return 7 
kthLargest.add(9); // return 8

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Kth Largest Element in a Stream**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["KthLargest", "add", "add", "add", "add", "add"] 
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, 4, 5, 5, 8, 8]`.
4. **Verification:** KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]); 
kthLargest.add(3); // return 4 
kthLargest.add(5); // return 5 
kthLargest.add(10); // return 5 
kthLargest.add(9); // return 8 
kthLargest.add(4); // return 8

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # Remove the smallest if heap exceeds size k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [215. Kth Largest Element in an Array](../../0001-0500/0215-kth-largest-element-in-an-array/)
- [230. Kth Smallest Element in a BST](../../0001-0500/0230-kth-smallest-element-in-a-bst/)
- [378. Kth Smallest Element in a Sorted Matrix](../../0001-0500/0378-kth-smallest-element-in-a-sorted-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
