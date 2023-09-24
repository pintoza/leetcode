"""Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        triangle = [[1]]

        for _ in range(rowIndex):

            new_row = [1]

            last_row = triangle[-1]

            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i + 1])

            new_row.append(1)
            triangle.append(new_row)

        return triangle[rowIndex]
