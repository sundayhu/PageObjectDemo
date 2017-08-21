import sys
import xlrd,time
from selenium import webdriver
import login,record,setup
import test_record
def read_excel(file_path,index):
    data=xlrd.open_workbook(file_path)
    table=data.sheets()[index]
    return table
table=read_excel("er.xlsx",0)
nrows=table.nrows
ncols=table.ncols
#print(nrows)
#print(ncols)
counts=0;
#按行读
i=1
for rownum in range(nrows):
    print('\n####### Start Test Case '+str(i)+' #######')
    # 获取行数据，为列表形式
    list = table.row_values(rownum)
    #　动态导入模块
    #__import__('cases.' + list[0])
    print(__import__(list[0]))
    # 根据字符串确定要使用的模块
    module = sys.modules[list[0]]
    print(module)
    # 根据list[0]这个字符串获取到类
    c = getattr(module, list[0])
    # 实例化该对象
    obj = c()
    # 根据list[1]这个字符串获取到方法
    mtd = getattr(obj,list[1])
    # 将list[2]，即excel中的prams单元格按回车转换为列表
    params = list[2].split('\n')
    # 驱动方法执行，传入测试参数和预期结果
    n=mtd(params,list[3])
    counts+=n;
    print('####### End Test Case '+str(i)+' #######\n')
    i += 1
print("总的用例数：",nrows)
print("未通过的用例数：",counts)
print("用例通过率：",(nrows-counts)/nrows)
