import pandas as pd

import matplotlib.pyplot as plot

# # wczytanie pliku
df_schema = pd.read_csv("survey_results_schema.csv")
df_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "Gender", "WorkWeekHrs", "CompTotal", "CurrencySymbol"],
                        index_col="Respondent")

# usunięcie nulli
df_public.dropna(inplace=True)


# wykres
plot.scatter(df_public["Age"], df_public["WorkWeekHrs"])
plot.title("Work Week Hours depending on Age")
plot.xlabel("Age")
plot.ylabel("Work Week Hours")
plot.show()

# wykres nr2
df_public = df_public.loc[df_public["CurrencySymbol"] == "PLN"]
df = df_public[(df_public["Gender"] == "Man") | (df_public["Gender"] == "Woman")]
df = df[["Age", "Gender", "WorkWeekHrs", "CompTotal", "CurrencySymbol"]]

plot.scatter(df["Gender"], df["CompTotal"])
plot.title("Total Compensation depending on Gender")
plot.xlabel("Gender")
plot.ylabel("Total Compensation")
plot.show()