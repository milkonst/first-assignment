import pandas as pd

# headers
df = pd.read_csv(r'C:\Users\Dell\Desktop\ML\first-assignment-master\first-assignment-master\train.tsv', delimiter='\t',
                 names=["Price", "Number_Of_Rooms", "Area", "Floor_Number", "Address", "Description"])

df2 = pd.read_csv(r'C:\Users\Dell\Documents\GitHub\Machine_Learning\Zestaw 1\description.csv', delimiter=',')

# merge dataframe
df3 = pd.merge(df, df2, left_on="Floor_Number", right_on="liczba", how="inner")

#print(df3)
#stworzenie DataFrame z wybranymi kolumnami
df4 = pd.DataFrame(df3, columns=["Price", "Number_Of_Rooms", "Area", "Floor_Number", " opis", "Address", "Description"])
print(df4)

# zapisanie csv
with open('out2.csv', 'w', encoding="utf-8") as csvfile:
    df4.to_csv(csvfile, index=False, line_terminator='\n')