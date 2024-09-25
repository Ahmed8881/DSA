import matplotlib.pyplot as plt
import pandas as pd

def SymptomVsDisease():
    # Load the data
    data = pd.read_csv('Train.csv')
    diesease = data.columns[:-1]
    label = data['TYPE']
    # Scatter plot for each symptom vs label
    for i in diesease:
        plt.figure(figsize=(5, 3))
        plt.scatter(data[i], label)
        plt.title(f"Scatter plot of {i} vs Disease Label")
        plt.xlabel(i)
        plt.ylabel('Disease Label')
        plt.show()

if __name__ == "__main__":
    
    SymptomVsDisease()
