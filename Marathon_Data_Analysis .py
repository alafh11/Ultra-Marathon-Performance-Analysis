import pandas as pd

# Load the dataset
data = pd.read_csv(
    r"C:\Users\Alaa\Desktop\project for data manipulation with python\TWO_CENTURIES_OF_UM_RACES.CSV.csv"
)

# Preview the first 5 rows of the dataset
data_preview = data.head()
# print(data_preview)

# Check the shape of the dataset
data_shape = data.shape
# print(data_shape)  # (7,461,195 records, 13 columns)

# Check the data types of each column
data_types = data.dtypes
# print(data_types, "Data types of columns")

# Filter for 50-mile races
fifty_mile_races = data[data["Event distance/length"] == "50mi"]
# print(fifty_mile_races, "50-mile races")

# Filter for both 50-mile and 50-kilometer races in 2020
fifty_mile_and_km_races_2020 = data[
    (data["Event distance/length"].isin(["50mi", "50km"]))
    & (data["Year of event"] == 2020)
]
# print(fifty_mile_and_km_races_2020, "50-mile and 50-km races in 2020")

# Get unique event names
unique_event_names = data["Event name"].unique()
unique_events_df = pd.DataFrame(unique_event_names, columns=["Event name"])
# print(unique_events_df)

# Search for a specific event in the USA
specific_event_usa = (
    data[data["Event name"] == "Ice Cubes for Brains 50 Km (USA)"]["Event name"]
    .str.split("(")
    .str.get(1)
    .str.split(")")
    .str.get(0)
)
# print(specific_event_usa)

# Filter for all events in the United States
all_usa_events = data[
    data["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == "USA"
]
# print(all_usa_events)

# Combine multiple filters: 50-mile or 50-km races in 2020 in the USA
combined_filters = data[
    (data["Event distance/length"].isin(["50mi", "50km"]))
    & (data["Year of event"] == 2020)
    & (data["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == "USA")
]
# print(combined_filters)

# Create a new DataFrame containing only USA events with 50-mile or 50-km races in 2020
usa_events_2020 = data[
    (data["Event distance/length"].isin(["50mi", "50km"]))
    & (data["Year of event"] == 2020)
    & (data["Event name"].str.split("(").str.get(1).str.split(")").str.get(0) == "USA")
]
# print(usa_events_2020.head(10))

# Remove "USA" from the Event name
usa_events_2020["Event name"] = usa_events_2020["Event name"].str.split("(").str.get(0)
# print(usa_events_2020)

# Clean the athlete age category by calculating age
usa_events_2020["Athlete year of birth"] = (
    2020 - usa_events_2020["Athlete year of birth"]
)
usa_events_2020.rename(columns={"Athlete year of birth": "Age"}, inplace=True)
# print(usa_events_2020.head(3))

# Clean the athlete performance column by removing the "h" suffix
usa_events_2020["Athlete performance"] = (
    usa_events_2020["Athlete performance"].str.split(" ").str.get(0)
)
# print(usa_events_2020.head(5))

# Drop unnecessary columns
usa_events_2020.drop(
    ["Athlete country", "Athlete age category", "Athlete club"], axis=1, inplace=True
)
# print(usa_events_2020.head(5), "After dropping unnecessary columns")

# Clean up null values
null_values_summary = usa_events_2020.isna().sum()
# print(null_values_summary)

usa_events_2020 = usa_events_2020.dropna(subset=["Age"])
# print(usa_events_2020.head(5))

updated_null_values_summary = usa_events_2020.isna().sum()
# print(updated_null_values_summary)

# Check for duplicates
duplicate_records = usa_events_2020[usa_events_2020.duplicated() == True]
# print(duplicate_records)

usa_events_2020 = usa_events_2020.reset_index(drop=True)
# print(usa_events_2020.head(5))

# Fix data types
usa_events_2020["Age"] = usa_events_2020["Age"].astype(int)
usa_events_2020["Athlete average speed"] = usa_events_2020[
    "Athlete average speed"
].astype(float)
updated_data_types = usa_events_2020.dtypes
# print(updated_data_types)

# Rename all columns for clarity
usa_events_2020 = usa_events_2020.rename(
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
# print(usa_events_2020.head(3))

# Reorder the columns for better organization
final_data = usa_events_2020[
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
print(final_data.head(10))

# Filter for 50-kilometer races
fifty_km_races = final_data[final_data["distance_length"] == "50km"]
# print("50km Races:")
# print(fifty_km_races.head())

# Now it's time for visualizations using seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Example histogram
# sns.histplot(final_data["distance_length"])
# plt.show()

# Histogram with gender differentiation
# sns.histplot(final_data, x="distance_length", hue="gender")
# plt.show()

# Distribution plot for average speed in 50-mile races
# sns.displot(final_data[final_data["distance_length"] == "50mi"]["avg_speed"])
# plt.show()

# Violin plot for average speed by distance and gender
# sns.violinplot(final_data, x="distance_length", y="avg_speed", hue="gender")
# plt.show()

# Enhanced violin plot with more details
# sns.violinplot(
#     final_data,
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

# Scatter plot with regression line for age vs. average speed
# sns.lmplot(data=final_data, x="Age", y="avg_speed", hue="gender")
# plt.show()

# ============================

# Answering specific questions

# 1. Difference in average speed between males and females for 50-km and 50-mile races
speed_by_distance_gender = final_data.groupby(["distance_length", "gender"])[
    "avg_speed"
].mean()
print(speed_by_distance_gender)

# 2. Age groups with the best average speed in 50-mile races (minimum 20 participants)
best_age_groups_50mi = (
    final_data.query("distance_length == '50mi'")
    .groupby("Age")["avg_speed"]
    .agg(["mean", "count"])
    .sort_values("mean", ascending=False)
    .query("count >= 20")
)

print(best_age_groups_50mi)

# 3. Age groups with the worst average speed in 50-mile races (minimum 20 participants)
worst_age_groups_50mi = (
    final_data.query("distance_length == '50mi'")
    .groupby("Age")["avg_speed"]
    .agg(["mean", "count"])
    .sort_values("mean", ascending=True)
    .query("count >= 20")
)

print(worst_age_groups_50mi)

# 4. Analyze performance by season (Spring, Summer, Fall, Winter)
final_data["date"] = final_data["date"].str.split(".").str.get(1).astype(int)

final_data["race_season"] = final_data["date"].apply(
    lambda x: (
        "Winter" if x > 11 else "Fall" if x > 8 else "Spring" if x > 3 else "Summer"
    )
)

print(final_data)

seasonal_performance = (
    final_data.groupby("race_season")["avg_speed"]
    .agg(["mean", "count"])
    .sort_values("mean", ascending=True)
)

print(seasonal_performance)

# Export the cleaned DataFrame to a CSV file
final_data.to_csv("cleaned_ultra_marathon_data.csv", index=False)
