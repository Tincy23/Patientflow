import pandas as pd
houseno=int(input("enter the houseno"))
place=input("enter the place")
housename=input("enter the housename")
price=int(input("enter the price"))
squarefeet=int(input("enter the squarefeet"))
d={"housenumber":[houseno,1,2],"place":[place,'a','b'],"housename":[housename,'w','f'],"price":[price,223,4244],"squarefeet":[squarefeet,2345,657]}
print(d)
df=pd.DataFrame(d)
print(df)
df.to_excel("dataset/abc.xlsx")
df.to_csv("dataset/abc.csv")

