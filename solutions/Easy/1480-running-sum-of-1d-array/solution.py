class Solution:
    def runningSum(self, numbers):
        for i in range(1, len(numbers)):
            numbers[i] += numbers[i - 1]

        return numbers