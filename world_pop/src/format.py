import numpy as np
import pandas as pd
import pickle

with open('countries.pkl', 'rb') as f:
    countries = pickle.load(f)

df = pd.read_csv('world_pop_raw.csv')
df.drop('2019', axis=1, inplace=True)
df.replace(np.nan, 0)

ctry_codes = {}
for code, ctry in countries:
    ctry_codes[ctry] = code

url = 'https://www.countryflags.io/{0}/flat/64.png'
df.insert(1, "flags", 'manual entry')
for idx, row, in df.iterrows():
    curr_ctry = row[0]
    # for each country, add in the flag url using the ctry_codes map
    if curr_ctry in ctry_codes:
        curr_code = ctry_codes[curr_ctry]
        curr_url = url.format(curr_code.lower())
        df.at[idx, 'flags'] = curr_url
print(df)


# print(df['1960'][0])
# print(df['Country Name']['Aruba'])
df.to_csv('processed.csv')
