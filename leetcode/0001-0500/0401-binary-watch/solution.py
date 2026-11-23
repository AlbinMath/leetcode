class Solution:
    def readBinaryWatch(self, turnedOn):
        result = []

        for hour in range(12):
            for minute in range(60):
                hour_bits = bin(hour).count('1')
                minute_bits = bin(minute).count('1')

                if hour_bits + minute_bits == turnedOn:
                    result.append(str(hour) + ":" + format(minute, "02d"))

        return result
