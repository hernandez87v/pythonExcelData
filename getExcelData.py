import pandas as pd

spreadsheet_file = pd.ExcelFile(
    "/mnt/HDD/CODE/pythonExcelData/produceSales.xlsx")
worksheets = spreadsheet_file.sheet_names
appended_data = []

for sheet_name in worksheets:
    print(sheet_name)
