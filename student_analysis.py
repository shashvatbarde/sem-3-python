import pandas as pd

file = open("students.csv")
df = pd.read_csv(file)

print(df)
print("Average Marks:", df["Marks"].mean())

file.close()