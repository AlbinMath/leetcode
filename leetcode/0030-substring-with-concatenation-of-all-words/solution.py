from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        # Required frequency of each word
        target = Counter(words)

        result = []

        # Try each possible alignment
        for offset in range(word_len):
            left = offset
            right = offset

            current = Counter()
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                # Word is not in words
                if word not in target:
                    current.clear()
                    count = 0
                    left = right
                    continue

                current[word] += 1
                count += 1

                # Too many occurrences of this word
                while current[word] > target[word]:
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

                # Found all words
                if count == word_count:
                    result.append(left)

                    # Move window forward
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

        return result
