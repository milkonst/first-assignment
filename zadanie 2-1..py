import pandas as pd

import matplotlib.pyplot as plot

# wczytanie kolumn
df_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "WorkWeekHrs", "CompTotal", "YearsCode", "Age1stCode"],
                        index_col="Respondent")

# usunięcie null
df_public.dropna(inplace=True)

# zmiana tekstu na liczby
df_public.loc[df_public["YearsCode"] == "Less than 1 year"] = 0
df_public.loc[df_public["YearsCode"] == "More than 50 years"] = 55
df_public.loc[df_public["Age1stCode"] == "Younger than 5 years"] = 0
df_public.loc[df_public["Age1stCode"] == "Older than 85"] = 90

# zmiana typu na float
df_public["YearsCode"] = df_public["YearsCode"].astype("float64")
df_public["Age1stCode"] = df_public["Age1stCode"].astype("float64")


# corr
print(df_public.corr(method='pearson'))

# wykresy
# zmienna zależna: "YearsCode"
# zmienna niezależna: "Age" & "Age1stCode"
plot.scatter(df_public["Age"], df_public["WorkWeekHrs"])
plot.title("Work Week Hours depending on Age")
plot.xlabel("Age")
plot.ylabel("Work Week Hours")
plot.show()

plot.scatter(df_public["Age"], df_public["CompTotal"])
plot.title("Total Compensation depending on Age")
plot.xlabel("Age")
plot.ylabel("Total Compensation")
plot.show()

plot.scatter(df_public["Age"], df_public["YearsCode"])
plot.title("Years of coding depending on Age")
plot.xlabel("Age")
plot.ylabel("Years of coding")
plot.show()

plot.scatter(df_public["Age"], df_public["Age1stCode"])
plot.title("Age of starting programming depending on Age")
plot.xlabel("Age")
plot.ylabel("Age of starting programming")
plot.show()

plot.scatter(df_public["WorkWeekHrs"], df_public["CompTotal"])
plot.title("Total Compensation depending on Work Week Hours")
plot.xlabel("Work Week Hours")
plot.ylabel("Total Compensation")
plot.show()

plot.scatter(df_public["YearsCode"], df_public["CompTotal"])
plot.title("Total Compensation depending on Years of coding")
plot.xlabel("Years of coding")
plot.ylabel("Total Compensation")
plot.show()

plot.scatter(df_public["YearsCode"], df_public["WorkWeekHrs"])
plot.title("Work Week Hours depending on Years of coding")
plot.xlabel("Years of coding")
plot.ylabel("Work Week Hours")
plot.show()

plot.scatter(df_public["Age1stCode"], df_public["CompTotal"])
plot.title("Total Compensation depending on Age of starting programming")
plot.xlabel("Age of starting programming")
plot.ylabel("Total Compensation")
plot.show()

plot.scatter(df_public["Age1stCode"], df_public["WorkWeekHrs"])
plot.title("Work Week Hours depending on Age of starting programming")
plot.xlabel("Age of starting programming")
plot.ylabel("Work Week Hours")
plot.show()

plot.scatter(df_public["Age1stCode"], df_public["YearsCode"])
plot.title("Years of coding depending on Age of starting programming")
plot.xlabel("Age of starting programming")
plot.ylabel("Years of coding")
plot.show()