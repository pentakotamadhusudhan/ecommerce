# import xlrd
# # def bmiweight(Height, Weight):
# #     Height = (Height)*12
# #     Weight = (Weight)*2.20462
# #     BMI = ((Weight / (Height) ** 2))*703
# #     BMI1 = round(BMI,2)
# #     return BMI1
# # Give the location of the file
# loc = ("/home/vfy1/Downloads/Percentiles/boys/boys_p_0_2.xls")
# # d=bmiweight(5.7,40)
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
# sheet.cell_value(0, 0)
# bmi = 12.8
# age = 18
# row_data = int()
# col_data = int()
#
#
# for i in range(sheet.ncols):
#     for j in range(sheet.nrows):
#
#         if sheet.cell_value(j, i) == bmi:
#             row_data = i
#             print(i)
#         elif sheet.cell_value(j, i) == age:
#             col_data = i
# print(sheet.cell_value(col_data, row_data))

import xlrd

# Give the location of the file
loc = ("/home/vfy1/Downloads/Percentiles/boys/boys_p_0_2.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
bmi = 16.3335

age = 15
row_data = int()
col_data = int()

# Extracting number of rows
# print(sheet.nrows)
for i in range(sheet.ncols):
    for j in range(sheet.nrows):
        # print(sheet.cell(18, 4))
        if sheet.cell_value(j, i) == bmi:
            row_data = i
            print(row_data)

        elif sheet.cell_value(j, i) == age:
            col_data = i
print(sheet.cell_value(col_data, row_data))















