def mul_table(height: int, width: int) -> list[list[int]]:
    rows: list[list[int]] = []
    row_i: int = 1
    while row_i <= height:
        col_i: int = 1
        row: list[int] = []
        while col_i <= width:
            row.append(row_i * col_i)
            col_i += 1
        rows.append(row)
        row_i += 1

    return rows


print(mul_table(3, 2))
