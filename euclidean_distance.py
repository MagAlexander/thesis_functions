# This Python file uses the following encoding: utf-8
import math

def euclidean_distance_coord(x1,y1,x2,y2):
    d = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
    return d

def euclidean_distance_id(id1,id2, n,m):
    # m rows, n columns
    x1=(id1-1)%n
    y1=(id1-1)//m
 
    x2=(id2-1)%n
    y2=(id2-1)//m
    print(id1,"=(",x1,",",y1,")\t",id2,"=(",x2,",",y2,")")
    d = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
    return d