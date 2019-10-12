import csv
with open ('assrst.csv','a',newline = '') as csvfile:
    writer = csv.writer(csvfile,dialect='exccel')
    header = ['小区','地址','建筑年份','楼栋','单元','户室','朝向','面积']
    writer.writerrow
    title = input('')