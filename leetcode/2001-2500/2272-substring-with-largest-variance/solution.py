from collections import defaultdict

class Solution(object):
    def largestVariance(self, s):
        indices = defaultdict(list)
        for i, ch in enumerate(s):
            indices[ch].append(i)

        chars = list(indices.keys())
        max_var = 0

        for major in chars:
            for minor in chars:
                if major == minor:
                    continue

                pos_maj = indices[major]
                pos_min = indices[minor]
                rest_minor = len(pos_min)
                major_count = 0
                minor_count = 0

                i = j = 0
                while i < len(pos_maj) and j < len(pos_min):
                    if pos_maj[i] < pos_min[j]:
                        major_count += 1
                        i += 1
                    else:
                        minor_count += 1
                        rest_minor -= 1
                        j += 1

                    if minor_count > 0:
                        max_var = max(max_var, major_count - minor_count)

                    if major_count < minor_count and rest_minor > 0:
                        major_count = 0
                        minor_count = 0

                # Case 1: Trailing 'major' characters after all 'minor' characters were processed
                if minor_count > 0 and i < len(pos_maj):
                    major_count += len(pos_maj) - i
                    max_var = max(max_var, major_count - minor_count)

                # Case 2: All 'major' characters appeared before a remaining 'minor' (e.g., "bbc")
                if minor_count == 0 and j < len(pos_min):
                    max_var = max(max_var, major_count - 1)

        return max_var
