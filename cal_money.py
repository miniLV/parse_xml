"""四舍六入算法 - demo"""

'''四舍六入5考虑 - 保留2位小数'''
money1 = 1.1650 #10.16
money2 = 1.1651 #10.17
money3 = 0.1350 #10.14
money4 = 0.825
# from math import *

from decimal import *

'''round - 4舍6如，5不看均舍去'''

def cal_money(money):

    # 整数部分取值正确的话，先乘以100 
    start_money = money * 100

    # 取整数
    get1 = round(start_money)

    #再 / 100 取 2位小数 - 
    end_money = get1 / 100
    a = '%.2f'%(end_money)#只有这样获取精度，才不会再次进行四舍五入！
    print(a)

cal_money(money1)
cal_money(money2)
cal_money(money3)
cal_money(money4)

print('-------------------------\n')

cal_money(1.1550) #进1 ，0.16
cal_money(0.1550) #不进，1.16
cal_money(2.2550)
cal_money(0.1750)
cal_money(0.1850)
