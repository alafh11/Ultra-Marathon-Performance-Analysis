import pandas as pd
import seaborn as sns

# see the data has been given


df = pd.read_csv(
    r"C:\Users\Alaa\Desktop\project for data manipulation with python\TWO_CENTURIES_OF_UM_RACES.CSV.csv"
)

# Test is with the first 5 lines
firstfive = df.head()

# print(firstfive)


shape_of_thedata = df.shape
# print(shape_of_thedata)
# (7461195 records , 13 cols)

dftypes = df.dtypes
# print(dftypes, "These are the dtypes")

# races 50mi , 2020

races_50mi = df[df["Event distance/length"] == "50mi"]
# print(races_50mi, "These are the races of 50 mi")


# now more creative like let's try both 50 min and 50 km

races_50mi_50km = df[
    (df["Event distance/length"].isin(["50mi", "50Km"])) & (df["Year of event"] == 2020)
]
# print(races_50mi_50km, "races in 2020 with 50 km or mi ")

event_names_uniques = df["Event name"].unique()
unique_events_df = pd.DataFrame(event_names_uniques, columns=["Event name"])
# print(unique_events_df)


event_search_usa = (
    df[df["Event name"] == "Ice Cubes for Brains 50 Km (USA)"]["Event name"]
    .str.split("(")
    .str.get(1)
    .str.split(")")
    .str.get(0)
)
# print(event_search_usa)


# now all the events in the united states

all_events_in_united_states = df[
    df["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == "USA"
]
# print(all_events_in_united_states)


# combining many filters together

combo_filters_XD = df[
    (df["Event distance/length"].isin(["50mi", "50Km"]))
    & (df["Year of event"] == 2020)
    & (df["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == "USA")
]

# print(combo_filters_XD)


# lets create a new dataframe just containing the usa events

df2 = df[
    (df["Event distance/length"].isin(["50mi", "50Km"]))
    & (df["Year of event"] == 2020)
    & (df["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == "USA")
]


# print(df2.head(10))


# remove usa from df2
df2["Event name"].str.split("(").str.get(0)
# print(df2)


# clean the athlete age category

# Calculate Age
df2["Athlete year of birth"] = 2020 - df2["Athlete year of birth"]
df2.rename(columns={"Athlete year of birth": "Age"}, inplace=True)

# print(df2.head(3))

# now from the athlete performance we are going to remove the h

# df2["Athlete performance"] = df2["Athlete performance"].str.replace(
#     "h", "", regex=False
# )

# or we can do it like this

df2["Athlete performance"] = df2["Athlete performance"].str.split(" ").str.get(0)

# print(df2.head(5))


# now we are going to drop colomns that we dont need for example lilke athlete club , athlete country  , athlete year of birth

df2.drop(
    ["Athlete country", "Athlete age category", "Athlete club"], axis=1, inplace=True
)

# print(df2.head(5), "This after DROPPING THE COLSSSSSSSSSSSSS")

# now let's clean up null values


sum_of_nullvalues_in_df2 = df2.isna().sum()

# print(sum_of_nullvalues_in_df2)

df2 = df2.dropna(subset=["Age"])
# another method df2["Age"] = df2["Age"].fillna(0)  # Or use df2["Age"].fillna(df2["Age"].mean())

# print(df2.head(5))
new_sum_of_nullvalues_in_df2 = df2.isna().sum()

# print(new_sum_of_nullvalues_in_df2)


# check for duplicate
check_duplicates = df2[df2.duplicated() == True]

print(check_duplicates)

df2 = df2.reset_index(drop=True)
# print(df2.head(5))


# fix types

dtypes_of_df2 = df2.dtypes
print(dtypes_of_df2)
