#!/usr/bin/python3

import csv
import time

import psutil
import pyecharts
from pyecharts import options as opts
from pyecharts.charts import Line

today = time.strftime('%F', time.localtime(time.time()))
filename = today + '_cpu.csv'

def get_csvhead():
    res = ['time', 'turtle']
    for i in range(1, psutil.cpu_count() + 1):
        res.append('core%d'%i)
    return res

def get_cpu_percent():
    cur_time = time.strftime('%T', time.localtime(time.time()))
    cpu_res_turtle = psutil.cpu_percent()
    percpu = psutil.cpu_percent(percpu=True)
    rows = [cur_time, cpu_res_turtle]
    rows += percpu

    with open(filename, 'r+', newline='') as fw:
        r = csv.reader(fw, dialect='excel')
        if len(list(r)) == 0:
            w = csv.writer(fw, dialect='excel')
            w.writerow(get_csvhead())

    with open(filename, 'a+', newline='') as f:
        w = csv.writer(f, dialect='excel')
        w.writerow(rows)

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
    
    line = Line()
    line.add_xaxis(xlist[1:])
    for i in range(len(ylist)):
        line.add_yaxis(ylist[i][0], ylist[i][1:])
    line.set_global_opts(title_opts=opts.TitleOpts('CPU实时监测'))
    line.set_global_opts(xaxis_opts = opts.AxisOpts(name = xlist[0]))
    line.set_global_opts(yaxis_opts = opts.AxisOpts(name = 'percent'))

    line.render(today + '_cpu.html')
    

def main():
    get_cpu_percent()
    generate_html()


if __name__ == "__main__":
    main()
