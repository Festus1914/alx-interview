def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n  # Initialize a list to keep track of visited boxes
    visited[0] = True  # Mark the first box as visited

    stack = [0]  # Initialize a stack to perform DFS starting from box 0

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
