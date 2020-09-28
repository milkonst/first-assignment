import pandas as pd


# wczytanie kolumn
df = pd.read_csv("train.tsv", delimiter='\t',
                 names=["Price", "Number_Of_Rooms", "Area", "Floor_Number", "Address", "Description"])


#liczenie średniej
with open('out0.csv', 'w') as csvfile:
    csvfile.write(str(df["Price"].mean().round(0)))