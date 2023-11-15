import math
import random


def fel1(szam1: int, szam2: int):
    osszeg: int = 0
    i = szam1
    while szam1 < szam2:
        if szam1 == i:
            szam1 += 1
        if szam1 % 2 == 0:
            osszeg += szam1
        szam1 += 1
    return osszeg


def fel2():
    szam: float = math.floor(random.random()*20-10)
    i: int = 0
    db: int = 0
    while i < 20:
        szam: float = math.floor(random.random()*21-10)
        if szam < 0:
            db += 1
        i += 1
    return db


def fel3(szam1: int, szam2: int):
    osszeg: int = 0
    for i in range(szam1, szam2):
        if i == szam1:
            i += 1
        if i % 2 == 0:
            osszeg += i
    return osszeg


def fel4():
    osszeg: int = 0
    for i in range(0, 10, 1):
        szam: float = math.floor(random.random() * 22 + 12)
        osszeg += szam
    return osszeg


def fel5():
    legnagyobb: float = 0
    for i in range(0, 8, 1):
        szam: float = math.floor(random.random() * 30 + 20)
        if szam > legnagyobb:
            legnagyobb = szam
    return legnagyobb


def fel6():
    osszeg: int = 0
    atlag: float = 0
    for i in range(0, 3, 1):
        szam: int = int(input(f"Adja meg az {i+1}. számot!"))
        osszeg += szam
    atlag = osszeg/3
    return atlag


def fel7():
    i: int = 0
    osszeg: int = 0
    szam: int = int(input(f"Adjon meg az {i + 1}. számot!"))
    while szam != 0:
        osszeg += szam
        i += 1
        szam: int = int(input(f"Adjon meg a {i + 1}. számot!"))
    return osszeg/i
