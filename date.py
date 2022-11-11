from datetime import datetime

class Date:
    def __init__(self, day):
        self.day = day
        self.time_in = None
        self.time_out = None

    def updateTime_in(self, timestamp):
        self.time_in = timestamp
    
    def updateTime_out(self, timestamp):
        if (self.time_out == None or self.time_out < timestamp):
            self.time_out = timestamp

    def updateTime(self, timestamp):
        if (self.time_in == None):
            self.updateTime_in(timestamp)
        else:
            if (self.time_in > timestamp):
                self.updateTime_out(self.time_in)
                self.updateTime_in(timestamp)
            else: 
                self.updateTime_out(timestamp)

    def salaryCoefficient(self):
        start_time = datetime.strptime("08:30:00", "%H:%M:%S").time()
        end_morning_time = datetime.strptime("12:00:00", "%H:%M:%S").time()
        start_afternoon_time = datetime.strptime("13:30:00", "%H:%M:%S").time()
        end_time = datetime.strptime("17:00:00", "%H:%M:%S").time()
        if (self.time_in == None or self.time_out == None):
            return 0
        if (self.time_in.time() <= start_time and self.time_out.time() >= end_time):
            return 1
        if (self.time_in.time() <= start_time and self.time_out.time() >= end_morning_time):
            return 2
        if (self.time_in.time() <= start_afternoon_time and self.time_out.time() >= end_time):
            return 2
        return 0