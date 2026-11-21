class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def devowel(w: str) -> str:
            return ''.join('*' if ch in vowels else ch for ch in w.lower())

        exact = set(wordlist)
        case_map = {}
        vowel_map = {}

        for w in wordlist:
            case_map.setdefault(w.lower(), w)
            vowel_map.setdefault(devowel(w), w)

        res = []
        for q in queries:
            if q in exact:
                res.append(q)
            elif q.lower() in case_map:
                res.append(case_map[q.lower()])
            else:
                res.append(vowel_map.get(devowel(q), ""))
        return res
