import pandas as pd
import seaborn as sns

# see the data has been given


df = pd.read_csv("")

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
print(event_search_usa)


# now all the events in the united states

all_events_in_united_states = df[
    df["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == "USA"
]
print(all_events_in_united_states)
