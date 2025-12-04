
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from google.colab import files
import os
import warnings
import pickle
import json
from google.colab import drive
import os

warnings.filterwarnings("ignore")

np.random.seed(31071967)




def pickle_col(PROJECT_PATH, project_config, df, col='all', drop_col=False, include_merge_ID=True, pickle_name=""):

  import pickle

  if pickle_name == "":
    file_name = f"{PROJECT_PATH}{project_config['pickles_directory']}{col}.pkl"
  else:
    file_name = f"{PROJECT_PATH}{project_config['pickles_directory']}{pickle_name}.pkl"

  with open(file_name, 'wb') as f:

    if col =='all':
      pickle.dump(df, f)

    elif col in df.columns: # in case we aready droped the col before

      # track_id for a later merge, if we need.
      #and y_col so can can invetigate the pickel later indepandantly from the main df
      pickle.dump(df[[MERGE_ON_COL, col, y_col]], f)

    f.close()

    if drop_col == True:
      df.drop(col, axis=1, inplace=True, errors='ignore')

  if project_config['split_df'] == '1':
    with open(file_name+".test.pkl", 'wb') as f:

      if col =='all':
        pickle.dump(test_df, f)

      elif col in test_df.columns: # in case we aready droped the col before
        pickle.dump(test_df[[MERGE_ON_COL, col, y_col]], f)

      f.close()

    if drop_col == True:
      test_df.drop(col, axis=1, inplace=True, errors='ignore')

  return df

