def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # The first element in each row is always 1

        if triangle:
            # If there are previous rows, calculate the current row based on the previous row
            prev_row = triangle[-1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])

            row.append(1)  # The last element in each row is always 1

        triangle.append(row)

    return triangle

# Example usage:
if __name__ == "__main__":
    result = pascal_triangle(5)
    for row in result:
        print(row)
