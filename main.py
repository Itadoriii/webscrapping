import pandas as pd 

url = "https://en.wikipedia.org/wiki/History_of_Python"
dfs = pd.read_html(url)
df = dfs[0]
df2 = df[['Latest micro version','Release date']]
print(df2)