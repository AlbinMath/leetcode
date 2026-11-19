from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        need = 0  # continuation bytes still expected

        for byte in data:
            byte &= 0xFF
            if need == 0:
                if byte >> 7 == 0b0:
                    need = 0
                elif byte >> 5 == 0b110:
                    need = 1
                elif byte >> 4 == 0b1110:
                    need = 2
                elif byte >> 3 == 0b11110:
                    need = 3
                else:
                    return False
            else:
                if byte >> 6 != 0b10:
                    return False
                need -= 1

        return need == 0
