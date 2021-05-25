#! python3
# multiplicationTable.py - creates an Excel workbook of a number(N) multiplacated N times(N*N).

import openpyxl, sys
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb.active
bold = Font(bold=True)

number = int(sys.argv[1])

for column in range(1, number + 2):
    column_num = column
    column = openpyxl.utils.get_column_letter(column_num)
    for row in range(1, number + 2):
        # (A, B, C, D...)1
        if row == 1:
            if column == 'A':
                sheet[column + str(row)] = ' '
                continue
            else:
                sheet[column + str(row)].font = bold
                sheet[column + str(row)] = (column_num - 1)
                continue
        
        # A(1, 2, 3...)
        if column == 'A':
            sheet[column + str(row)].font = bold
            sheet[column + str(row)] = (row - 1)
            continue

        # Any other column
        sheet[column + str(row)] = (row - 1) * (column_num - 1)

wb.save('myworkbook.xlsx')