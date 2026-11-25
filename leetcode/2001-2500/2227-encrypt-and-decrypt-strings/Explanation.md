# LeetCode 2227: Encrypt and Decrypt Strings

**LeetCode Problem #2227 — Encrypt and Decrypt Strings**
Solve LeetCode Encrypt and Decrypt Strings using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Encrypt and Decrypt Strings |
| LeetCode | #2227 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a character array `keys` containing **unique** characters and a string array `values` containing strings of length 2. You are also given another string array `dictionary` that contains all permitted original strings after decryption. You should implement a data structure that can encrypt or decrypt a **0-indexed** string.

A string is **encrypted** with the following process:

For each character `c` in the string, we find the index `i` satisfying `keys[i] == c` in `keys`. 
 Replace `c` with `values[i]` in the string.

Note that in case a character of the string is **not present** in `keys`, the encryption process cannot be carried out, and an empty string `""` is returned.

A string is **decrypted** with the following process:

For each substring `s` of length 2 occurring at an even index in the string, we find an `i` such that `values[i] == s`. If there are multiple valid `i`, we choose **any** one of them. This means a string could have multiple possible strings it can decrypt to. 
 Replace `s` with `keys[i]` in the string.

Implement the `Encrypter` class:

`Encrypter(char[] keys, String[] values, String[] dictionary)` Initializes the `Encrypter` class with `keys, values`, and `dictionary`. 
 `String encrypt(String word1)` Encrypts `word1` with the encryption process described above and returns the encrypted string. 
 `int decrypt(String word2)` Returns the number of possible strings `word2` could decrypt to that also appear in `dictionary`.

## Constraints
- `1 <= keys.length == values.length <= 26`
- `values[i].length == 2`
- `1 <= dictionary.length <= 100`
- `1 <= dictionary[i].length <= 100`
- All `keys[i]` and `dictionary[i]` are **unique**.
- `1 <= word1.length <= 2000`
- `2 <= word2.length <= 200`
- All `word1[i]` appear in `keys`.
- `word2.length` is even.
- `keys`, `values[i]`, `dictionary[i]`, `word1`, and `word2` only contain lowercase English letters.
- At most `200` calls will be made to `encrypt` and `decrypt` **in total**.

## Examples
### Example 1
- **Input:** `["Encrypter", "encrypt", "decrypt"]
[[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]`
- **Output:** `[null, "eizfeiam", 2]`
- **Explanation:** Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]);
encrypter.encrypt("abcd"); // return "eizfeiam". 
 // 'a' maps to "ei", 'b' maps to "zf", 'c' maps to "ei", and 'd' maps to "am".
encrypter.decrypt("eizfeiam"); // return 2. 
 // "ei" can map to 'a' or 'c', "zf" maps to 'b', and "am" maps to 'd'. 
 // Thus, the possible strings after decryption are "abad", "cbad", "abcd", and "cbcd". 
 // 2 of those strings, "abad" and "abcd", appear in dictionary, so the answer is 2.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Encrypt and Decrypt Strings**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Encrypter", "encrypt", "decrypt"]
[[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, "eizfeiam", 2]`.
4. **Verification:** Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]);
encrypter.encrypt("abcd"); // return "eizfeiam". 
 // 'a' maps to "ei", 'b' maps to "zf", 'c' maps to "ei", and 'd' maps to "am".
encrypter.decrypt("eizfeiam"); // return 2. 
 // "ei" can map to 'a' or 'c', "zf" maps to 'b', and "am" maps to 'd'. 
 // Thus, the possible strings after decryption are "abad", "cbad", "abcd", and "cbcd". 
 // 2 of those strings, "abad" and "abcd", appear in dictionary, so the answer is 2.

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
from collections import Counter

class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.mp = dict(zip(keys, values))
        self.cnt = Counter(self.encrypt(w) for w in dictionary)

    def encrypt(self, word1: str) -> str:
        return ''.join(self.mp.get(c, '') for c in word1) if all(c in self.mp for c in word1) else ''

    def decrypt(self, word2: str) -> int:
        return self.cnt[word2]
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
- [1309. Decrypt String from Alphabet to Integer Mapping](../../1001-1500/1309-decrypt-string-from-alphabet-to-integer-mapping/)
- [43. Multiply Strings](../../0001-0500/0043-multiply-strings/)
- [205. Isomorphic Strings](../../0001-0500/0205-isomorphic-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/encrypt-and-decrypt-strings/)
