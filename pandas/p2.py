import pandas as pd

data = {
    "name": ["John", "Anna","teena","mena","lena","sena"],
    "age": [25, 30, 28, 35, 22, 29],
    "salary": [30000, 40000, 35000, 45000, 28000, 38000],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "department": ["HR", "Engineering", "Marketing", "Sales", "IT", "Finance"],
    "experience": [2, 5, 3, 7, 1, 4],

}

df = pd.DataFrame(data)
print(df)
print(df.columns)
print(df.dtypes)    
print(df.shape)

print(df.head())   # first 5 rows
print(df.tail())   # last 5 rows
print(df.describe()) #summary statistics
print(df.info()) #info about the dataframe
print(df["name"]) #selecting a column
print(df[["name", "age"]]) #selecting multiple columns'

print(df.iloc[1]) #selecting a row by index
print(df.loc[1]) #selecting a row by label
print(df.iloc[1:4]) #selecting multiple rows by index
print(df.loc[1:4]) #selecting multiple rows by label
print(df[df["age"] > 30]) #filtering rows based on a condition
print(df[df["city"] == "New York"]) #filtering rows based on a condition
print(df.sort_values("age")) #sorting the dataframe by age
print(df.sort_values("salary", ascending=False)) #sorting the dataframe by salary in descending order
print(df.groupby("department")["salary"].mean()) #grouping by department and calculating mean
#delete
print(df.drop("experience", axis=1)) #drop a column
print(df.drop(0, axis=0)) #drop a row   
#isnull
print(df.isnull()) #check for null values
print(df.isnull().sum()) #count of null values in each column   
df.dropna(inplace=True) #drop rows with null values
print(df)