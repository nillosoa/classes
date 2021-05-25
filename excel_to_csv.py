#! python3
# Converts an excel file to the csv(Comma Separated Value) format.
# Use: python excel_to_csv.py [my_excel_file.xlsx]

import os, csv, sys, openpyxl

excelFile = sys.argv[1]
no_ext_filename   = excelFile[:len(excelFile)-5]
if not os.path.isfile(excelFile):
    print('I need a valid file in the cwd to work with;')
    sys.exit()

excelObj = openpyxl.load_workbook(excelFile)
writenFiles = []
#csvObj  = None # Just a reference

for sheetName in excelObj.get_sheet_names():
    sheet = excelObj.get_sheet_by_name(sheetName)
    csvFilename = no_ext_filename + '_' + sheetName + '.csv'
    csvFobj = open(csvFilename, 'w')
    csvWriter = csv.writer(csvFobj, lineterminator='\n')
    writenFiles.append(csvFilename)
    print('Working with ' + sheetName + '...')
    for rowNum in range(1, sheet.max_row + 1):
        rowData = []
        for colNum in range(1, sheet.max_column + 1):
            letter = openpyxl.utils.get_column_letter(rowNum)
            rowData.append(sheet[letter + str(colNum)].value)
        if any(rowData):
            csvWriter.writerow(rowData)

    csvFobj.close()

print('Done with ' + excelFile + '.')
print('Files writen:', ', '.join(writenFiles) + '.')