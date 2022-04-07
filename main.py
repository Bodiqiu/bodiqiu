from xlrd import open_workbook

fname = r'wg.xls'
rname = r'dk.txt'
xname = r'dkkk.txt'
data = open_workbook(fname)
table = data.sheets()[0]
cols = table.col(0)


with open(rname, encoding='UTF-8') as f:
    data = f.read()  # 读取文件
    for col in cols:
        if str(col.value) not in data:
            with open(xname, "a") as j:
                j.write(col.value)
                j.write("\r")

