class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        # left to right: cost of bringing balls from the left into box i
        balls = ops = 0
        for i in range(n):
            ans[i] += ops
            if boxes[i] == '1':
                balls += 1
            ops += balls

        # right to left: cost of bringing balls from the right into box i
        balls = ops = 0
        for i in range(n - 1, -1, -1):
            ans[i] += ops
            if boxes[i] == '1':
                balls += 1
            ops += balls

        return ans
        
