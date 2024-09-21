import matplotlib.pyplot as plt
import pandas as pd

# Solution 1  
df = pd.read_csv('Train.csv')
print(df.dtypes) 
len=len(df.columns)
names = df.columns
for i in range(0,len-1):
    plt.scatter(df[names[i]].tolist(), df[names[len-1]].tolist(), s=10, c='b', marker="s", label='first') 
plt.show()
# Solution 2
# Load the data
# data = pd.read_csv('Train.csv')
# diesease = data.columns[:-1]
# label = data['TYPE']

# Scatter plot for each symptom vs label
# for i in diesease:
#     plt.figure(figsize=(5, 3))
#     plt.scatter(data[i], label)
#     plt.title(f"Scatter plot of {i} vs Disease Label")
#     plt.xlabel(i)
#     plt.ylabel('Disease Label')
#     plt.show()

