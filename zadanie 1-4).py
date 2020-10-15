import pandas as pd

# read file
df_schema = pd.read_csv(r'C:\Users\Dell\Desktop\ML\developer_survey_2019\survey_results_schema.csv')
df_public = pd.read_csv(r'C:\Users\Dell\Desktop\ML\developer_survey_2019\survey_results_public.csv',
                        usecols=["Respondent", "WorkWeekHrs", "CompTotal"],
                        index_col="Respondent")


# drop null
df_public.dropna(inplace=True)

# int64
df_public = df_public.astype('int64', copy=False)
print(df_public.dtypes)