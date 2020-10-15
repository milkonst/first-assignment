import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read file
df_schema = pd.read_csv(r'C:\Users\Dell\Desktop\ML\developer_survey_2019\survey_results_schema.csv')
df_public = pd.read_csv(r'C:\Users\Dell\Desktop\ML\developer_survey_2019\survey_results_public.csv',
                        usecols=["Respondent", "Gender", "WorkWeekHrs", "CompTotal", "Age"],
                        index_col="Respondent")

# drop null
df_public.dropna(inplace=True)


# wykres

plt.scatter(df_public["Age"], df_public["WorkWeekHrs"])
plt.title("Work Week Hours depending on Age")
plt.xlabel("Age")
plt.ylabel("Work Week Hours")
plt.show()


# wykres nr2
df = df_public[(df_public["Gender"] == "Man") | (df_public["Gender"] == "Woman")]

plt.scatter(df["Gender"], df["CompTotal"])
plt.title("Total Compensation depending on Gender")
plt.xlabel("Gender")
plt.ylabel("CompTotal")
plt.show()