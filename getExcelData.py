import pandas as pd

spreadsheet_file = pd.ExcelFile(
    "/mnt/HDD/CODE/pythonExcelData/produceSales.xlsx")
worksheets = spreadsheet_file.sheet_names
appended_data = []

for sheet_name in worksheets:
    produce = "PRODUCE"
    df = pd.read_excel(spreadsheet_file, sheet_name, header=0)
    df = df[[produce, "POUNDS SOLD"]].where(df["POUNDS SOLD"] > 39.5).dropna()
    df["Product ID"] = sheet_name
    df = df[["Product ID", "POUNDS SOLD", produce]]
    appended_data.append(df)

appended_data = pd.concat(appended_data)
appended_data.to_excel(
    "/mnt/HDD/CODE/pythonExcelData/output.xlsx")
