#! python3
# blankRowInserter.py - Inserts M blabk rows before given N row.
# Use: python blankRowInserter.py 3 2 myexcel.xlsx

import openpyxl, sys

N = int(sys.argv[1])
M = int(sys.argv[2])
filename = sys.argv[3]

wb = openpyxl.load_workbook(filename)
ws = wb.active

for row in range(1, M + 1):
    print('Inserting ' + str(row) + 'a row.')
    ws.insert_rows(N, 1)

saveas = filename.split('.')[0] + '_blankrow.xlsx'
wb.save(saveas)
print('Saved as ' + saveas)
print('Done.')