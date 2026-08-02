class Solution:
    def removeDuplicates(self, numbers):
        if not numbers:
            return 0

        write_index = 1

        for i in range(1, len(numbers)):
            if numbers[i] != numbers[i - 1]:
                numbers[write_index] = numbers[i]
                write_index += 1

        return write_index