import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dailySteps_merged.csv')
print(df.dtypes)
df['ActivityDay']=pd.to_datetime(df['ActivityDay'])
grouped_df = df.groupby('ActivityDay')['StepTotal'].sum().reset_index()
grouped_df=grouped_df.sort_values('ActivityDay')
list1 = grouped_df['ActivityDay'].values.tolist()
list2 = grouped_df['StepTotal'].values.tolist()
plt.plot(list1, list2)
plt.show()
