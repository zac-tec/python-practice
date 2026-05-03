# HANDLE MISSING DATA (REAL WORLD)
import pandas as pd
data = {
    "name": ["John", "Anna","teena","mena","lena","sena"],
    "age": [25, 30, 28, 35, 22, 29],
    "salary": [30000, 40000, 35000, 45000, 28000, 38000],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "department": ["HR", "Engineering", "Marketing", "Sales", "IT", "Finance"]
}

df = pd.DataFrame(data)
print(df.isnull())# CHECK FOR NULL VALUES
print(df.isnull().sum())# COUNT OF NULL VALUES IN EACH COLUMN
df.dropna(inplace=True) # DROP ROWS WITH NULL VALUES
print(df)
#put null values
df.loc[2, "salary"] = None
print(df)
print(df.isnull())# CHECK FOR NULL VALUES
print(df.isnull().sum())# COUNT OF NULL VALUES IN EACH COLUMN
df.dropna(inplace=True) # DROP ROWS WITH NULL VALUES
print(df)
#replace null values with mean
df.loc[2, "salary"] = None
print(df)
df["salary"].fillna(df["salary"].mean(), inplace=True)
print(df)   
