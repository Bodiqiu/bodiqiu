from pandas import read_table
from xlrd import open_workbook

fname = r'wg.xls'
rname = r'dk.txt'
xname = r'dkkk.txt'
data = open_workbook(fname)
table = data.sheets()[0]
cols = table.col(0)

daka = read_table(rname, sep=',')

for i in daka:
    for col in cols:
        if str(col.value) not in str(daka[i].values):
            with open(xname, "a") as f:
                f.write(col.value)
                f.write("\r")
