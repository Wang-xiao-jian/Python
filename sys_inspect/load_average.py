#!/usr/bin/python

import csv
import time
import os

import psutil
import pyecharts
from pyecharts import options as opts
from pyecharts.charts import Bar

today = time.strftime('%F', time.localtime(time.time()))
filename = today + '_la.csv'

head = ['time', 'load_1', 'load_5', 'load_15']

def get_load_average():
    now = time.strftime('%T', time.localtime(time.time()))
    res = psutil.getloadavg()
    ret = [now] + list(res)
    return ret

def input_csv(data):
    if os.path.exists(filename):
        with open(filename, 'a+', newline='') as f:
            w = csv.writer(f, dialect='excel')
            w.writerow(data)
    else:
        with open(filename, 'a+', newline='') as f:
            w = csv.writer(f, dialect='excel')
            w.writerow(head)
            w.writerow(data)

def generate_html():
    xlist = []
    ylist = []

    with open(filename, 'r') as f:
        r = csv.reader(f, dialect='excel')
        content = list(r)
        xlist.append(content[0][0])
        for i in range(1, len(content[0])):
            ylist.append([content[0][i]])
        for i in range(1, len(content)):
            xlist.append(content[i][0])
            for j in range(1, len(content[i])):
                ylist[j-1].append(content[i][j])
    
    bar = Bar()
    bar.add_xaxis(xlist[1:])
    for i in range(len(ylist)):
        bar.add_yaxis(ylist[i][0], ylist[i][1:])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="平均负载", subtitle="1分钟,5分钟,15分钟"))
    bar.render(today + '_la.html')

def main():
    res = get_load_average()
    input_csv(list(res))
    generate_html()

if __name__ == "__main__":
    main()
