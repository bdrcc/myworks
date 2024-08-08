#!/usr/bin/env python

# !_index.htmlの情報を受け取り、仮想サーバー上で使用することを想定
# 自分の生年月から主な学校の入学年度・卒業年度を計算するアプリ
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')
import cgi
import cgitb
cgitb.enable()
import datetime

html_body='''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>result/年計算アプリ</title>
</head>
<body>
    <p>{}{}年 (西暦{}年) {}月 生まれのあなたは</p>
    <p>小学校入学 : {}年 (西暦{}年) 4月</p>
    <p>小学校卒業 : {}年 (西暦{}年) 3月</p>
    <p>中学校入学 : {}年 (西暦{}年) 4月</p>
    <p>中学校卒業 : {}年 (西暦{}年) 3月</p>
    <p>高校入学 : {}年 (西暦{}年) 4月</p>
    <p>高校卒業 : {}年 (西暦{}年) 3月</p>
    <p>大学入学 : {}年 (西暦{}年) 4月</p>
    <p>大学卒業 : {}年 (西暦{}年) 3月</p>
    </body>
</html>
'''

param_data = cgi.FieldStorage()
ge = param_data.getvalue('val')
year = 0

y_bir = param_data.getvalue('num_y')
month = int(param_data.getvalue('num_m'))

if ge == 'm':
    if y_bir == '1' or y_bir =='元':
        y_bir = '元'
        year = 1868
    else:
        year = int(y_bir) + 1868 - 1
    gen = '明治'
elif ge == 't':
    if y_bir == '1' or y_bir =='元':
        y_bir = '元'
        year = 1912
    else:
        year = int(y_bir) + 1912 - 1
    gen = '大正'
elif ge == 's':
    if y_bir == '1' or y_bir =='元':
        y_bir = '元'
        year = 1926
    else:
        year = int(y_bir) + 1926 - 1
    gen = '昭和'
elif ge == 'h':
    if y_bir == '1' or y_bir =='元':
        y_bir = '元'
        year = 1989
    else:
        year = int(y_bir) + 1989 - 1
    gen = '平成'
elif ge == 'r':
    if y_bir == '1' or y_bir =='元':
        y_bir = '元'
        year = 2019
    else:
        year = int(y_bir) + 2019 - 1
    gen = '令和'
else:
    year = int(y_bir) 
    if year >= 2019:
        gen = '令和'
        if year == 2019:
            y_bir = '元'
        else:
            y_bir = str(year - 2019 + 1)
    elif year >= 1989:
        gen = '平成'
        if year == 1989:
            y_bir = '元'
        else:
            y_bir = str(year - 1989 + 1)
    elif year >= 1926:
        gen = '昭和'
        if year == 1926:
            y_bir = '元'
        else:
            y_bir = str(year - 1926 + 1)
    elif year >= 1912:
        gen = '大正'
        if year == 1912:
            y_bir = '元'
        else:
            y_bir = str(year - 1912 + 1)
    elif year >= 1868:
        gen = '明治'
        if year == 1868:
            y_bir = '元'
        else:
            y_bir = str(year - 1868 + 1)

if month >= 4:
    y_ele = year + 7
    y_jh = year + 13
    y_h = year + 16
    y_c = year + 19
    y_end = year + 23
else:
    y_ele = year + 6
    y_jh = year + 12
    y_h = year + 15
    y_c = year + 18
    y_end = year + 22

y_l = [y_ele,y_jh,y_h,y_c,y_end]
y = ['','','','','']

for i in range(5):
    if y_l[i] >=2019:
        if y_l[i] == 2019:
            y[i] = '令和元'
        else:
            dif = y_l[i] - 2019 + 1
            y[i] = '令和' + str(dif)
    elif y_l[i] >= 1989:
        if y_l[i] == 1989:
            y[i] = '平成元'
        else:
            dif = y_l[i] - 1989 + 1
            y[i] = '平成' + str(dif)
    elif y_l[i] >= 1926:
        if y_l[i] == 1926:
            y[i] = '昭和元'
        else:
            dif = y_l[i] - 1926 + 1
            y[i] = '昭和' + str(dif)
    elif y_l[i] >= 1912:
        if y_l[i] == 1912:
            y[i] = '大正元'
        else:
            dif = y_l[i] - 1912 + 1
            y[i] = '大正' + str(dif)
    elif y_l[i] >= 1868:
        if y_l[i] == 1868:
            y[i] = '明治元'
        else:
            dif = y_l[i] - 1868 + 1
            y[i] = '明治' + str(dif)

print('Content-type: text/html')
print('')
print(html_body.format(gen, y_bir, year, month, y[0], y_ele, y[1], y_jh, y[1], y_jh, y[2], y_h, y[2], y_h, y[3], y_c, y[3], y_c, y[4], y_end))
