# LeetCode 535: Encode and Decode TinyURL

**LeetCode Problem #535 — Encode and Decode TinyURL**
Solve LeetCode Encode and Decode TinyURL using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Encode and Decode TinyURL |
| LeetCode | #535 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Note: This is a companion problem to the System Design problem: Design TinyURL .

TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the `Solution` class:

`Solution()` Initializes the object of the system. 
 `String encode(String longUrl)` Returns a tiny URL for the given `longUrl`. 
 `String decode(String shortUrl)` Returns the original long URL for the given `shortUrl`. It is guaranteed that the given `shortUrl` was encoded by the same object.

## Constraints
- `1 <= url.length <= 10^4`
- `url` is guranteed to be a valid URL.

## Examples
### Example 1
- **Input:** `url = "https://leetcode.com/problems/design-tinyurl"`
- **Output:** `"https://leetcode.com/problems/design-tinyurl"`
- **Explanation:** Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after decoding it.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Encode and Decode TinyURL**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `url = "https://leetcode.com/problems/design-tinyurl"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"https://leetcode.com/problems/design-tinyurl"`.
4. **Verification:** Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after decoding it.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Codec:
    PREFIX = "http://tinyurl.com/"

    def __init__(self):
        self.id_to_url = {}
        self.url_to_id = {}
        self.next_id = 0

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.url_to_id:
            self.url_to_id[longUrl] = self.next_id
            self.id_to_url[self.next_id] = longUrl
            self.next_id += 1
        return self.PREFIX + str(self.url_to_id[longUrl])

    def decode(self, shortUrl: str) -> str:
        return self.id_to_url[int(shortUrl[len(self.PREFIX):])]
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
- [91. Decode Ways](../../0001-0500/0091-decode-ways/)
- [394. Decode String](../../0001-0500/0394-decode-string/)
- [639. Decode Ways II](../../0501-1000/0639-decode-ways-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/encode-and-decode-tinyurl/)
