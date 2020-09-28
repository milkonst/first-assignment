import pandas as pd

# wczytanie kolumn
df = pd.read_csv("train.tsv", delimiter='\t',
                 names=["Price", "Number_Of_Rooms", "Area", "Floor_Number", "Address", "Description"])

df2 = pd.read_csv("description.csv", delimiter=',')

# złączenie dataframe
df = pd.merge(df, df2, left_on="Floor_Number", right_on="liczba", how="left")

# stworzenie DataFrame z wybranymi kolumnami
df3 = pd.DataFrame(df, columns=["Value", "Number_Of_Rooms", "Area", "Floor_Number", " opis", "Address", "Description"])


# zapisanie csv
with open('out2.csv', 'w', encoding="utf-8") as csvfile:
    df3.to_csv(csvfile, index=False, line_terminator='\n')