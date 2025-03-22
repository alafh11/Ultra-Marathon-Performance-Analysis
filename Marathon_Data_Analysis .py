import pandas as pd

# Load the dataset
df = pd.read_csv(
    r"C:\Users\Alaa\Desktop\project for data manipulation with python\TWO_CENTURIES_OF_UM_RACES.CSV.csv"
)

# Test with the first 5 lines
firstfive = df.head()
# print(firstfive)

# Check the shape of the data
shape_of_thedata = df.shape
# print(shape_of_thedata)  # (7461195 records , 13 cols)

# Check the data types
dftypes = df.dtypes
# print(dftypes, "These are the dtypes")

# Filter for 50mi races
races_50mi = df[df["Event distance/length"] == "50mi"]
# print(races_50mi, "These are the races of 50 mi")

# Filter for both 50mi and 50km races in 2020
# CHANGE HERE: Ensure "50km" is lowercase if the data uses lowercase
races_50mi_50km = df[
    (df["Event distance/length"].isin(["50mi", "50km"])) & (df["Year of event"] == 2020)
]
# print(races_50mi_50km, "races in 2020 with 50 km or mi ")

# Get unique event names
event_names_uniques = df["Event name"].unique()
unique_events_df = pd.DataFrame(event_names_uniques, columns=["Event name"])
# print(unique_events_df)

# Search for a specific event in the USA
event_search_usa = (
    df[df["Event name"] == "Ice Cubes for Brains 50 Km (USA)"]["Event name"]
    .str.split("(")
    .str.get(1)
    .str.split(")")
    .str.get(0)
)
# print(event_search_usa)

# Filter for all events in the United States
all_events_in_united_states = df[
    df["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == "USA"
]
# print(all_events_in_united_states)

# Combine multiple filters
combo_filters_XD = df[
    (df["Event distance/length"].isin(["50mi", "50km"]))
    & (df["Year of event"] == 2020)
    & (df["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == "USA")
]
# print(combo_filters_XD)

# Create a new DataFrame containing only USA events
df2 = df[
    (df["Event distance/length"].isin(["50mi", "50km"]))
    & (df["Year of event"] == 2020)
    & (df["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == "USA")
]
# print(df2.head(10))

# Remove "USA" from the Event name
df2["Event name"] = df2["Event name"].str.split("(").str.get(0)
# print(df2)

# Clean the athlete age category
# Calculate Age
df2["Athlete year of birth"] = 2020 - df2["Athlete year of birth"]
df2.rename(columns={"Athlete year of birth": "Age"}, inplace=True)
# print(df2.head(3))

# now from the athlete performance we are going to remove the h
# df2["Athlete performance"] = df2["Athlete performance"].str.replace(
#     "h", "", regex=False
# )

# Clean the athlete performance column  => we can remove the h like this too XD
df2["Athlete performance"] = df2["Athlete performance"].str.split(" ").str.get(0)
# print(df2.head(5))

# Drop unnecessary columns
df2.drop(
    ["Athlete country", "Athlete age category", "Athlete club"], axis=1, inplace=True
)
# print(df2.head(5), "This after DROPPING THE COLSSSSSSSSSSSSS")

# Clean up null values
sum_of_nullvalues_in_df2 = df2.isna().sum()
# print(sum_of_nullvalues_in_df2)

df2 = df2.dropna(subset=["Age"])
# print(df2.head(5))

new_sum_of_nullvalues_in_df2 = df2.isna().sum()
# print(new_sum_of_nullvalues_in_df2)

# Check for duplicates
check_duplicates = df2[df2.duplicated() == True]
# print(check_duplicates)

df2 = df2.reset_index(drop=True)
# print(df2.head(5))

# Fix data types
df2["Age"] = df2["Age"].astype(int)
df2["Athlete average speed"] = df2["Athlete average speed"].astype(float)
dtypes_of_df2 = df2.dtypes
# print(dtypes_of_df2)

# Rename all columns
df2 = df2.rename(
    columns={
        "Year of event": "year",
        "Event dates": "date",
        "Event distance/length": "distance_length",
        "Event number of finishers": "num_finishers",
        "Athlete performance": "performance",
        "Athlete gender": "gender",
        "Athlete average speed": "avg_speed",
        "Athlete ID": "ID",
    }
)
# print(df2.head(3))

# Reorder the columns
df3 = df2[
    [
        "date",
        "year",
        "Event name",
        "num_finishers",
        "Age",
        "avg_speed",
        "gender",
        "ID",
        "distance_length",
    ]
]
print(df3.head(10))

# Check for 50km races
df_50km = df3[df3["distance_length"] == "50km"]
# print("50km Races:")
# print(df_50km.head())

# Now it's time for graphs and use seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Example histogram
# sns.histplot(df3["distance_length"])
# plt.show()

# sns.histplot(df3, x="distance_length", hue="gender")
# plt.show()

# sns.displot(df3[df3["distance_length"] == "50mi"]["avg_speed"])
# plt.show()

# sns.violinplot(df3, x="distance_length", y="avg_speed", hue="gender")
# plt.show()
# same the last one just with more details  trying new things
# sns.violinplot(
#     df3,
#     x="distance_length",
#     y="avg_speed",
#     hue="gender",
#     split=True,
#     inner="quart",
#     linewidth=1,
# )
# plt.show()
# Summary:
# inner="quart" → Shows quartiles inside the violin.

# linewidth=1 → Sets the border thickness.
# split=True → Splits the violin into two for comparison when using hue.

sns.lmplot(data=df3, x="Age", y="avg_speed", hue="gender")
plt.show()
