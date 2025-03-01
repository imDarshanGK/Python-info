row1 = ['🤑', '🤑', '🤑']
row2 = ['🤑', '🤑', '🤑']
row3 = ['🤑', '🤑', '🤑']
selected_rows = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}\n')

position = input("Enter the position where you want to hide the money (row and column as two digits, e.g., 12 for row 1 column 2): ")

row_number = int(position[0])
column_number = int(position[1])

row_selected = selected_rows[row_number - 1]
row_selected[column_number - 1] = "X"

print(f'{row1}\n{row2}\n{row3}\n')
