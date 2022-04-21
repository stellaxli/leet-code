class Solution:
    def nearestExit(maze, entrance):
        rows, cols = len(maze), len(maze[0])
        start = tuple(entrance)

        visited = set([start])
        print(visited)
        queue = [start]
        count = 0
        # print(queue)
        while queue:
            for i in range(len(queue)):
                currRow, currCol = queue.pop(0)
                # print(currRow)
                if ([currRow,currCol] != entrance and (currCol == 0 or currCol == cols-1 or currRow == 0 or currRow == rows-1)):
                    return count

                for dr,dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    newRow, newCol = currRow + dr, currCol + dc

                    if (0<=newRow<rows and 0<=newCol<cols and maze[newRow][newCol] == '.' and (newRow,newCol) not in visited):
                        queue.append((newRow,newCol))
                        visited.add((newRow,newCol))
            count += 1

        return -1


maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]

maze1 = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance1 = [1,0]

maze2 = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".",".",".","+"],["+","+","+","+",".","+","."]]
entrance2 = [0,1]


print(Solution.nearestExit(maze2, entrance2))
