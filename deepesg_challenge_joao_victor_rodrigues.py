# -*- coding: utf-8 -*-
"""DeepESG challenge - Joao Victor Rodrigues.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UQhkwJBfzHNyUbWLWJ_ZRRrdjWDfqVJ_

## Importing libraries and gcloud configuration
"""

# Import libraries:

import pandas as pd
import numpy as np

# Authentication of google:

from google.colab import auth
auth.authenticate_user()

# Gcloud configuration. Project_id and bucket_name in GCP:

project_id = 'propane-abbey-344120'
bucket_name = 'deepesg_bucket'
!gcloud config set project {project_id}

"""## Importing datasets from GCP:

Obs: the two originals xlsx files were uploaded manually to a bucket. For more information, read the txt file "readme" on github.
"""

# Reading the dataframes:

df_ledger = pd.read_excel("https://storage.googleapis.com/deepesg_bucket/original_files/general_ledger.xlsx")
df_chart = pd.read_excel("https://storage.googleapis.com/deepesg_bucket/original_files/chart_of_accounts.xlsx")

"""## Treatment with pandas:"""

# Backups:

df_ledger_1 = df_ledger
df_chart_1 = df_chart

# Making a array for a more practical treatment:

np_chart_1 = np.array(df_chart_1)
np_ledger_1 = np.array(df_ledger_1)

# Creating a loop using "for in" to populate the most specifcs subtopics:

for i in range(len(np_chart_1)):
  sum = 0
  for line in np_ledger_1:
    if np_chart_1[i][0] == line[0]:
       sum += line[1]
  np_chart_1[i][0] = [np_chart_1[i][0],round(sum,2)]
  
np_chart_1

# Creating a list with from np_chart_1 :

list_chart = []
for item in np_chart_1:
  for j in item:
    list_chart.append(j)

list_chart

# Creating a loop to populate the entire chart:

for i in range(len(list_chart)):
  for j in range(len(list_chart)):
    if list_chart[i][0][0:2] == list_chart[j][0][0:2]:
      if list_chart [i][0] in list_chart[j][0]:
        if list_chart[i][0] == list_chart[j][0]:
          continue
        list_chart[i][1] += list_chart[j][1]
      list_chart[i][1] = round(list_chart[i][1],2)
    else:
      continue

# list_chart completed:

list_chart

# Creating a dataframe from the list_chart:

df_chart_2 = pd.DataFrame(list_chart, columns = ['accounts','values'])

# Let's see the first 30 rows:
df_chart_2.head(30)

"""## Saving a local file and upload to GCP bucket:"""

# Saving a local xlsx file:

chart_of_accounts_final_xlsx = df_chart_2.to_excel('chart_of_accounts_final_xlsx.xlsx', index = False)

# Upload the local treated xlsx file to the bucket:

!gsutil cp chart_of_accounts_final_xlsx.xlsx gs://deepesg_bucket/treated_files/chart_of_accounts_final_xlsx

# Downloading the chart_of_accounts_final_xlsx.xlsx from google colab:

from google.colab import files
files.download("chart_of_accounts_final_xlsx.xlsx")