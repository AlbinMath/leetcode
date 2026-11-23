# LeetCode 4020: Elevator Requests I

**LeetCode Problem #4020 — Elevator Requests I**
Solve LeetCode Elevator Requests I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Elevator Requests I |
| LeetCode | #4020 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n` denoting the number of floors in a building, where the floors are numbered from 0 to `n - 1`.

You are also given an integer array `requests`, where `requests` represents the sequence of floor requests.

An elevator starts at floor 0 and follows these rules:

The elevator moves one floor per second. 
 The elevator serves requests in the given order. 
 If the elevator is already on the requested floor, no movement is needed. 
 After serving a request, the elevator immediately starts moving toward the next request.

Return the **total time** in seconds required to serve all requests.

## Constraints
- `1 <= n <= 100`
- `1 <= requests.length <= 100`
- `0 <= requests[i] <= n - 1`

## Examples
### Example 1
- **Input:** `n = 5, requests = [2,1,4,3]`
- **Output:** `7`
- **Explanation:** `requests[0] = 2`: Moving from floor 0 to floor 2 takes 2 seconds. 
 `requests[1] = 1`: Moving from floor 2 to floor 1 takes 1 second. 
 `requests[2] = 4`: Moving from floor 1 to floor 4 takes 3 seconds. 
 `requests[3] = 3`: Moving from floor 4 to floor 3 takes 1 second. 
 

 The total time required is `2 + 1 + 3 + 1 = 7` seconds.

### Example 2
- **Input:** `n = 3, requests = [2,0,0]`
- **Output:** `4`
- **Explanation:** `requests[0] = 2`: Moving from floor 0 to floor 2 takes 2 seconds. 
 `requests[1] = 0`: Moving from floor 2 to floor 0 takes 2 seconds. 
 `requests[2] = 0`: No movement is needed. 
 

 The total time required is `2 + 2 + 0 = 4` seconds.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Elevator Requests I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, requests = [2,1,4,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** `requests[0] = 2`: Moving from floor 0 to floor 2 takes 2 seconds. 
 `requests[1] = 1`: Moving from floor 2 to floor 1 takes 1 second. 
 `requests[2] = 4`: Moving from floor 1 to floor 4 takes 3 seconds. 
 `requests[3] = 3`: Moving from floor 4 to floor 3 takes 1 second. 
 

 The total time required is `2 + 1 + 3 + 1 = 7` seconds.

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
class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        cur = 0
        total = 0
        for f in requests:
            total += abs(f - cur)
            cur = f
        return total
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
- [4027. Elevator Requests III](../../4001-4500/4386-elevator-requests-iii/)
- [602. Friend Requests II: Who Has the Most Friends](../../0501-1000/0602-friend-requests-ii-who-has-the-most-friends/)
- [1601. Maximum Number of Achievable Transfer Requests](../../1501-2000/1723-maximum-number-of-achievable-transfer-requests/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/elevator-requests-i/)
