# Ultra Marathon Performance Analysis

## Overview
This project focuses on cleaning and analyzing a dataset of ultra marathon races over two centuries using Python. The dataset includes information about race events, athlete performance, and demographics. The cleaned data is ready for further analysis or visualization in tools like Power BI.

## Dataset
The dataset was sourced from [Kaggle]([https://www.kaggle.com/datasets/your-dataset-link](https://www.kaggle.com/datasets/aiaiaidavid/the-big-dataset-of-ultra-marathon-running/discussion/420633)) and contains the following columns:

| Column Name                 | Data Type | Description                                                                 |
|-----------------------------|-----------|-----------------------------------------------------------------------------|
| **Year of event**           | int64     | The year the race took place.                                               |
| **Event dates**             | object    | The date(s) of the race.                                                    |
| **Event name**              | object    | The name of the race.                                                       |
| **Event distance/length**   | object    | The distance or length of the race (e.g., 50km, 50mi).                      |
| **Event number of finishers** | int64   | The number of athletes who finished the race.                               |
| **Athlete performance**     | object    | The performance of the athlete (e.g., time taken).                          |
| **Athlete club**            | object    | The club or team the athlete belongs to (if any).                           |
| **Athlete country**         | object    | The country of the athlete.                                                 |
| **Athlete year of birth**   | float64   | The birth year of the athlete (used to calculate age).                       |
| **Athlete gender**          | object    | The gender of the athlete.                                                  |
| **Athlete age category**    | object    | The age category of the athlete (e.g., 20-29, 30-39).                       |
| **Athlete average speed**   | object    | The average speed of the athlete during the race.                           |
| **Athlete ID**              | int64     | A unique identifier for the athlete.                                        |

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


## Conclusion
This project demonstrates the process of cleaning and analyzing a dataset of ultra marathon races using Python. The cleaned dataset (`cleaned_ultra_marathon_data.csv`) is now ready for further analysis or visualization in tools like Power BI. Key insights include trends in athlete performance by gender, distance, and age groups, as well as seasonal variations in race performance.


