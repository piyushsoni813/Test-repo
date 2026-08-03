class Solution:
    def buildArray(self, numbers):
        answer = [0] * len(numbers)

        for i in range(len(numbers)):
            answer[i] = numbers[numbers[i]]

        return answer