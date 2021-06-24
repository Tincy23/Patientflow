import pandas as pd
df=pd.read_excel("pq.xlsx")
print(df)

print(df.head)

print(df.tail(3))

df1=df.loc[df['modelname']=='rtyj']
print(df1)

df2=df.loc[0:1]
print(df2)

df2=df.loc[5:]
print(df2)


df2=df.loc[:,['modelname']]
print(df2)

df2.df.loc[1:5,['modelname',]]
print(df2)

df