from collections import deque

def shortest_path_maze(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    if not (0 <= start[0] < rows and 0 <= start[1] < cols and matrix[start[0]][start[1]] == 1):
        return -1
        
    queue = deque([(start[0], start[1], 0)])
    
    visited = set()
    visited.add((start[0], start[1]))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y, dist = queue.popleft()
        
        if (x, y) == end:
            return dist
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
                
    return -1