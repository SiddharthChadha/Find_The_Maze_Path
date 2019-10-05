'''
8.2 Robot in a Grid

Imagine a robot sitting on the upper left corner of grid with r is and c columns. 
The robot can only move in to directions, right and down, but certain cells are "off limits" such that the robot cannot
step on them. Design and algorithm to find a path for the robit from the top left to bottom right

Approach:

    - Robot can either move down or right.
    - Consider each square in a grid as a Node in a graph
    - From each Node, check if there's a path to down or right, if there is store coodinates of that node
    - Checking if a path exists to down or to the right would be recrursive call as for checking if there is a path existing from 1 to 9,
    you check if there is a path existing from 4 to 9 or 2 to 9 and so on. 
    - Base case would be the case where our algorithm is checking if a path exists from 9 to 9. This returns TRUE
    - Time Complexity: Worst case(2^(r+c)), Space Complexity: O(r+c)

Memoisation:
    - Save failed paths in hashset
    - No need to compute them again
    - Time Complexity: O(rc)
    
Example: 
    1   2   3   
    4   5   6
    7   8   9
    Output: 9, 8, 7, 4, 1
    0 means path is blocked
'''

def find_path(maze, row, col, path, failed_path): #Finds path from row, col to the end
    
    if(row > len(maze) - 1 or col > len(maze[0]) - 1 or not maze[row][col]): #Our of bounds or path blocked
        return False

    pt = (row, col)
    if(pt in failed_path):
        return False
    is_destination = True if (row == len(maze) - 1 and col == len(maze[0]) - 1) else False

    if(is_destination or find_path(maze, row+1, col, path, failed_path) or find_path(maze, row, col+1, path, failed_path)):
        path.append([row, col])
        return True

    failed_path.add(pt)
    return False
    
def get_path(maze):
    if(len(maze) == 0 or len(maze[0]) == 0):
        return None
    path = []
    failed_path = set()

    if(find_path(maze, 0, 0, path, failed_path)):
        
        return [path, failed_path]
    return [None, None]

'''

'''

maze = [[1,2,3], [4,5,6], [7,8,9]]
output_path, failed_path = get_path(maze) #1, 4, 7, 8, 9

print("Path from Top left to Bottom right")
print(output_path)
print("Blocked points")
print(failed_path) 

maze = [[1,2,3], [0,5,6], [7,8,9]] 
print("----------")

output_path, failed_path = get_path(maze) #1, 2, 5, 8, 9
print("Path from Top left to Bottom right")
print(output_path)
print("Blocked points")
print(failed_path) 

maze = [[1,2,3], [0,5,6], [7,0,9]]
print("----------")
output_path, failed_path = get_path(maze) #1, 2, 5, 6, 9
print("Path from Top left to Bottom right")
print(output_path)
print("Blocked points")
print(failed_path) 

maze = [[1,2,3,4], [5,6,0,8], [0,0,11,12], [13,14,15,16]]
print("----------")
output_path, failed_path = get_path(maze) #1, 5, 6, 2, 3, 4, 8, 12, 16
print("Path from Top left to Bottom right")
print(output_path)
print("Blocked points")
print(failed_path) #5,6 are blocked





