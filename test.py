import random as rd
import numpy as np

matrice = np.zeros((100,100))
posPopA = []
posPopB = []
def generateMatrice(a,b,c):
    d = 1 - a
    e = a * 4000
    f = d * 4000
    f = int(f)
    e = int(e)
    g = list(range(1, 2)) * e
    print(g)
def setPops(pA, pB):
    print("First population")
    matriceA = np.zeros((100, 100))
    for i in range(pA):
        x = rd.randint(0, 99)
        y = rd.randint(0, 99)
        posPopA.append([x,y])
        matriceA[x, y] = 1
    print(posPopA)
    print("Second population")
    matriceB = np.zeros((100, 100))
    for i in range(pB):
        x = rd.randint(0, 99)
        y = rd.randint(0, 99)
        posPopB.append([x, y])
        matriceB[x, y] = 1
    print(posPopB)
generateMatrice(0.4,100,100)
setPops(70,30)
