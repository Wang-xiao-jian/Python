#!/usr/bin/python3

from PIL import Image, ImageDraw
import csv
import datetime
import time
import os
import zipfile

hour = datetime.datetime.now().hour
now = int(time.time())

coord = {}

with open('coord.txt', 'r') as f:
    reader = csv.reader(f,delimiter=' ')
    for row in reader:
        if row[0] == '0':
            continue
        coord[row[1]] = list(row[0]) + [tuple([float(x) for x in row[2].split(',')])] + [tuple([float(x) for x in row[3].split(',')])] + [tuple([int(y) for y in x.split(',')]) for x in row[4:]]

# 将源数据压缩
z = zipfile.ZipFile('./source_data.zip', 'a')
z.write('./coord.txt', 'coord_'+ str(now) + '.txt')
z.close()
os.system('rm coord.txt')


for item in coord.items():
    pic_path = './pic/' + item[0][0:8] + '/' + item[0][8:10] + '/' + item[0]
    if (os.path.exists(pic_path) == False):
        print(pic_path, " : not found")
        continue
    im = Image.open(pic_path)
    draw = ImageDraw.Draw(im)
    plate_coord = tuple([item[1][3][0], item[1][3][1], (item[1][3][0] + item[1][3][2]), (item[1][3][1] + item[1][3][3])])
    car_coord = tuple([item[1][4][0], item[1][4][1], (item[1][4][0] + item[1][4][2]), (item[1][4][1] + item[1][4][3])])
    # 画车牌框
    draw.rectangle(plate_coord, None, 'red', 8)
    # 画车身框
    draw.rectangle(car_coord, None, 'green', 8)
    im.save(pic_path, quality=95)