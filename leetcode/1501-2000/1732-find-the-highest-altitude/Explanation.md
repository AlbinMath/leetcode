# LeetCode 1732: Find the Highest Altitude

**LeetCode Problem #1732 — Find the Highest Altitude**
Solve LeetCode Find the Highest Altitude using JavaScript, Kotlin, Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Highest Altitude |
| LeetCode | #1732 |
| Difficulty | Easy |
| Language | JavaScript, Kotlin, Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a biker going on a road trip. The road trip consists of `n + 1` points at various altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the **net gain in altitude** between points `i`​​​​​​ and `i + 1` for all (`0 <= i < n)`. Return *the **highest altitude** of a point.*

## Constraints
- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`

## Examples
### Example 1
- **Input:** `gain = [-5,1,5,0,-7]`
- **Output:** `1`
- **Explanation:** The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

### Example 2
- **Input:** `gain = [-4,-3,-2,-1,4,3,2]`
- **Output:** `0`
- **Explanation:** The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code simply accumulates the altitude by adding each gain value to a running sum, tracking the maximum value encountered. Start at `0`, add each `gain[i]`, and keep updating the highest altitude.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `gain = [-5,1,5,0,-7]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript, Kotlin, Python

## Source Code
- [solution.js](./solution.js)
- [solution.kt](./solution.kt)
- [solution.py](./solution.py)


### JavaScript
```javascript
var largestAltitude = function(gain) {
    let altitude = 0;
    let maxAltitude = 0;

    for (let i = 0; i < gain.length; i++) {
        altitude += gain[i];
        maxAltitude = Math.max(maxAltitude, altitude);
    }

    return maxAltitude;
};
```

### Kotlin
```kotlin
class Solution {
    fun largestAltitude(gain: IntArray): Int {
        var altitude = 0
        var highest = 0

        for (g in gain) {
            altitude += g
            highest = maxOf(highest, altitude)
        }

        return highest
    }
}
```

### Python
```python
class Solution:
    def largestAltitude(self, gain):
        h = ans = 0
        for x in gain:
            h += x
            ans = max(ans, h)
        return ans
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [176. Second Highest Salary](../../0001-0500/0176-second-highest-salary/)
- [177. Nth Highest Salary](../../0001-0500/0177-nth-highest-salary/)
- [184. Department Highest Salary](../../0001-0500/0184-department-highest-salary/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-highest-altitude/)
