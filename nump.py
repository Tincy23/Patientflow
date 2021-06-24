
import numpy as np
def numpybasics():
    array1=np.array([1,45,7,8])
    print(array1)
    #double
    array2=np.array([2.5,55,7])
    print(array2)
    #string
    array3=np.array(['a','b'])
    print(array3)
    #altogether
    array4=np.array([3,'b',7.7])
    print(array4)
    a=[1,2,3,4]
    a.append(5)
    print(a)
    array5=np.array(a)
    print(array5)
    array6=array5.copy()
    print(array6)
    array7=np.concatenate((array5,array6))
    print(array7)
    array8=np.where(array7>4)
    print(array8)
    array7[2]=7
    print(array7)

def numpysort():
    a=[1,6,9,4,32,55]
    array8=np.array(a)
    print(array8)
    array9=np.sort(array8)
    print(array9)
    a=['anu','abi','achu']
    array10=np.array(a)
    print(array10)
    array11=np.sort(array10)
    print(array11)
    a=[5.5,1.2,3.3]
    array12=np.sort(a)
    print(array12)
    array13=np.sort(array12)
    print(array13)
#numpysort()

def filter():
    a=[23,88,56,26]
    array14=np.array(a)
    print(array14)
    filter=array14>30
    print(filter)
    array16=array14[filter]
    print(array16)
#filter()

def multidimension():
    a=[[1,2],[4,6],[8,9]]
    array17=np.array(a)
    array18=np.array([[1,1],[3,5],[7,8]])
    print(array17)
    print(array18)
    array19=np.add(array17,array18)
    print(array19)
    array20=np.subtract(array17,array18)
    print(array20)
    array21=np.multiply(array17,array18)
    print(array21)
    array22=np.array([[1,2],[2,4]])
    array23=np.array([[4,3],[5,7]])
    array24=np.dot(array22,array23)
    print(array24)
    array25=np.sqrt(array17)
    print(array25)


multidimension()







