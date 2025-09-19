import pandas as pd

data = {
    'calories':[420,340,390],
    'Duration':[50,40,45]
}

df = pd.DataFrame(data,index = ['Day1','Day2','Day3'])

print(df.loc[['Day1','Day2']])