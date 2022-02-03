import pandas as pd
import xlwings as xw

PATH,password1 = r"C:\Users\User\Desktop\EXCEL\1338-01052021.xlsx","C06210"
wb = xw.Book(PATH,password1)
sheet = wb.sheets['1338-01052021']

df = sheet['A1:C4'].options(pd.DataFrame, index=False, header=True).value
print(df)