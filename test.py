import csv
# data = [
# ('CJsI2kedTZ20HdEXsVNfuZyp0I8=',1),
# ('57URehwrSduh1Rtm0Sn2RZyp0I8=',1),
# ('T0MAK8XcRvGpxbTOHAShrJyp0I8=',1),
# ('pkkx4HR/Sa+OvBxJ50T3L5yp0I8=',1),
# ('W+JAyezaTsyWYuad29peG5yp0I8=',1),
# ('X1271/TeQSK5XOB0tURqv5yp0I8=',1),
# ('yHjzUjbeS/u1710KYy734Jyp0I8=',1),
# ('SYBvzH+tTGymahzWb5Irtpyp0I8=',1),
# ('ZFh5pk+dQdaAuFDewRdAd5yp0I8=',1),
# ('Dl5lHHp4QFOCGx/4AO1Dg5yp0I8=',1),
# ('9xZApUCKRD2p0cmLOmyd9Zyp0I8=',1),
# ('3ppM9KTnSNSke/Ij2opqt5yp0I8=',1),
# ('8YsEmH+PQcea2Mi6n9iJQZyp0I8=',1),
# ('LiVbh25sTUu8wwZlYWnk7pyp0I8=',1),
# ('FJ3zFa6vTG+4Zmc7YfV+Y5yp0I8=',1),
# ('QhOMEpH5Q3GNE6lw10xV0Jyp0I8=',1),
# ('YtvPHy0JSeyuNdtK8K91Hpyp0I8=',1),
# ('xCnxptezR1e21YMVVQkC8pyp0I8=',1),
# ('tX117MrhTWKdu4Wko6gW3Jyp0I8=',1),
# ('rzFu4esyTaKK6Nj4un5gmJyp0I8=',1),
# ('3lGeC5nRRk2VjzWuYd51TZyp0I8=',1),
# ('mlnc1p66TUa5MMYH3WTrz5yp0I8=',1),
# ('PdxrkiK+QkOA/pqgVHA2cZyp0I8=',1),
# ('tIdebZF4RViJ1RREly9lOpyp0I8=',1)
# ]
# f = open('222.csv','a+')
# writer = csv.writer(f)
# for i in data:
#     writer.writerow(i)
# f.close()
#
# # coding:utf-8
# import csv
# f = csv.reader(open('222.csv','r'))
# count = 0
# for i in f:
#     if i[1]=='1':
#         count=count+1
#         print('【'+count.__str__()+'】\t'+i[0])

# 初始化两个已修改与未修改list
# modifiedlist=[]
# unmodifiedlist=[]
#
# record = csv.reader(open('222.csv','r'))
# for item in record:
#     modifiedlist.append(item[0])
#
# print(modifiedlist)
# print(unmodifiedlist)
#
#
#
# print('HMN0f9ThQCaTEaBpPbVLgZyp0I8=' in modifiedlist)

# coding=utf-8

import xlrd,xlwt
from xlutils.copy import copy

rb = xlrd.open_workbook('/Users/jackietsoi/Documents/workDirectory/zhtb/Docs/xk/cp.xls')

# 通过sheet_by_index()获取的sheet没有write()方法
rs = rb.sheet_by_index(0)

wb = copy(rb)
# 利用xlutils.copy函数，将xlrd.Book转为xlwt.Workbook，再用xlwt模块进行存储


# 通过get_sheet()获取的sheet有write()方法
ws = wb.get_sheet(0)
ws.write(1, 16, 'changed!')

wb.save('/Users/jackietsoi/Documents/workDirectory/zhtb/Docs/xk/cp.xls')

print(rs.cell(1,16).value)
