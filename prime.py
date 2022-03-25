import sys
from datetime import datetime
def isNum(str):
    try:
        i=int(str)
    except:
        return True
    return False
def enterNum():
    strNum="a"
    while (isNum(strNum)):
        strNum=input("Please enter a upper limit: ")
    return int(strNum)
def isPrime(n):
    p = True
    if n > 1:
        for m in range(2, n):
            if n % m == 0:
                p = False
    return p
def convert_timedelta(duration):
    s=duration.seconds
    return duration.days * 24 + s, s%3600, s%60
num=0
if len(sys.argv)>1:
    if not isNum(sys.argv[1]):
        num = int(sys.argv[1])
    else:
        print(sys.argv[1], "is not a valid number")
        num=enterNum()
else:
    num=enterNum()
list =[]
ognum=num
if (num%2)!=1:
    num=num-1
ts =datetime.now()
while num>1:
    if isPrime(num):
        list.append(num)
    num=num-2
if (ognum>=2):
    list.append(2)
d=datetime.now()-ts
print(list)
h, m, s = convert_timedelta(d)
print("It took", d, "to find the", len(list), "prime numbers less than", ognum)
