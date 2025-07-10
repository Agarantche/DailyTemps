class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result array with zeros.
        result = [0] * len(temperatures)

        # Stack to store indices of days.
        stack = []

        # Iterate through each temperature.
        for i in range(len(temperatures)):
            # While stack is not empty and current temp is warmer than temp at stack top.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Pop previous day's index.
                prevDay = stack.pop()
                # Calculate and store days difference.
                result[prevDay] = i - prevDay

            # Push current day's index onto stack.
            stack.append(i)

        # Return the result array.
        return result
