"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = [[1]]

        for _ in range(numRows - 1):

            # new row will start with a 1 (all of them do)
            new_row = [1]

            # this selects the most recent "row" in result (because result is an array of arrays)
            last_row = result[-1]

            # this creates elements in the new row so that the total is one more than the previous
            # the new elements (the middle ones between the 1's) are the sum of the two above it
            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i + 1])

            # new row will end with a 1 (all of them do)
            new_row.append(1)
            result.append(new_row)

        return result[:numRows]
