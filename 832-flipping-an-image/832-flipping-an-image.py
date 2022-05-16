class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        R , C = len(image) , len(image[0])
        for i in range(R):
            image[i].reverse()
        print(image)
        for i in range(R):
            for j in range(C):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image
        