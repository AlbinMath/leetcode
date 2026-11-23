class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        out = []
        for i, w in enumerate(words):
            w = w.lower()
            if i > 0:
                w = w.capitalize()
            out.append(w)
        s = "".join(c for c in "".join(out) if c.isalpha())
        return ("#" + s)[:100]
