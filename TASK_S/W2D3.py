f= open('TASK_S/myfile.txt','r')
print(f)
text = f.read()
print(text)
f.close() 

f= open('TASK_S/myfile2.txt','w')   #when you open a file in 'w', it automatically creates the file if it does not exist
print(f)

f=open('TASK_S/myfile2.txt ','w')
# f.write('Hello World')
# f.close()

with open('TASK_S/myfile2.txt','a')as f:
    f.write("Hi.. I am inside") 


f = open('/home/yensee/Desktop/TASK/TASK_S/myfile2.txt ', 'r')
while True:
    line = f.readline()
    print(line)
    if not line:  # Check if the line is empty (end of file)
        break


f = open('/home/yensee/Desktop/TASK/TASK_S/myfile2.txt ','r')
i=0
while True:
    i=i+1
    line = f.readline()
    if not line:  # Check if the line is empty (end of file)
        break  
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"marks of student {i} in maths is:{m1}")
    print(f"marks of student {i} in English is:{m2}")
    print(f"marks of student {i} in Science is:{m3}")

f=open('/home/yensee/Desktop/TASK/TASK_S/myfile.txt','w')
lines=['line 1\n','line 2\n','line 3\n',]
f.writelines(lines)
f.close()

with open('/home/yensee/Desktop/TASK/TASK_S/myfile.txt','r') as f:
    print(type(f))
    f.seek(10)  #move to the 10th byte in the file
    data=f.read(5)  #read the next five bytes
    print(data)


with open('/home/yensee/Desktop/TASK/TASK_S/myfile.txt','r') as f:
    print(type(f))
    f.seek(10)  #move to the 10th byte in the file
    print(f.tell()) #tell() gives the current byte position of the file pointer.
    data=f.read(5)  #read the next five bytes
    print(data)

with open('Sample.txt','w') as f:
    f.write("Hello World")
    f.truncate(5)  # Keep only the first 5 bytes
with open('Sample.txt','r') as f:
    print(f.read())

# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
fo.close()

with open("/home/yensee/Desktop/TASK/TASK_S/myfile.txt", "r") as file:
   content = file.read()
   print(content)

with open("foo.txt", "w") as file:
   file.write("Hello, World!")
   print ("Content added Successfully!!")

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("foo.txt", "a") as file:
   file.writelines(lines)
   print ("Content added Successfully!!")

with open("foo.txt", "r") as file:
   content = file.read()
   print(content)

file = open("foo.txt", "w")
file.write("This is an example.")
file.close()
print ("File closed successfully!!")
   
with open("foo.txt", "a") as file:
    file.write("This is an example using the with statement.")
print ("File closed successfully!!")

# Open a file in read-write mode
fo = open("foo.txt", "w+")
fo.write("This is a rat race")

fo.seek(10, 0)
data = fo.read(3)

fo.seek(10, 0)
fo.write('cat') #Overwrite the existing content with new text

fo.close()