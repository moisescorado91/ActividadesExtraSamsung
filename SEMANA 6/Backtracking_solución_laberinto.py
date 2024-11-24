
# La matriz binaria N*N se da en un laberinto de la siguiente manera,
# y el ratón debe moverse desde la coordenada (0, 0) hasta la coordenada (N-1, N-1) dfs-laberinto-1.png
# maze = [
#   [0, 0, 0, 0],
#   [1, 0, 1, 0],
#   [1, 0, 1, 1],
#   [0, 0, 0, 0],
# ]
# 
# [(0,1), 1, 1, (1,2,3)] 
# solve (maze)



def solve_maze(maze):
    N = len(maze)
    path = []
    
    def is_safe(x, y):
        return 0 <= x < N and 0 <= y < N and maze[x][y] == 0
    
    def dfs(x, y):
        if (x, y) == (N-1, N-1):
            path.append((x, y))
            return True
        
        if is_safe(x, y):
            path.append((x, y))
            maze[x][y] = -1  
            
            if dfs(x, y + 1):
                return True

            if dfs(x + 1, y):
                return True

            if dfs(x, y - 1):
                return True

            if dfs(x - 1, y):
                return True
            
            path.pop()  
            
        return False
    
    if dfs(0, 0):
        return path
    else:
        return "Se encontro un obstaculo"

maze = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 0],
]

solucion = solve_maze(maze)
print(solucion)
