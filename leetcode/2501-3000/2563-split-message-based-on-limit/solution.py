class Solution(object):
    def splitMessage(self, message, limit):
        n = len(message)
        b = 0
        prefix_a_digits = 0

        while True:
            b += 1
            len_b = len(str(b))
            # Even the final part "<b/b>" must leave at least 1 character for message
            if 3 + 2 * len_b >= limit:
                return []

            prefix_a_digits += len_b
            total_suffix = 3 * b + prefix_a_digits + b * len_b
            if b * limit - total_suffix >= n:
                break

        res = []
        idx = 0
        for a in range(1, b + 1):
            suffix = "<{}/{}>".format(a, b)
            take = limit - len(suffix)
            res.append(message[idx:idx + take] + suffix)
            idx += take

        return res
