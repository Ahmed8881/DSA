import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('data.csv')
print(df.dtypes)
list1=df['Name'].values.tolist()
list2=df['Age'].values.tolist()
plt.bar(list1,list2)
plt.show()