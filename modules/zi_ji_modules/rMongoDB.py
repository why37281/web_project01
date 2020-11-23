import pymongo
def rclient(port = 27017):
    client = pymongo.MongoClient('mongodb://localhost:' + str(port))
    return client
def ropen(client = None, lname = None):
    if client == None:
        raise FileNotFoundError('ropen —— Client is Not Found.')
    if lname == None:
        raise FileNotFoundError('ropen —— DBName is Not Found.')
    name = client[lname[0]][lname[1]]
    return name
def rfind(condition = {}, table = None):
    if table == None:
        raise FileNotFoundError('rfind —— Table is Not Found.')
    find_res = table.find(condition)
    res_for = []
    for i in find_res:
        res_for.append(i)
    return res_for
def rinsert(insert_list, table = None):
    if table == None:
        raise FileNotFoundError('rinsert —— Table is Not Found.')
    if insert_list != []:
        for i in insert_list:
            table.insert_one(i)
def rdelete(condition = {}, table = None):
    if table == None:
        raise FileNotFoundError('rdelete —— Table is Not Found.')
    table.delete_many(condition)
def rupdata(updata_list, condition = {}, table = None):
    if table == None:
        raise FileNotFoundError('rupdata —— Table is Not Found.')
    if updata_list != []:
        for i in updata_list:
            table.updata_many(condition, i)
def rdrap(table = None):
    if table == None:
        raise FileNotFoundError('rdrap —— Table is Not Found.')
    return table.drap()