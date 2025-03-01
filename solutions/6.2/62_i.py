import pandas as pd

FILE_NAME = "data.csv"
df = pd.read_csv(FILE_NAME)

x_min, y_min = map(int, input().split())
x_max, y_max = map(int, input().split())

if x_min > x_max:
    x_min, x_max = x_max, x_min

if y_min > y_max:
    y_min, y_max = y_max, y_min

df = df[(df["x"].between(x_min, x_max)) & (df["y"].between(y_min, y_max))]

print(df)
