from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        return heapq.nsmallest(k, count, key=lambda w: (-count[w], w))
