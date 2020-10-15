import pandas as pd


#headers
df = pd.read_csv(r'C:\Users\Dell\Desktop\ML\first-assignment-master\first-assignment-master\train.tsv',
                 delimiter='\t',
                 names=["Price", "Number_Of_Rooms", "Area", "Floor_Number", "Address", "Description"])

# price per meter calc
df["Price_per_meter"] = df["Price"]/df["Area"]

# conditions
cond1 = df["Number_Of_Rooms"] >= 3
cond2 = df["Price_per_meter"] < df["Price_per_meter"].mean()

# DataFrame conditions
df2 = pd.DataFrame(df[cond1 & cond2], columns=["Number_Of_Rooms", "Price", "Price_per_meter"])


# save as csv
with open('out1.csv', 'w', encoding="utf-8") as csvfile:
    df2.to_csv(csvfile, index=False, line_terminator='\n')