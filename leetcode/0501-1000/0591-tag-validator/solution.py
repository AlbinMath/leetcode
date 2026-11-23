class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i, n = 0, len(code)

        while i < n:
            if i > 0 and not stack:
                return False

            if code.startswith("<![CDATA[", i):
                j = code.find("]]>", i + 9)
                if j == -1 or not stack:
                    return False
                i = j + 3

            elif code.startswith("</", i):
                j = code.find(">", i)
                if j == -1:
                    return False
                tag = code[i + 2:j]
                if not stack or stack.pop() != tag:
                    return False
                i = j + 1

            elif code[i] == "<":
                j = code.find(">", i)
                if j == -1:
                    return False
                tag = code[i + 1:j]
                if not 1 <= len(tag) <= 9 or not tag.isupper() or not tag.isalpha():
                    return False
                stack.append(tag)
                i = j + 1

            else:
                i += 1

        return not stack
