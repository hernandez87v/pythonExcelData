import pandas as pd

spreadsheet_file = pd.ExcelFile(
    "/mnt/HDD/CODE/pythonExcelData/produceSales.xlsx")
worksheets = spreadsheet_file.sheet_names
appended_data = []

for sheet_name in worksheets:
    produce = "PRODUCE"
    df = pd.read_excel(spreadsheet_file, sheet_name, header=0)
    df = df[[produce, "POUNDS SOLD"]].where(df["POUNDS SOLD"] > 39.5).dropna()
    # df = df.dropna()
    print(df)
