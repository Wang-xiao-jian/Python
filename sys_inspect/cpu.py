#!/usr/bin/python3

import csv
import time

import psutil
import pyecharts
from pyecharts.charts import Line
from pyecharts import options as opts

head = ['time', '%cpu']
today = time.strftime('%F', time.localtime(time.time()))
filename = today + '_cpu.csv'

def init():
    with open(filename, 'w', newline='') as f:
        w = csv.writer(f, dialect='excel')
        w.writerow(head)

def get_cpu_persec():
    count = 0
    while count < 60:
        cur_time = time.strftime('%T', time.localtime(time.time()))
        cpu_res = psutil.cpu_percent()
        with open(filename, 'a+', newline='') as f:
            w = csv.writer(f, dialect='excel')
            w.writerow([cur_time, cpu_res])
        time.sleep(1)
        count += 1


def generate_html():
    xlist = []
    ylist = []

    with open(filename, 'r') as f:
        r = csv.reader(f, dialect='excel')
        for row in r:
            xlist.append(row[0])
            ylist.append(row[1])
        xlist.remove(xlist[0])
        ylist.remove(ylist[0])
    
    line1 = Line()
    line1.add_xaxis(xlist)
    line1.add_yaxis('ip1',ylist)
    line1.set_global_opts(title_opts=opts.TitleOpts('CPU实时监测'))
    line1.render(today + '.html')

def main():
    # init()
    # get_cpu_persec()
    generate_html()


if __name__ == "__main__":
    main()
