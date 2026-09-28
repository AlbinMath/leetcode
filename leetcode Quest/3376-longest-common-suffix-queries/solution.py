class Solution(object):

    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """

        # Trie represented using dictionaries.
        # Each node:
        # [children, best_index]
        trie = [
            [{}, -1]
        ]

        # Find the best container index according to:
        # 1. shortest length
        # 2. smallest index
        def better(i, j):
            if j == -1:
                return i

            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return i

            if len(wordsContainer[i]) > len(wordsContainer[j]):
                return j

            return min(i, j)

        # --------------------------------------------------
        # Build Trie using reversed container strings
        # --------------------------------------------------

        for idx, word in enumerate(wordsContainer):

            node = 0

            # Root represents empty suffix.
            trie[node][1] = better(idx, trie[node][1])

            for ch in reversed(word):

                children = trie[node][0]

                if ch not in children:
                    children[ch] = len(trie)
                    trie.append([{}, -1])

                node = children[ch]

                trie[node][1] = better(idx, trie[node][1])

        # --------------------------------------------------
        # Answer queries
        # --------------------------------------------------

        answer = []

        for word in wordsQuery:

            node = 0

            # At least the empty suffix is always shared.
            best = trie[0][1]

            for ch in reversed(word):

                children = trie[node][0]

                if ch not in children:
                    break

                node = children[ch]

                # This node represents a longer common suffix.
                best = trie[node][1]

            answer.append(best)

        return answer
