class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = set("aeiou")
        words = s.split(' ')

        def count(w: str) -> int:
            return sum(c in vowels for c in w)

        target = count(words[0])
        for i in range(1, len(words)):
            if count(words[i]) == target:
                words[i] = words[i][::-1]
        return ' '.join(words)
