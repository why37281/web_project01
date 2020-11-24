import rMongoDB
import time
import os
client = rMongoDB.rclient()
table1 = rMongoDB.ropen(client, ['db_user', 'user_table'])
table2 = rMongoDB.ropen(client, ['db_pm', 'pm'])
table3 = rMongoDB.ropen(client, ['db_lhnp', 'lhnp'])
table4 = rMongoDB.ropen(client, ['db_ping', 'ping'])
os.chdir("./")
def time_tool():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
def form0(p,m,table):
    find = rMongoDB.rfind({'p': p, 'm': m}, table)
    if find == []:
        return True
    else:
        return False
def form1(p, m, w_or_r_or_a: str):
    if w_or_r_or_a == 'w':
        if form0(p, m, table1):
            rMongoDB.rinsert([{'p': p, 'm': m}], table1)
        return True
    elif w_or_r_or_a == 'r':
        if len(rMongoDB.rfind({'p': p, 'm': m}, table1)) == 1:
            return True
        else:
            return False
def form2(name, age, gender, tel):
    rMongoDB.rinsert({name, age, gender, tel}, table1)
def form3():
    find = rMongoDB.rfind({}, table1)
    return find
#def notepad_lhnp():
def ping():
    return rMongoDB.rfind(table=table4)
def ping1(value):
    rMongoDB.rinsert([value], table4)