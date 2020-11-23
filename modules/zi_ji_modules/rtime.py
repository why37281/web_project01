import time
def rhelp():
    re = open('/Users/Administrator/PycharmProjects/untitled/python3_modules/zi_ji_modules/rhelp/rtime.txt','r',encoding='UTF-8')
    rea = re.read()
    re.close()
    return rea
def rtime(list1):
    lian = time.strftime(list1, time.localtime())
    return lian
def jie():
    """
    :return: 返回时间截
    """
    return time.time()
def rrcanlendar():
    """
    :return: 返回 现在的详细时间
    """
    return time.asctime(time.localtime(time.time()))
def yun_nian(year):
    return time.isleap(year)
def ca(list1):
    list1[1] = str()
    le = '%s.%s.%s %s:%s:%s' % (list1[0], list1[1], list1[2], list1[3], list1[4], list1[5])
    return le