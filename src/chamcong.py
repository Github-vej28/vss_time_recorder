import datetime
import pandas as pd
import xlrd
from xlutils.copy import copy
import openpyxl
import os

from employee import Employee

file_input = 'input/cham_cong/20221118161927_37640_BAOCAO_TONG_HOP_CONG.xlsx'
file_output = 'output/20221018153519_39296_DanhsachImportChamcongCTV4.xls'
file_on_leave = 'input/nghi_phep/20221118162155_37640_BaoCao_TonghopdonxinnghiCBCNV.xlsx'

MONTH = 11

start = '11/01/2022'
end = '11/30/2022'

### (Optional) Find all weekend days 
def getWeekendDays(start, end):
    saturdays = pd.date_range(start = start, end = end, freq = 'W-SAT')
    sundays = pd.date_range(start = start, end = end, freq = 'W-SUN')
    return saturdays, sundays

saturdays, sundays = getWeekendDays(start, end)
sat = saturdays.day
sun = sundays.day
###

### Đọc file cham cong 
workbook_in = openpyxl.load_workbook(file_input)

sheet = workbook_in.active
max = sheet.max_row + 1

# With openyxl, cols and rows start with 1
employees = dict()

# for i in range(2, max):
for i in range(1, max):
    id = sheet.cell(row = i, column = 2).value
    # id = sheet.cell(row = i, column = 5).value
    if id not in employees:
        new_employee = Employee(id)
        employees[id] = new_employee
    
    date = sheet.cell(row = i, column = 3).value
    # date = sheet.cell(row = i, column = 6).value
    employee = employees[id]
    employee.createDate(date)

    timestamp = sheet.cell(row = i, column = 4).value
    # timestamp = sheet.cell(row = i, column = 7).value
    employee.Timekeeping[date.day].updateTime(timestamp)
###    

### Đọc file nghi phep
work_book_off = openpyxl.load_workbook(file_on_leave)
sheet_off = work_book_off.active
num_rows = sheet_off.max_row + 1

# Buffer_id được dùng khi có nhiều hàng chung 1 id nên id bị None => Dùng buffer_id để lấy id ban đầu
buffer_id = 0
for i in range(8, num_rows):
    # Kiểm tra tình trạng đơn
    state = sheet_off.cell(row = i, column = 8).value
    if (state != "Đã phê duyệt"):
        continue

    if (sheet_off.cell(row = i, column = 5).value != None) and ('chế độ con nhỏ' in sheet_off.cell(row = i, column = 5).value):
        continue

    id = sheet_off.cell(row = i, column = 2).value
    if id == None:
        employee = employees[buffer_id]
    else:
        id = int(id)
        if id not in employees:
            employee = Employee(id)
            employees[id] = employee
        else:
            employee = employees[id]

        if buffer_id != id:
            buffer_id = id

    dates = sheet_off.cell(row = i, column = 7).value
    dates_on_leave = dates.split(' - ')
    
    from_date_on_leave = datetime.datetime.strptime(dates_on_leave[0], "%d/%m/%Y %H:%M")
    end_date_on_leave = datetime.datetime.strptime(dates_on_leave[1], "%d/%m/%Y %H:%M")

    reason = sheet_off.cell(row = i, column = 6).value
    employee.getOnLeave(from_date_on_leave, end_date_on_leave, reason)
###

### Viết vào file output
workbook_out = xlrd.open_workbook(file_output, formatting_info=True)
r_sheet = workbook_out.sheet_by_name("Sheet1")

wb = copy(workbook_out)
w_sheet = wb.get_sheet(0)

# With xlrd, indexes of col and row start with 0
days = []
for col in range(3, r_sheet.ncols - 1):
    day = r_sheet.cell(1, col).value
    days.append(int(day))

for row in range(2, r_sheet.nrows - 2):
    id = r_sheet.cell(row, 1).value

    if id not in employees:
        continue
    employee = employees[id]

    dates = employee.Timekeeping
    for day in dates:
        date = employee.Timekeeping[day]
        if (day in sun) or (day in sat):
            continue
        if (date.salaryCoefficient() == 0):
            w_sheet.write(row, day + 2, "XX")
        if (date.salaryCoefficient() == 1):
            w_sheet.write(row, day + 2, "X:8")
        if (date.salaryCoefficient() == 2):
            w_sheet.write(row, day + 2, "X:4")

    # Viết kí hiệu vào file output
    dates_on_leave = employee.on_leave
    for date in dates_on_leave:
        month = date.month
        if (month != MONTH):
            continue
        day = date.day
        if (day in sun) or (day in sat):
            continue
        # w_sheet.write(row, day + 2, dates_on_leave[date])
        value = r_sheet.cell(row, day + 2).value
        if value == "":
            w_sheet.write(row, day + 2, dates_on_leave[date])
        else:
            value = value + ", " + dates_on_leave[date]
            w_sheet.write(row, day + 2, value)

wb.save(file_output + '.out' + os.path.splitext(file_output)[-1])
