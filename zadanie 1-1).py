import pandas as pd


#headers
df = pd.read_csv(r'C:\Users\Dell\Desktop\ML\first-assignment-master\first-assignment-master\train.tsv',
                 delimiter='\t',
                 names=["Price", "Number_Of_Rooms", "Area", "Floor_Number", "Address", "Description"])


#mean calc
mean_price = str(df["Price"].mean().round(0))

with open('out0.csv', 'w') as csvfile:
    csvfile.write(mean_price)

#    print(df)
#    print(mean_price)