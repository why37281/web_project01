"""
在 calendar 模块中的以学功能
"""
import calendar
def mouth_calendar(year,mouth):
    """
    功能：生成月历表
    :param year: 年
    :param mouth: 月
    :return: 返回生成的月历表
    """
    return calendar.month(year,mouth)
def year_canlendar(year):
    """
    功能：生成月历表
    :param year: 年
    :return: 返回生成的年历表
    """
    return calendar.calendar(year)
