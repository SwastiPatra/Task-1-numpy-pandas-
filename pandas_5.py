import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("Original Dataframe:")
print("diamonds.shape")
print("\nDuplicate rows of diamonds Dataframe:")
print(diamonds.duplicated().sum()) 