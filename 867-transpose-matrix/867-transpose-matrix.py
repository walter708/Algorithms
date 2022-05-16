class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for j in range(len(matrix[0])):
            res = []
            for i in range(len(matrix)):
                res.append(matrix[i][j])
            result.append(res)
        return result
        