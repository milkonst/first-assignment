import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

# wczytanie kolumn
df_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Student", "Age", "Gender", "WorkWeekHrs", "CompTotal", "YearsCode", "Age1stCode"],
                        index_col="Respondent")

# usunięcie null
df_public.dropna(inplace=True)

# zmiana tekstu na liczby
df_public.loc[df_public["YearsCode"] == "Less than 1 year"] = 0
df_public.loc[df_public["YearsCode"] == "More than 50 years"] = 55
df_public.loc[df_public["Age1stCode"] == "Younger than 5 years"] = 0
df_public.loc[df_public["Age1stCode"] == "Older than 85"] = 90

# zmiana typu na float i str
df_public["YearsCode"] = df_public["YearsCode"].astype("float64")
df_public["Age1stCode"] = df_public["Age1stCode"].astype("float64")
df_public["Gender"] = df_public["Gender"].astype("str")

# zamiana yes/no na 1/0
student_map = {"Yes, full-time": 1, "Yes, part-time": 1, "No": 0}
df_public["Student"] = df_public["Student"].map(student_map)

# One-Hot Encoding
df_public = df_public[(df_public["Gender"] == "Man") | (df_public["Gender"] == "Woman")]
df_public = pd.get_dummies(df_public, columns=["Gender"])
print(df_public)

# corr
print(df_public.corr(method='pearson'))

# usuwanie wartości odstających
Q1 = df_public.quantile(0.25)
Q3 = df_public.quantile(0.75)
IQR = Q3 - Q1

df_public = df_public[~((df_public < (Q1 - 1.5 * IQR)) | (df_public > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df_public)

# regresja liniowa
reg1 = linear_model.LinearRegression()
reg1.fit(df_public[["Age"]], df_public["YearsCode"])
print("Coefficients: \n", reg1.coef_)
print("MSE: \n %.2f"
      % mean_squared_error(df_public["YearsCode"], reg1.predict(df_public[["Age"]])))

reg2 = linear_model.LinearRegression()
reg2.fit(df_public[["Age", "Age1stCode"]], df_public["YearsCode"])
print("Coefficients: \n", reg2.coef_)
print("MSE: \n %.2f"
      % mean_squared_error(df_public["YearsCode"], reg2.predict(df_public[["Age", "Age1stCode"]])))

reg3 = linear_model.LinearRegression()
reg3.fit(df_public[["Age", "Age1stCode", "Student", "Gender_Man", "Gender_Woman"]], df_public["YearsCode"])
print("Coefficients: \n", reg3.coef_)
print("MSE: \n %.2f"
      % mean_squared_error(df_public["YearsCode"],
                           reg3.predict(df_public[["Age", "Age1stCode", "Student", "Gender_Man", "Gender_Woman"]])))