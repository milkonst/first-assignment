import pandas as pd

# wczytanie pliku
df_schema = pd.read_csv("survey_results_schema.csv")
df_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "WorkWeekHrs", "CompTotal"],
                        index_col="Respondent")


# usunięcie nulli
df_public.dropna(inplace=True)

# zmiana na typ int64
df_public = df_public.astype('int64', copy=False)
print(df_public.dtypes)