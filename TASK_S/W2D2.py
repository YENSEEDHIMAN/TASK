# prin("Hello World")         #Incorrect (should be print)

# print("Hello World!"        # Missing closing parenthesis

# print("Hello World)         #unterminated string literal

# def add(n):
# print(n)                    #IndentationError
# add(5)

# a=5
# if a>0                          #SyntaxError: expected ':'
#     print("A is a greater than zero")

# class="Raman"                  #SyntaxError: invalid syntax

# a=10
# b=a/0                           #ZeroDivisionError: division by zero
# print(b)

# import math
# print(math.exp(1000))              #OverflowError: math range error

# print("hello"+5)                    #TypeError: can only concatenate str (not "int") to str

# print(x)                        #NameError: name 'x' is not defined

# num=10
# print(num.append(5))            #AttributeError: 'int' object has no attribute 'append'

# lst=[1,2,3,4,5]
# print(lst[5])                       #IndexError: list index out of range

# dic={"a":1,"b":2}
# print(dic["c"])                         #KeyError: 'c'


# try:
#     num=int(input("Enter a number: " ))
#     print(10/num)
# except ZeroDivisionError: #If the user enters 0                  
#     print("You can't divide by zero")
# except ValueError: #If the user enters non-numeric input (e.g., "abc", "@", "1.5")
#     print("Invalid input! please enter a number")


# try:
#     age=int(input("Enter your age: "))
#     if age<18:
#         raise ValueError("You must be 18 or older to proceed.")
#     print("Access Granteed")
# except ValueError as e:         #Error invalid literal for int() with base 10: 'u'
#     print("Error",e)


# try:
#     num=int(input("Enter a number: "))
#     if num<0:
#         raise ValueError ("negative number not allowed")
#     print("You Entered",num)
# except ValueError as e:
#     print(e)


# try:
#     num=int(input("Enter a number: "))
#     result= 100/num
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# else:
#     print(result)
# finally:
#     print("Execution complete")


# try:
#     num=int(input("Enter a number: "))
#     result= 100/num
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# except ValueError as e:
#     print(e)
# else:
#     print(result)
# finally:
#     print("Exexution complete")


# age = int(input("Enter your age: "))
# if age <= 18:
#     raise ValueError("You must be 18 or older.")       #raise an error


# class youaretooyoung(Exception):
#     pass
# age = int(input("Enter your age: "))
# if age < 18:
#     raise youaretooyoung("You are two young to vote")  #Creating Custom Exceptions


# def validate_username(username):
#     if len(username)<5:
#         raise ValueError("Username must be at least 5 characters long.")
# try:
#     user=str(input("Enter the username: "))
#     validate_username(user)
#     print("Welcome",user)
# except ValueError as e:
#     print(f"Error: {e}")

# import sys
# try:
#     file=open("Complete_with_Docusign_Yenseedocx_Yenseed8.pdf",'r')
# except Exception as e: 
#     print(e) 


# try:
#     large_list = [1] * (100**9)  
# except MemoryError:
#     print("MemoryError: Not enough memory!")

# import sys
# try:
#     file=open("Complete_with_Docusign_Yenseedocx_Yenseed8.pdf",'r')
# except Exception:
#     print(sys.exc_info()[0]) 
#     print(sys.exc_info()[1]) 
#     print(sys.exc_info()[2]) 

# try:
#     result = 1.0 / 0.0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# try:
#     assert 1 == 2,"Assertion failed"
# except AssertionError as e:
#     print(e)

# d = {"key1": "value1"}
# try:
#     val = d["key2"]
# except KeyError as e:
#     print(e)
