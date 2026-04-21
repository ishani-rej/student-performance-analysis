import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (make sure file name is correct)
df = pd.read_csv("students.csv")   # or "student-por.csv"

# Check columns (for safety)
print("Columns:\n", df.columns)

# -------------------- DATA PROCESSING --------------------

# Use correct columns (G1, G2, G3)
df["Total"] = df["G1"] + df["G2"] + df["G3"]
df["Average"] = df["Total"] / 3

# Show first rows
print("\nDataset Preview:\n", df.head())

# -------------------- ANALYSIS --------------------

# Top students
top_students = df.sort_values(by="Average", ascending=False).head(5)
print("\nTop Students:\n", top_students)

# Gender-wise performance
print("\nAverage by Gender:\n", df.groupby("sex")["Average"].mean())

# Study time impact
print("\nStudy Time Impact:\n", df.groupby("studytime")["Average"].mean())

# Correlation
print("\nCorrelation:\n", df.corr(numeric_only=True))

# -------------------- VISUALIZATION --------------------

# 1. Average marks distribution
sns.histplot(df["Average"], bins=10, kde=True)
plt.title("Distribution of Average Marks")
plt.show()

# 2. Gender comparison
sns.barplot(x="sex", y="Average", data=df)
plt.title("Average Marks by Gender")
plt.show()

# 3. Study time impact
sns.barplot(x="studytime", y="Average", data=df)
plt.title("Study Time vs Performance")
plt.show()

# -------------------- GRADING --------------------

def grade(avg):
    if avg >= 15:
        return "A"
    elif avg >= 10:
        return "B"
    else:
        return "C"

df["Grade"] = df["Average"].apply(grade)

# Grade distribution
df["Grade"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.ylabel("")
plt.show()