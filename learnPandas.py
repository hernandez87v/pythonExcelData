import pandas as pd
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df)

ages = pd.Series([23, 45, 89], name="Age")

# print(df["Age"].min())
titanic = pd.read_csv("titanic.csv")

print(titanic)