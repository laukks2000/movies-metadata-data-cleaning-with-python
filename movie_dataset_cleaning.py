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
# Using Multivariate Imputation by Chained Equations (MICE) to impute missing values
# MICE is used as the missing values are MAR (missing at random)
# Importing the imputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn import linear_model

df_mice = df1.filter(['imdb_score', 'duration', 'gross', 'budget'], axis=1).copy()

# Defining the MICE imputer and filling in the missing values
mice_imputer = IterativeImputer(estimator=linear_model.BayesianRidge(),
                                n_nearest_features=None,
                                imputation_order='random')
df_mice_imputed = pd.DataFrame(mice_imputer.fit_transform(df_mice),
                               columns=df.mice.columns)

df_mice_imputed['duration'] = df_mice_imputed['duration'].round()
df_mice_imputed['gross'] = df_mice_imputed['gross'].round()
df_mice_imputed['budget'] = df_mice_imputed['budget'].round()

df1 = df1.drop(['imdb_score', 'duration', 'gross', 'budget'], axix=1)
df1 = pd.concat([df1, df_mice_imputed], axis=1)
df1 = df1.dropna()
##############################################################################################
# Splitting the genres and combining with the main dataset
df2 = df1.genres.str.split('|', expand=True).add_prefix('genres_')
df3 = pd.concat([df1, df2], axis=1)

# Dropping redundant variables
df3 = df3.drop(['genres'], axis=1)

# Output the dataframe into a .csv file
df3.to_csv('movie_metadata_subset_cleaned.csv', index=False)
