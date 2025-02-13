#math for mathematical operations

import math
print(math.sqrt(44))    # Square root of 44
print(math.cbrt(44))    # Cube root of 44
print(math.factorial(4))    # Factorial of 4 (4! = 4 * 3 * 2 * 1)
print(math.pow(44,2))   # 44 raised to the power of 2 (44^2)
print(math.fabs(-55))   # Absolute value of -55
print(math.fabs(55))    # Absolute value of 55 (positive stays positive)
print(math.log(100))    # Natural logarithm (base e) of 100
print(math.log10(100))  # Logarithm of 100 with base 10
print(math.log2(100))   # Logarithm of 100 with base 2
print(math.exp(2))      # Exponential function (e^2)
print(math.floor(5.7))  # Floor value (largest integer less than or equal to 5.7)
print(math.ceil(5.7))   # Ceiling value (smallest integer greater than or equal to 5.7)
print(math.trunc(5.7))  # Truncate decimal part
print(math.pi)          # Mathematical constant Pi
print(math.e)           # Mathematical constant e 

#Logarithmic and Exponential Functions
print(math.sin(0))      
print(math.sin(1))
print(math.cos(0))
print(math.cos(1))
print(math.tan(0))
print(math.tan(1))

import os
print(os.getcwd())          # Output: Current directory path
print(type(os.getcwd()))    # Output: <class 'str'>
print(os.getrandom(2))      # Get 2 random bytes 
print(type(os.getrandom(2)))#Output: <class 'bytes'>
os.chdir#('/path/to/new/directory')
print(os.getcwd())          # Output: New directory path
print(os.listdir('/home/yensee/Desktop'))# Output: List of files and folders
# os.mkdir('new_folder')    
# os.makedirs('new_folder/hello folder')
# os.rmdir('new_folder')
# os.removedirs('new_folder/hello folder')
print(os.path.exists('myfile2.txt'))        # Output: True or False
print(os.path.isfile('myfile2.txt'))        #Output: True or False
print(os.path.isfile('yensee'))             #Output: True or False
print(os.path.isdir('/home/yensee/Desktop/TASK_S'))     #Output: True or False
os.rename('hello.txt','myfile2.txt')                    #Rename 'hello.txt' to 'myfile2.txt'
print(os.path.getsize('myfile2.txt'))                   # Get the size of 'myfile2.txt' in bytes
print(os.path.getsize('/home/yensee/Desktop/TASK_S'))   # Get the size of 'myfile2.txt' in bytes
os.rename('myfile2.txt','hello.txt')                    # Rename 'myfile2.txt' back to 'hello.txt'
# os.remove('/home/yensee/Desktop/TASK_S/myfile2.txt ') # Remove file
print(os.environ.get('TASK'))                           # Get the value of the 'TASK' environment variable
os.environ['MY_VARIABLE'] = 'HelloWorld'                # Set a new environment variable 'MY_VARIABLE'
print(os.environ.get('MY_VARIABLE'))                    # Get the value of the newly set environment variable
os.system('ls')                                         # Run a system command to list files 
print(os.path.join('folder', 'subfolder', 'file.txt'))  # Join folder names to create a file path safely
print(os.path.abspath('hello.txt'))                     # Get the absolute path of 'hello.txt'
print(os.path.abspath('file.txt'))                      # Get the absolute path of a non-existent file 'file.txt'
#Split a full file path into directory and file name
directory, file_name = os.path.split('/home/yensee/Desktop/TASK_S/hello.txt')
print(directory)                                        # Output: Directory path
print(file_name)                                        # Output: File name
print(os.path.splitext('hello.txt'))                    # Split the file name into name and extension
print(os.name)                                          # Get the name of the operating system


import random
print(random.random())
print(random.uniform(5,6))
print(random.randint(5,6))
print(random.randbytes(5))  
print(random.randrange(0, 101, 2))  
print(random.randrange(1, 100, 2))  
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'orange']
print(random.choice(fruits))  
print(random.choices(fruits, k=3))  
print(random.sample(fruits, k=3))  
random.seed(42)
print(random.random())
print(random.randint(5,6))
print(random.randbytes(5))
print(random.gauss(0, 11)) 

from datetime import *
print(datetime.now())
print(date.today())
print(datetime.now().time())

s_date=date(1997,2,12)
print(s_date)
s_time=time(8,25,58)
print(s_time)
s_datetime=datetime(1997,2,12,8,25,58)
print(s_datetime)

#Difference between dates
date1 = date(2025, 2, 13)
date2 = date(2024, 12, 25)
difference = date1 - date2
print(difference.days) 

now = datetime.now()

print(now.year)   # Output: 2025
print(now.month)  # Output: 2
print(now.day)    # Output: 13
print(now.hour)   # Output: 8
print(now.minute) # Output: 30
print(now.second) # Output: 45

#Combine date and time
d = date(2025, 2, 13)
t = time(14, 30, 45)
combined = datetime.combine(d, t)
print(combined)  # Output: 2025-02-13 14:30:45

# Split datetime into date and time
now = datetime.now()
print(now.date())  # Output: 2025-02-13
print(now.time())  # Output: 08:30:45.123456

import mymod
print(mymod.add(5,6))
print(mymod.sub(5,6))
print(mymod.mul(5,6))
print(mymod.div(5,6))
print(mymod.call("Yensee"))

from mymod import call
print(mymod.call("Ishu"))
print(mymod.mob)
from packages import my_mod 
my_mod.add(5,6)



import random
def roll_dice():
    return(random.randint(1,6))
def main():
    while True:
        input("Press Enter to roll the dice......")
        result=roll_dice()
        print(f"you rolled a {result}")
        choice=input("do you want to roll again. y/n....").lower()
        if choice!='y':
            print("Thanks for playing...")
            break
main()