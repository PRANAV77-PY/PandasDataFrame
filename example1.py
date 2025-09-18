import pandas as pd

data = {
    'calories':[450,560,390],
    'duration':[50,40,45]
}

#load data into a dataframe object
df = pd.DataFrame(data)

print(df)

#refer to the row index
print(df.loc[0])

print(df.loc[[0,1]])