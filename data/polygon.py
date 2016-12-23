import math
import random
import matplotlib.pyplot as plt


def do(ao):
    # 点
    class Point(object):

        def __init__(self, x, y):
            self.x, self.y = x, y

    # 向量
    class Vector(object):

        def __init__(self, start_point, end_point):
            self.start, self.end = start_point, end_point
            self.x = end_point.x - start_point.x
            self.y = end_point.y - start_point.y

        def __repr__(self):
            return repr(self.start_point, self.end_point)

        def get__start_point(self):
            return self.start

        def get__end_point(self):
            return self.end

    ZERO = 1e-9

    def negative(vector):
        """取反"""
        return Vector(vector.get__end_point(), vector.get__start_point())

    def vector_product(vectorA, vectorB):
        '''计算 x_1 * y_2 - x_2 * y_1'''
        return vectorA.x * vectorB.y - vectorB.x * vectorA.y

    def is_intersected(A, B, C, D):
        '''A, B, C, D 为 Point 类型'''
        AC = Vector(A, C)
        AD = Vector(A, D)
        BC = Vector(B, C)
        BD = Vector(B, D)
        CA = negative(AC)
        CB = negative(BC)
        DA = negative(AD)
        DB = negative(BD)
        if (A.x == C.x and A.y == C.y) or (A.x == D.x and A.y == D.y) or (B.x == C.x and B.y == C.y) or (
                B.x == D.x and B.y == D.y):
            return False
        else:
            return (vector_product(AC, AD) * vector_product(BC, BD) <= ZERO) \
                   and (vector_product(CA, CB) * vector_product(DA, DB) <= ZERO)

    A = Point(35, 82)
    B = Point(2, 84)
    C = Point(5, 82)
    D = Point(7, 21)
    print(is_intersected(A, B, C, B))

    def isInsidePolygon(pt, poly):
        c = False
        i = -1
        l = len(poly)
        j = l - 1
        while i < l - 1:
            i += 1
            print
            i, poly[i], j, poly[j]
            if ((poly[i]["lat"] <= pt["lat"] and pt["lat"] < poly[j]["lat"]) or (
                            poly[j]["lat"] <= pt["lat"] and pt["lat"] < poly[i]["lat"])):
                if (pt["lng"] < (poly[j]["lng"] - poly[i]["lng"]) * (pt["lat"] - poly[i]["lat"]) / (
                            poly[j]["lat"] - poly[i]["lat"]) + poly[i]["lng"]):
                    c = not c
            j = i
        return c

    list = []
    polygon = []
    for a in range(0, 3):
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        point = (x, y)
        list.append(point)
        polygon.append({'lat': x, 'lng': y})
    nu = 1
    while nu <= ao:
        x=random.randint(0, 99)
        y=random.randint(0, 99)
        con = 0
       # if isInsidePolygon({'lat': x, 'lng': y}, polygon) ==0 :
        if point.__contains__((x,y))==0:

            for a in range(0,len(list)-1):
                if con == 0:
                    for b in range(0, len(list)):
                        print(list)
                        print(list[a][0], list[a][1])
                        print(list[a+1][0], list[a+1][1])
                        print(list[b][0], list[b][1])


                        A = Point(x, y)
                        B = Point(list[a][0], list[a][1])
                        C = Point(list[a+1][0], list[a+1][1])
                        D = Point(list[b][0], list[b][1])
                        if b == len(list)-1 :
                            E = Point(list[0][0], list[0][1])
                            print(list[0][0], list[0][1])
                        else:
                            E = Point(list[b+1][0], list[b+1][1])
                            print(list[b + 1][0], list[b + 1][1])
                        print(is_intersected(A, B, D, E))
                        print(is_intersected(A, C, D, E))
                        if is_intersected(A, B, D, E)==1 or is_intersected(A, C, D, E)==1:
                            break
                        if b ==len(list)-1:
                            point = (x, y)
                            nu += 1
                            print(a)
                            list.insert(a+1, point)
                            polygon.insert(a+1, {'lat': x, 'lng': y})
                            con=1
                            #print(A.x,A.y,B.x,B.y,C.x,C.y,D.x,D.y,E.x,E.y)
    import csv
    with open('data.csv','w') as csvfile:
        fieldmanes =['X','Y']
        writer = csv.DictWriter(csvfile,fieldnames=fieldmanes)
        writer.writeheader()
        for a in range(0, len(list)):
            writer.writerow({'X': list[a][0], 'Y': list[a][1]})


    listxx = []
    listyy = []
    for a in range(0,len(list)):
        listxx.append(list[a][0])
        listyy.append(list[a][1])
    print(list)
    plt.plot(listxx, listyy)
    plt.plot([listxx[0],listxx[len(listxx)-1]],[listyy[0],listyy[len(listyy)-1]])
    plt.show()