import pandas as pd

excel_file = 'movies.xls'
movies = pd.read_excel(excel_file)

# print(movies.head())

movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)

print(movies_sheet1.head())
