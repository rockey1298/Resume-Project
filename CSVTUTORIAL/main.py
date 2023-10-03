import pandas as pd
import re

df = pd.read_csv(
    "C:/Users/drewg/OneDrive/Desktop/VISUAL STUDIO CODE PYTHON/CSVTUTORIAL/pokemon_data.csv"
)
# prints rows between 2 points
# print(df.iloc[38:55])
# gets specific location
# print(df.iloc[2, 1])

# interating through the data

# for index, row in df.iterrows():
#     print(index, row["Name"], row["Type 1"], row["Type 2"])

# print(df.loc[df["Type 1"] == "Fire"])

# print(df.sort_values("Name", ascending=False))

# print(df.sort_values(["Type 1", "HP"], ascending=[1, 0]))
# creating total column by adding all numbers together in the row

# df["Total"] = (
#     df["HP"]
#     + df["Attack"]
#     + df["Defense"]
#     + df["Sp. Atk"]
#     + df["Sp. Def"]
#     + df["Speed"]
# )


# print(df.head(5))


# how to drop table
# df = df.drop(columns=["Total"])
# fast way of creating total column then adding everything up in previous columns to create the total
df["Total"] = df.iloc[:, 4:10].sum(axis=1)
# getting a list of the columns
cols = list(df.columns.values)
# reordering list
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# print(df.head(5))
# how to save and output your new csv file
# df.to_csv("modified.csv", index=False)
# How to only print columns where the key matches what your searching for. For Panda you use & for and and | for or
# print(df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)])
# if you wanted to create a new file with this information
# new_df = df.loc[
#     (df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)
# ]
# # This is how you add a new index to the old frame, there is a way to remove the old index that we will have to look up later
# # video fucked up here on howto remove old index row. he added inplace=True at the end , however its bs and just deletes the table
# new_df = new_df.reset_index(drop=True,)
# print(new_df)

# new_df.to_csv("filtered.csv")
# ~ means not
# This is how you would search the entire table for a string and return the table depending on ~
# print(df.loc[~df["Name"].str.contains("Mega")])

# This was some chat gpt thing to delete the first row in the csv file because somehow the new indexing got into the old file
df = df.drop(df.columns[0], axis=1)
# Another example of the str.contains thing on the df.loc method
# print(df.loc[df["Type 1"].str.contains("Fire|Grass", )])


# Using regex or regular expressions within the contains method to get all names that start with pi
# print(df.loc[df["Name"].str.contains("^pi[a-z]*", flags=re.I, regex=True)])

# here we are changing every instance of fire to flamer
# df.loc[df["Type 1"] == "Fire", "Type 1"] = "Flamer"
# changing them back
# df.loc[df["Type 1"] == "Flamer", "Type 1"] = "Fire"
# This is how you would select all fire pokemon and make them legendary
# df.loc[df["Type 1"] == "Flamer", "Legendary"] = True
# print(df)

# This is how you would select a certain row, and if it meets the conditonal change the named values to the new ones provided
# df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['TEST VALUE for generation','TEST VALUE for legendary']


df = pd.read_csv("modified.csv")
# print(df)

# here we are going throughthe data file to get the types. Then, we are calculating the means for each of the types
# print(
#     df.groupby(["Type 1"])
#     .mean(numeric_only=True)
#     .sort_values("Defense", ascending=False)
# )

# Here we are adding a count column to each row for the purpose of using it to count up how many are in each row later
df["count"] = 1
print(df.groupby(["Type 1", "Type 2"]).count()["count"])
