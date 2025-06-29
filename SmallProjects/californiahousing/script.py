# %% [markdown]
# Importing all packages
# 

# %%


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

# %% [markdown]
# Importing the data

# %%
df = pd.read_csv(r'C:\Users\Ananya\Downloads\Assignments\/californiahousing.csv')


# %% [markdown]
# Understanding the data
# 

# %%

df.head()
df.info()
df.describe()


# %% [markdown]
# 
# 
# Fixing the missing values
# 

# %%

df.isnull().sum()
df = df.fillna(method="ffill")

df.isnull().sum()



# %% [markdown]
# 
# Statistical analysis
# 

# %%

# Ocean proximity
sns.set_theme(style="dark")
sns.countplot(x="ocean_proximity", data=df, palette="prism")

# Median house value x ocean proximity
sns.barplot(x='ocean_proximity', y='median_house_value',
            data=df, palette="prism")

# Median Price of Houses in a block in $
plt.hist(df.median_house_value, bins=40, color='#E11439')
plt.xlabel('Median Price of Houses in a block in $')
plt.ylabel('Number of Houses')
plt.title('Average Distribution of Median Price of Housing')




# %% [markdown]
# Plotting the points on a map
# 


