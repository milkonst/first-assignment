import pandas as pd


# wczytanie kolumn
df = pd.read_csv("train.tsv", delimiter='\t',
                 names=["Price", "Number_Of_Rooms", "Area", "Floor_Number", "Address", "Description"])

# średnia za metr
df["Price_per_meter"] = df["Price"]/df["Area"]

# selekcja
pokoje = df["Number_Of_Rooms"] >= 3
cena = df["Price_per_meter"] < df["Price_per_meter"].mean()

# stworzenie DataFrame z selekcji
df2 = pd.DataFrame(df[pokoje & cena], columns=["Number_Of_Rooms", "Price", "Price_per_meter"])

# zapisanie csv
with open('out1.csv', 'w', encoding="utf-8") as csvfile:
    df2.to_csv(csvfile, index=False, line_terminator='\n')