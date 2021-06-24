import pandas as pg
d={"name":[],"sqfeet":[],"location":[],"price":[]}
n=int(input("enter the  records num"))
for i in range(n):
     d["name"].append(input("enter the name"))
     d["sqfeet"].append(int(input("enter the sqfeet")))
     d["price"].append(int(input("enter the price")))
     d["location"].append(input("enter the location"))

print(d)
fg=pg.DataFrame(d)
fg.to_excel("sample.xlsx",index=False)




