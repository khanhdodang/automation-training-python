# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("SampleData.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print(sheet.cell_value(0, 0))

print("\nExtracting number of rows")
print(sheet.nrows)

print("\nExtracting number of columns")
print(sheet.ncols)

print("\nExtracting all columns name")
for i in range(sheet.ncols):
  print(sheet.cell_value(0, i))

print("\nExtract first column")
for i in range(sheet.nrows):
  print(sheet.cell_value(i, 0))

print("\nExtract first column")
print(sheet.row_values(1))
