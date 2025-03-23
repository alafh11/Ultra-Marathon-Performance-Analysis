# Ultra Marathon Performance Analysis

## Overview
This project focuses on cleaning and analyzing a dataset of ultra marathon races over two centuries using Python. The dataset includes information about race events, athlete performance, and demographics. The cleaned data is ready for further analysis or visualization in tools like Power BI.

## Dataset
The dataset was sourced from [Kaggle](#) and contains the following key features:
- **Event name**: Name of the race.
- **Event distance/length**: Distance of the race (e.g., 50km, 50mi).
- **Year of event**: Year the race took place.
- **Athlete performance**: Performance of the athlete (e.g., time taken).
- **Athlete gender**: Gender of the athlete.
- **Athlete average speed**: Average speed of the athlete.
- **Athlete year of birth**: Birth year of the athlete (used to calculate age).

## Project Steps
1. **Data Cleaning**:
   - Handled missing values and duplicates.
   - Fixed data types and renamed columns for clarity.
   - Calculated athlete age from birth year.
   - Removed unnecessary columns.

2. **Data Analysis**:
   - Filtered data for 50-km and 50-mile races.
   - Analyzed average speed by gender and distance.
   - Identified the best-performing age groups for 50-mile races.
   - Explored seasonal trends in performance.

3. **Data Export**:
   - The cleaned and processed data is exported to a CSV file (`cleaned_ultra_marathon_data.csv`) for further use in tools like Power BI.
