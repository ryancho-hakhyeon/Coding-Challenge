# A binary watch has 4 LEDs on the top to represent the hours (0-11),
# and 6 LEDs on the bottom to represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.
# For example, the below binary watch reads "4:51".
# Given an integer turnedOn which represents the number of LEDs
# that are currently on (ignoring the PM),
# return all possible times the watch could represent.
# You may return the answer in any order.
#
# The hour must not contain a leading zero.
#
# For example, "01:00" is not valid. It should be "1:00".
# The minute must be consist of two digits and may contain a leading zero.
#
# For example, "10:2" is not valid. It should be "10:02".

from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        numBin = [bin(i).count("1") for i in range(60)]

        for hour in range(12):
            hourBin = numBin[hour]
            for minute in range(60):
                minBin = numBin[minute]

                if hourBin + minBin == turnedOn:
                    res.append(f"{hour}:{minute:02d}")
        return res


obj = Solution()

turnedOn = 1
print(obj.readBinaryWatch(turnedOn))
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

turnedOn = 9
print(obj.readBinaryWatch(turnedOn))
# Output: []
