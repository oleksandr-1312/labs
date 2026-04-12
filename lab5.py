def flood_fill(matrix, start_row, start_col, new_color):
    if not matrix:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])

    if not (0 <= start_row < rows and 0 <= start_col < cols):
        return matrix

    target_color = matrix[start_row][start_col]

    if target_color == new_color:
        return matrix

    queue = [(start_row, start_col)]

    while queue:
        r, c = queue.pop(0)

        if matrix[r][c] == target_color:
            matrix[r][c] = new_color

            if r > 0: 
                queue.append((r - 1, c))
            if r < rows - 1: 
                queue.append((r + 1, c))
            if c > 0: 
                queue.append((r, c - 1))
            if c < cols - 1: 
                queue.append((r, c + 1))

    return matrix