from date import Date
import datetime

class Employee:
    def __init__(self, id):
        self.id = id
        self.Timekeeping = dict()
        self.on_leave = dict()
        self.signs = {  
            "CN": "Công tác nước ngoài",
            "CT": "Công tác trong nước",
            "C" : "Đi làm theo chế độ con nhỏ",
            "Cô": "Con ốm",
            "DS": "Nghỉ dưỡng sức sau sinh, nghỉ dưỡng sức sau ốm",
            "H" : "Đi học hưởng lương bảo hiểm",
            "KT": "Nghỉ khám thai, nghỉ sảy thai, nghỉ tránh thai",
            "L" : "Nghỉ lễ, nghỉ tết",
            "NB": "Nghỉ bù lễ, nghỉ bù tết",
            "P" : "Nghỉ phép",
            "Ro": "Nghỉ việc riêng không hưởng lương",
            "Rv": "Nghỉ việc riêng có hưởng lương",
            "TN": "Tai nạn",
            "TS": "Nghỉ thai sản",
            "VS": "Nghỉ vợ sinh",
            "Ô" : "Bản thân ốm, nghỉ ốm dài ngày",
            "Đc": "Nghỉ chờ hưu",
            "DL": "Nghỉ dưỡng hàng năm, du lịch",
            "CH": "Trực chỉ huy ngày nghỉ hàng tuần, ngày lễ, ngày tết",
            "CHT": "Trực chỉ huy ngày",
            "TL": "Trực ban ngày nghỉ hàng tuần, ngày lễ, tết",
            "TT": "Trực ban ngày thường",
            "TĐL": "Trực đêm ngày nghỉ hàng tuần, ngày lễ, tết",
            "TĐT": "Trực dêm ngày thường",
            "GL": "Công làm thêm ngày lễ, tết",
            "GN": "Công làm thêm ngày nghỉ hàng tuần",
            "GT": "Công làm thêm ngày thường"
        }

    def createDate(self, timekeeping_date):
        day = timekeeping_date.day
        if day in self.Timekeeping:
            return
        date = Date(day)
        self.Timekeeping[day] = date

    # Kiểm tra xem là nghỉ nửa ngày hay cả ngày
    def checkOnLeaveType(self, from_date_on_leave, end_date_on_leave):
        start_day_off = from_date_on_leave.date()
        to_day_off = end_date_on_leave.date()
        start_time_off = from_date_on_leave.time()
        end_time_off = end_date_on_leave.time()

        if (start_day_off == to_day_off):
            if (end_time_off == datetime.datetime.strptime("12:00:00", "%H:%M:%S").time()):
                self.on_leave[to_day_off] = "P:4"
            elif (start_time_off == datetime.datetime.strptime("13:30:00", "%H:%M:%S").time()):
                self.on_leave[start_day_off] = "P:4"
            else: 
                self.on_leave[to_day_off] = "P:8"
        else:
            if (start_time_off == datetime.datetime.strptime("08:00:00", "%H:%M:%S").time()):
                self.on_leave[start_day_off] = "P:8"
            else: 
                self.on_leave[start_day_off] = "P:4"
            if (end_time_off == datetime.datetime.strptime("12:00:00", "%H:%M:%S").time()):
                self.on_leave[to_day_off] = "P:4"
            else: 
                self.on_leave[to_day_off] = "P:8"
        
        start_day_off += datetime.timedelta(days=1)
        while (start_day_off < to_day_off):
            self.on_leave[start_day_off] = "P:8"
            start_day_off += datetime.timedelta(days=1)
        return

    # Lày loại ngày nghỉ
    def getOnLeave(self, date, reason):  
        day = date.date()
        if day in self.on_leave:
            return
        for sign in self.signs:
            if (reason.lower() in self.signs[sign].lower()):
                if sign == "P":
                    return sign
                else:
                    self.on_leave[day] = sign
        
    def updateOffDays(self, date):
        if date not in self.off_days:
            self.off_days.append(date)