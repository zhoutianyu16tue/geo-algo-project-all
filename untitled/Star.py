import random
import sys
import os
import numpy as np
import math
import random
import matplotlib.pyplot as plt

class Point:
    __x = 0
    __y = 0
    __neb1id = 0
    __neb2id = 0
    __id = 0
    __angle =0

    def __init__(self, x, y, id):
        self.__x = x
        self.__id = id
        self.__y = y
        # self.__neb1id=neb1id
        # self.__neb2id=neb2id

    def set_x(self, x):
        self.__x = x

    def get__x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get__y(self):
        return self.__y

    def set__neb1id(self, id):
        self.__neb1id = id

    def get__neb1id(self):
        return self.__neb1id

    def set__neb2id(self, id):
        self.__neb2id = id

    def get__neb2id(self):
        return self.__neb2id

    def set_id(self, id):
        self.__id = id

    def get__id(self):
        return self.__id
    def get__angle(self):
        return self.__angle

    def __repr__(self):
        return repr((self.__x, self.__angle, self.__y))

    def calculateAngle(self, x2, y2):
        angle = 0
        y_se = self.__y - y2
        x_se = self.__x - x2
        if x_se == 0 and y_se > 0:
            angle = 360
        if x_se == 0 and y_se < 0:
            angle = 180
        if y_se == 0 and x_se > 0:
            angle = 90
        if y_se == 0 and x_se < 0:
            angle = 270
        if x_se > 0 and y_se > 0:
            angle = math.atan(x_se / y_se) * 180 / math.pi
        elif x_se < 0 and y_se > 0:
            angle = 360 + math.atan(x_se / y_se) * 180 / math.pi
        elif x_se < 0 and y_se < 0:
            angle = 180 + math.atan(x_se / y_se) * 180 / math.pi
        elif x_se > 0 and y_se < 0:
            angle = 180 + math.atan(x_se / y_se) * 180 / math.pi
        self.__angle= angle
# commend



def do(a):
    list = []
    listx = []
    listy = []
    listpoint = []
    listxx = []
    listyy = []
    nu = 1
    while nu <= a:
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        point = (x, y)
        list.append(point)
        listx.append(x)
        listy.append(y)
        p = Point(x,y,nu)

        listpoint.append(p)
        # print(list[0][0])
        nu += 1
    averagex = sum(listx)/len(listx)
    averagey= sum(listy)/len(listy)
    for a in range(0,len(listpoint)):
        listpoint[a].calculateAngle(averagex, averagey)

    listpoint.sort(key = lambda pp:pp.get__angle())
    import csv
    with open('data.csv','w') as csvfile:
        fieldmanes =['X','Y']
        writer = csv.DictWriter(csvfile,fieldnames=fieldmanes)
        writer.writeheader()
        for a in range(0, len(listpoint)):
            writer.writerow({'X':listpoint[a].get__x(),'Y':listpoint[a].get__y()})

    for a in range(0,len(listpoint)):
        listxx.append(listpoint[a].get__x())
        listyy.append(listpoint[a].get__y())

    plt.plot(listxx, listyy)
    plt.plot([listxx[0],listxx[len(listxx)-1]],[listyy[0],listyy[len(listyy)-1]])
    plt.show()
