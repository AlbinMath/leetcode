class TextEditor:
    def __init__(self):
        self.left = []     # chars left of cursor, in order
        self.right = []    # chars right of cursor, reversed (top = next char)

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        k = min(k, len(self.left))
        if k:
            del self.left[-k:]
        return k

    def _last10(self) -> str:
        return ''.join(self.left[-10:])

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.left))):
            self.right.append(self.left.pop())
        return self._last10()

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right))):
            self.left.append(self.right.pop())
        return self._last10()
