class Solution(object):
    def largestPower(self, nums):
        blocks = [list(nums)]
        res = []
        for b in range(14, -1, -1):
            total = 0
            new_blocks = []
            i = 0
            while i < len(blocks):
                blk = blocks[i]
                on = [x for x in blk if (x >> b) & 1]
                if len(on) == len(blk):
                    total += len(blk)
                    new_blocks.append(blk)
                    i += 1
                else:
                    total += len(on)
                    off = [x for x in blk if not (x >> b) & 1]
                    if on:
                        new_blocks.append(on)
                    new_blocks.append(off)
                    new_blocks.extend(blocks[i + 1:])
                    break
            blocks = new_blocks
            res.append(total)
        return res
