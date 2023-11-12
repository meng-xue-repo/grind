############ Check visited: Option 1 ############
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = set() # "{}" means dict, NOT set

        # Have to fix the original color at that position!
        originalColor = image[sr][sc]

        def inBoundary(row, col):
            return row >= 0 and row < len(image) and col >= 0 and col < len(image[row])

        def traversal(row, col):
            if not inBoundary(row, col):
                return

            if (row, col) in visited:
                return

            if image[row][col] != originalColor:
                return

            image[row][col] = color
            visited.add((row, col)) # NOT append()

            traversal(row - 1, col)
            traversal(row + 1, col)
            traversal(row, col - 1)
            traversal(row, col + 1)

        traversal(sr, sc)

        return image      

############ Check visited: Option 2 ############
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # Have to fix the original color at that position!
        originalColor = image[sr][sc]

        def inBoundary(row, col):
            return row >= 0 and row < len(image) and col >= 0 and col < len(image[row])

        def traversal(row, col):
            if not inBoundary(row, col):
                return

            # Already visited
            if image[row][col] == color:
                return

            if image[row][col] != originalColor:
                return

            image[row][col] = color

            traversal(row - 1, col)
            traversal(row + 1, col)
            traversal(row, col - 1)
            traversal(row, col + 1)

        traversal(sr, sc)

        return image  
