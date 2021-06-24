import pandas as pk
d={"username":[],"usermobileno":[],"user address":[],"companyname":[],"modelname":[],"power":[],"fueltank capacity":[],"total kms runned":[],"total no of services":[]}
n = int(input("enter the records "))
for i in range(n):
     d["username"].append(input("enter the name"))
     d["usermobileno"].append(int(input("enter the mobile no")))
     d["user address"].append(input("enter the address"))
     d["companyname"].append(input("enter the compamy name"))
     d["modelname"].append(input("enter the model name"))
     d["power"].append(int(input("enter the power")))
     d["fueltank capacity"].append(int(input("enter the capacity")))
     d["total kms runned"].append(int(input("enter the kms")))
     d["total no of services"].append(int(input("enter the total no of services")))

print(d)
fg = pk.DataFrame(d)
fg.to_excel("pq.xlsx", index=False)


