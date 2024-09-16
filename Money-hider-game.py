row1 = ['🤑', '🤑', '🤑']
row2 = ['🤑', '🤑', '🤑']
row3 = ['🤑', '🤑', '🤑']
selected_rows = [row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}\n')
postion = input("Enter the postion where you want to hide the money: ")
row_numner = int(postion[0])
coulum_number = int(postion[1])
row_selected = selected_rows[row_numner-1]
row_selected[coulum_number-1] = "X"
print(f'{row1}\n{row2}\n{row3}\n')