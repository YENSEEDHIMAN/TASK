
import math
import random
import re
import sys

# Question:1
def common_chars(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)
    top3_chars = sorted_chars[:3]
    for char, count in top3_chars:
        print(char, count)
        
common_chars('GOOGLE')




# Question:2
nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k=int(input())
arr.sort(key=lambda x:x[k])
for row in arr:
    print(*row)





# Question:3
import os
from datetime import datetime
def time_delta(t1, t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)
    return str(abs(int((dt1 - dt2).total_seconds())))

if __name__ == "__main__":

    fptr = os.environ.get('OUTPUT_PATH', '/home/yensee/Desktop/TASK1/output.txt')
    with open(fptr, 'w') as fptr:
        t = int(input())
        for t_itr in range(t):
            t1 = input()
            t2 = input()
            delta = time_delta(t1, t2)
            fptr.write(delta + '\n')
    fptr.close()



    
# Question:4
n=int(input("Enter the number of countries you want to enter:"))
counts=set()
for _ in range(n):
    count=input()
    counts.add(count)
print(len(counts))

