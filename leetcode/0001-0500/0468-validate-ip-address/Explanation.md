# LeetCode 468: Validate IP Address

**LeetCode Problem #468 — Validate IP Address**
Solve LeetCode Validate IP Address using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Validate IP Address |
| LeetCode | #468 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `queryIP`, return `"IPv4"` if IP is a valid IPv4 address, `"IPv6"` if IP is a valid IPv6 address or `"Neither"` if IP is not a correct IP of any type.

**A valid IPv4** address is an IP in the form `"x_1.x_2.x_3.x_4"` where `0 <= x_i <= 255` and `x_i` **cannot contain** leading zeros. For example, `"192.168.1.1"` and `"192.168.1.0"` are valid IPv4 addresses while `"192.168.01.1"`, `"192.168.1.00"`, and `"192.168@1.1"` are invalid IPv4 addresses.

**A valid IPv6** address is an IP in the form `"x_1:x_2:x_3:x_4:x_5:x_6:x_7:x_8"` where:

`1 <= x_i.length <= 4` 
 `x_i` is a **hexadecimal string** which may contain digits, lowercase English letter (`'a'` to `'f'`) and upper-case English letters (`'A'` to `'F'`). 
 Leading zeros are allowed in `x_i`.

For example, "`2001:0db8:85a3:0000:0000:8a2e:0370:7334"` and "`2001:db8:85a3:0:0:8A2E:0370:7334"` are valid IPv6 addresses, while "`2001:0db8:85a3::8A2E:037j:7334"` and "`02001:0db8:85a3:0000:0000:8a2e:0370:7334"` are invalid IPv6 addresses.

## Constraints
- `queryIP` consists only of English letters, digits and the characters `'.'` and `':'`.

## Examples
### Example 1
- **Input:** `queryIP = "172.16.254.1"`
- **Output:** `"IPv4"`
- **Explanation:** This is a valid IPv4 address, return "IPv4".

### Example 2
- **Input:** `queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"`
- **Output:** `"IPv6"`
- **Explanation:** This is a valid IPv6 address, return "IPv6".

### Example 3
- **Input:** `queryIP = "256.256.256.256"`
- **Output:** `"Neither"`
- **Explanation:** This is neither a IPv4 address nor a IPv6 address.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Validate IP Address**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `queryIP = "172.16.254.1"`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"IPv4"`.
4. **Verification:** This is a valid IPv4 address, return "IPv4".

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def valid_v4(ip: str) -> bool:
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for p in parts:
                if not p or not p.isdigit() or len(p) > 3:
                    return False
                if len(p) > 1 and p[0] == '0':
                    return False
                if int(p) > 255:
                    return False
            return True

        def valid_v6(ip: str) -> bool:
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            hex_chars = set("0123456789abcdefABCDEF")
            for p in parts:
                if not 1 <= len(p) <= 4:
                    return False
                if any(ch not in hex_chars for ch in p):
                    return False
            return True

        if '.' in queryIP and valid_v4(queryIP):
            return "IPv4"
        if ':' in queryIP and valid_v6(queryIP):
            return "IPv6"
        return "Neither"
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
- [1108. Defanging an IP Address](../../1001-1500/1205-defanging-an-ip-address/)
- [93. Restore IP Addresses](../../0001-0500/0093-restore-ip-addresses/)
- [3451. Find Invalid IP Addresses](../../3501-4000/3792-find-invalid-ip-addresses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/validate-ip-address/)
