class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = left = 0
        trie = {}

        def add(x, v):
            node = trie
            for b in range(20, -1, -1):
                bit = (x >> b) & 1
                node = node.setdefault(bit, {})
                node['#'] = node.get('#', 0) + v

        def query(x):
            node = trie
            res = 0
            for b in range(20, -1, -1):
                bit = (x >> b) & 1
                t = 1 - bit
                if t in node and node[t]['#'] > 0:
                    res |= 1 << b
                    node = node[t]
                else:
                    node = node[bit]
            return res

        for x in nums:
            add(x, 1)
            while nums[left] * 2 < x:
                add(nums[left], -1)
                left += 1
            ans = max(ans, query(x))
        return ans
