# Import the numpy library
import numpy

# Print the version of numpy being used
print(numpy.__version__)

# Create a numpy array from a list of integers
arr1 = numpy.array([1, 2, 3, 4, 5])
print(arr1)
print(type(arr1)) 

# Create a numpy array from a tuple of integers
arr2 = numpy.array((1, 2, 3, 4, 5))
print(arr2)
print(type(arr2))  

# Create a numpy array from a set of integers
# Sets are unordered, so converting to list ensures a consistent order
arr3 = numpy.array(list({1, 2, 3, 4, 5}))
print(arr3)
print(type(arr3))  

# Print the lengths of all three arrays
print(len(arr1), len(arr2), len(arr3))

# Import the numpy library with an alias 'np'
import numpy as np

# Create a 0-D array (scalar) with a single value
a = np.array(42)
print(a)

# Create a 1-D array (vector) 
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(b)

# Create a 2-D array (matrix) 
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)

# Create a 3-D array (tensor) 
d = np.array([[[1, 2, 3], [4, 5, 6]], 
              [[7, 8, 9], [10, 11, 12]]])

print(d)

# Print the number of dimensions for each array
print(a.ndim)  # 0-D array (scalar)
print(b.ndim)  # 1-D array (vector)
print(c.ndim)  # 2-D array (matrix)
print(d.ndim)  # 3-D array (tensor)

arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d[0])  # Access and print the first element
print(arr1d[0], arr1d[2])  # Access and print the first and third elements
print(arr1d[0] + arr1d[2])  # Add the first and third elements and print the result

arr2d = np.array([[1, 2, 3], 
                  [4, 5, 6]])
print(arr2d[0, 2], arr2d[1, 1])   # [0,2] -> 1st row, 3rd column; [1,1] -> 2nd row, 2nd column
print(arr2d[0, 2] + arr2d[1, 1])  # Add the elements from the 2-D array and print the result

arr3d = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])
print(arr3d[0, 0, 2])  # [0,0,2] -> 1st matrix, 1st row, 3rd element
print(arr3d[0,1,2]+arr3d[1,1,2])# arr3d[0,1,2] -> 1st matrix, 2nd row, 3rd element (6)
                                # arr3d[1,1,2] -> 2nd matrix, 2nd row, 3rd element (12)

arrn = np.array([1, 2, 3, 4, 5])
print(arrn[-1])  # Access the last element using a negative index

arr2n = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10]])
print(arr2n[0, -2])  # Access the 2nd last element of the 1st row using negative index

arr3n = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                  [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
print(arr3n[1, 1, -3])  # [1,1,-3] -> 2nd matrix, 2nd row, 3rd last element

arrs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arrs[2:6])  # Slicing from index 2 to 5 (6 is excluded)
print(arrs[4:])   # Slicing from index 4 to the end
print(arrs[:4])   # Slicing from the beginning to index 3 (4 is excluded)
print(arrs[-5:-1])  # Slicing from the 5th last to the 2nd last element
print(arrs[:-1])  # Slicing from the beginning to the second last element 
print(arrs[-5:])  # Slicing from the 5th last element to the end


arr2s = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']])
print(arr2s[1, 2:6])  # Access the 2nd row and slice from index 2 to 5 (6 is excluded)
print(arr2s[1, 2:]) # Access the 2nd row and slice from index 2 to the end
print(arr2s[1, :6])  # Access the 2nd row and slice from the start to index 5 (6 is excluded)
print(arr2s[1, -5:-1])  # Access the 2nd row and slice from the 5th last to the 2nd last element


arrd=np.array([1,2,3,4,5])
print(arrd.dtype)
arrd=np.array(['a','b','c','d','e'])
print(arrd.dtype)
arrd=np.array([1,2,3,4,5],dtype='S')
print(arrd)
print(arrd.dtype)
arrd=np.array([1,2,3,4,5],dtype='i4')
print(arrd)
print(arrd.dtype)
arrd=np.array([1.1,2.1,3.1,4.1,5.1])
print(arrd)
print(arrd.dtype)

