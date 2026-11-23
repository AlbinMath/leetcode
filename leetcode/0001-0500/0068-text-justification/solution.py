class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):

            # Find all words that fit in this line
            line_words = []
            line_length = 0

            while i < len(words):
                word_length = len(words[i])

                # Minimum required length:
                # current words + one space before new word
                required = line_length + word_length

                if line_words:
                    required += len(line_words)

                if required > maxWidth:
                    break

                line_words.append(words[i])
                line_length += word_length
                i += 1

            # Last line or single-word line
            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)
                continue

            # Fully justify normal line
            total_spaces = maxWidth - line_length
            gaps = len(line_words) - 1

            spaces_per_gap = total_spaces // gaps
            extra_spaces = total_spaces % gaps

            line = ""

            for j in range(gaps):
                line += line_words[j]
                line += " " * (
                    spaces_per_gap + (1 if j < extra_spaces else 0)
                )

            line += line_words[-1]

            result.append(line)

        return result
