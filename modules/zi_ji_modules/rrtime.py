import calendar
import time
def mouth_calendar(year, mouth):
    return calendar.month(year, mouth)
def year_canlendar(year):
    return calendar.calendar(year)
def rhelp():
    re = open('/Users/Administrator/PycharmProjects/untitled/python3_modules/zi_ji_modules/rhelp/rtime.txt', 'r', encoding='UTF-8')
    rea = re.read()
    re.close()
    return rea
def rtime(str1):
    lian = time.strftime(str1, time.localtime())
    return lian
def jie():
    return time.time()
def rrcanlendar():
    return time.asctime(time.localtime(time.time()))