arrd=np.array([1.1,2.1,3.1,4.1,5.1])
newarr=arrd.astype(int)
print(newarr)
print(newarr.dtype)

arrd=np.array([True,False,False,True,True])

print(arrd)
print(arrd.dtype)

arrd=np.array([True,False,False,True,True])
newarr=arrd.astype(int)
print(newarr)
print(newarr.dtype)

arrd=np.array([1,0,0,4,5])
newarr=arrd.astype(bool)
print(newarr)
print(newarr.dtype)


arr2s = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                 ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']])
print(arr2s.shape)

arrsh=np.array([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7])
newarr=arrsh.reshape(4,4)
print(newarr)

arrsh=np.array([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7])
newarr=arrsh.reshape(2,2,4)
print(newarr)

arrsh=np.array([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7])
newarr=arrsh.reshape(4,2,-1)
print(newarr)

arr2s = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                 ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']])
newarr=arr2s.reshape(-1)
print(newarr)

arr=np.array([1,2,3,4,5,6,7,8])
for x in arr:
    print(x)

arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)

arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print(y)

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    print(x)

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in np.nditer(arr):
    print(x)
        
    
arr=np.array([1,2,3,4,5,6,7,8])
for idx,x in np.ndenumerate(arr):
    print(idx,x)

arr1=np.array([1,2,3,4])
arr2=np.array([4,5,6,7])
arr=np.concatenate((arr1,arr2))
print(arr)

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)


newarr = np.array_split(arr, 7)
print(newarr)


newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])


arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)

arr = np.array([6, 8, 9,7,5,7,6])
x = np.searchsorted(arr,7)
print(x)

arr = np.array([6, 8, 9,7,5,7,6])
x = np.searchsorted(arr,7,side='right')
print(x)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

arr = np.array([3,9,2,7,0,1,8,4,3,5])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple', 'kiwi'])
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

arr=np.array([5,6,7,8])
x=[True,False,False,True]
newarr=arr[x]
print(newarr)

import pandas
import pandas as pd

print(pd.__version__)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
my_var=pandas.DataFrame(mydataset)
print(my_var)

myseies=[1,2,3,4]
x=pd.Series(myseies)
print(x)
print(x[1])
print()

x=pd.Series(myseies,index=['a','b','c','d'])
print(x)
print(x['c'])

day={'1st':'apple','2nd':'banana'}
x=pd.Series(day)
print(x)

day={'1st':'apple','2nd':'banana'}
x=pd.Series(day,index=['1st','2nd'])
print(x)

day={'1st':1,'2nd':2}
x=pd.Series(day)
print(x)

data={"1st":[1,2,3],'2nd':[4,5,6]
}
x=pd.DataFrame(data)
print(x)

data={
'2x':[2,4,6,8,10,12,14,16,18,20],
'3x':[3,6,9,12,15,18,21,24,27,30]
}
x=pd.DataFrame(data)
print(x)
print(x.loc[8])
print(x.loc[[4,8]])

x=pd.read_csv('data.csv')
print(x.to_string())

x=pd.read_csv('data.csv')
print(x)

print(pd.options.display.max_rows)

# pd.options.display.max_rows=90
x=pd.read_csv('data.csv')
print(x)

x=pd.read_json('marks.json')
print(x)

x=pd.read_json('marks.json')
print(x.to_string())

x=pd.read_csv('data.csv')
print(x.head(10))
print(x.head())
print(x.tail(10))
print(x.tail()) 
print(x.info())

new_x=x.dropna()
print(new_x.to_string())

x.dropna(inplace=True)
print(x.to_string())


x['hindi'].fillna(52,inplace=True)
x['english'].fillna(62,inplace=True)
x['maths'].fillna(92,inplace=True)
print(x.to_string())


x = pd.read_csv('data.csv')

newx = x['hindi'].mean()
print(f"Mean of Hindi scores: {newx}")
newx = x['hindi'].median()
print(f"Median of Hindi scores: {newx}")
newx = x['hindi'].mode()
print(f"Mode of Hindi scores: {newx}")

x.loc[14, 'maths'] = 45
print(x.duplicated().to_string())
print(x.corr())
print(x.to_string())
