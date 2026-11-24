import heapq

class Solution:
    def fullBloomFlowers(self, flowers, people):
        flowers.sort()
        order = sorted(range(len(people)), key=lambda i: people[i])
        ans = [0] * len(people)
        heap, j = [], 0
        for i in order:
            t = people[i]
            while j < len(flowers) and flowers[j][0] <= t:
                heapq.heappush(heap, flowers[j][1])
                j += 1
            while heap and heap[0] < t:
                heapq.heappop(heap)
            ans[i] = len(heap)
        return ans
