import pandas as pd
from dataset import clean_data

df = clean_data()

pivot = pd.pivot_table(
    df,
    index='Category',
    columns='Is_VIP',
    values='Total_Spent',
    aggfunc='sum'
)

print(pivot)
