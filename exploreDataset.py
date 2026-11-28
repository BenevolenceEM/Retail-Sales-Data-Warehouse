import pandas as pd

df = pd.read_excel("Online Retail.xlsx")

#Display the first 5 rows of the dataset
print(df.head())

#List the number of rows and columns in the dataset
print("\nRows:", len(df))
print("\nColumns:")
print(df.columns)

#Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

#Check for total values in the dataset
print("\nTotal Values:")
print(df["InvoiceNo"].count())
print(df["StockCode"].count())
print(df["CustomerID"].count())

#Check for unique values in the dataset
print("\nUnique Values:")
print(len(df["InvoiceNo"].unique()))
print(len(df["StockCode"].unique()))
print(len(df["CustomerID"].unique()))