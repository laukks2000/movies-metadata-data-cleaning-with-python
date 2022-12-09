# Importing the Pandas module into Python
import pandas as pd

# Reading the dataset file using Pandas and printing the output
df = pd.read_csv(r'C:\Users\Kenneth\Documents\BIS\Assignment 2\movie_metadata.csv')

# Selecting only the required columns from the dataset
df1 = df[["director_name",
          "duration",
          "director_facebook_likes",
          "actor_1_facebook_likes",
          "gross",
          "genres",
          "actor_1_name",
          "movie_title",
          "budget",
          "title_year",
          "imdb_score"]]
print(df1)
#############################################################################################
# To project the percentage of missing values
total_count = df1.count()
missing_count = df1.isnull().sum()
missing_percent = df1.isnull().sum() * 100 / len(df1)
missing_value_df1 = pd.DataFrame({'Total Count': total-count,
                                  'Count': missing count,
                                  'Percentage': missing_percent})
missing_value_df1.sort_values('Percentage', inplace=True)
print(missing_value_df1)
#############################################################################################
# Removing missing values from variables that cannot be imputed
df1 = df1.dropna(subset=['actor_1_name',
                         'actor_1_facebook_likes',
                         'director_name',
                         'director_facebook_likes',
                         'title_year'])
df1.count()
#############################################################################################
