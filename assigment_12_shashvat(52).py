import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("customer_churn.csv")

# Display original dataset
print("Original Dataset:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].mean()
)
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].median())

# Remove duplicate records
df = df.drop_duplicates()

# Generate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Calculate average monthly charges
print("\nAverage Monthly Charges:",
      np.mean(df["MonthlyCharges"]))

# Find maximum and minimum charges
print("Maximum Charges:", np.max(df["MonthlyCharges"]))
print("Minimum Charges:", np.min(df["MonthlyCharges"]))

# Analyze customer churn
print("\nChurn Count:")
print(df["Churn"].value_counts())

# Visualization 1: Churn distribution
df["Churn"].value_counts().plot(
    kind="bar", title="Customer Churn Distribution"
)
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

# Visualization 2: Monthly charges distribution
plt.hist(df["MonthlyCharges"], bins=10)
plt.title("Monthly Charges Distribution")
plt.xlabel("Monthly Charges")
plt.ylabel("Frequency")
plt.show()

# Visualization 3: Tenure vs Monthly Charges
plt.scatter(df["Tenure"], df["MonthlyCharges"])
plt.title("Tenure vs Monthly Charges")
plt.xlabel("Tenure")
plt.ylabel("Monthly Charges")
plt.show()