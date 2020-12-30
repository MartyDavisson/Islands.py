# Astranis GNC Internship Coding Question:
# Martin Davisson

# Problem Statement:
# Write a function, in the programming language of your choice, 
# which finds contiguous regions (or "islands") in a matrix 
# where all values in the island are greater than a threshold 
# (but not necessarily the same). The function should take a threshold,
# a minimum island size, and an arbitrarily sized matrix as inputs. 
# The function should output a matrix (same size as the input matrix) of booleans.
# Do not wrap around matrix edges. Corner neighbors are not sufficient for island continuity. 
# For example, if the the inputs are: threshold = 5, min island size = 3,
# and matrix = [4, 4, 4, 2, 2; 4, 2, 2, 2, 2; 2, 2, 8, 7, 2; 2, 8, 8, 8, 2; 8, 2, 2, 2, 8].
# Then the output would be [0, 0, 0, 0, 0; 0, 0, 0, 0, 0; 0, 0, 1, 1, 0; 0, 1, 1, 1, 0; 0, 0, 0, 0, 0].

# Language Used: Python3

# Algorithm Description:
# This algorithm uses the DFS (Depth First Search) algorithm to identify
# the number of islands in a grid as well as the size and "Altitude" of each
class Map:

    def __init__(self, row, col, m):
        self.R = row
        self.C = col
        self.map = m

    # A function to check if a given cell
    # (row, col) can be included in DFS
    def Incl(self, i, j, visited):
        # returns true if:
        # row number is in range, column number
        # is in range, graph value is 1
        # and not has not yet been visited
        return (i >= 0 and i < self.R and
                j >= 0 and j < self.C and
                not visited[i][j] and self.map[i][j])

    # A utility function to do DFS for a 2D
    # boolean matrix. It only considers
    # the 4 neighbours as adjacent vertices

    def DFS(self, i, j, visited):

        # These arrays are used to get row and
        # column numbers of 4 neighbours
        # of a given cell
        N_i = [-1, 0, 0, 1]
        N_j = [0, -1, 1, 0]

        # Mark this cell as visited
        visited[i][j] = True

        # Recur for all connected neighbours
        for k in range(4):
            if self.Incl(i + N_i[k], j + N_j[k], visited):
                self.DFS(i + N_i[k], j + N_j[k], visited)

    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def Islands(self, thresh, minsize):
        # First check to see if each point
        # meets a minimum value threshhold
        for i in range(self.R):
            for j in range(self.C):
                if graph[i][j] >= thresh:
                    graph[i][j] = 1
                else:
                    graph[i][j] = 0

        # An array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.C)]for i in range(self.R)]

        # Initialize count as 0 and begin searching
        count = 0
        islandcount = []
        islandsizes = []
        SOL = [[0] * row for _ in range(self.C)]
        for i in range(self.R):
            for j in range(self.C):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.map[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(i, j, visited)
                    count += 1
                    # Determine Island size
                    islandsize = 0
                    for i in range(self.R):
                        for j in range(self.C):
                            if visited[i][j] == True:
                                islandsize += 1
                    islandcount.append(count)
					# Adjust Island Size for each contiguous island
                    islandsize = islandsize-sum(islandsizes)
                    islandsizes.append(islandsize)

                    # Assign Island Sizes and apply min island threshold to each
                    for i in range(self.R):
                        for j in range(self.C):
                            if visited[i][j] == True and SOL[i][j] == 0 and islandsize >= minsize:
                                SOL[i][j] = 1

        return SOL


# Sample Problem Given in Problem Statement
graph = [[4, 4, 4, 2, 2],
         [4, 2, 2, 2, 2],
         [2, 2, 8, 7, 2],
         [2, 8, 8, 8, 2],
         [8, 2, 2, 2, 8]]


row = len(graph)
col = len(graph[0])

m = Map(row, col, graph)


print("Island Search Return:")
print(m.Islands(5, 1))


# Sources Used:
#     Title: Find the number of islands | Set 1 (Using DFS)
#     Author: Neelam Yadav 
#     Availability: https://www.geeksforgeeks.org/find-number-of-islands/

