
class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]

        transformations = set()

        for word in words:
            code = ""

            for ch in word:
                code += morse[ord(ch) - ord('a')]

            transformations.add(code)

        return len(transformations)

