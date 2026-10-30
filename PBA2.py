import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("employee.csv")

# Display employee details
print(df[["Name", "Department", "Salary"]])

# Employee receiving the highest salary
print("Employee with Highest Salary:")
print(df.loc[df["Salary"].idxmax()])

# Calculate average salary by department
dept_salary = df.groupby("Department")["Salary"].mean()
print("Average Salary by Department:")
print(dept_salary)

# Bar chart of average departmental salaries
dept_salary.plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")
plt.show()

# Histogram of employee salaries
plt.hist(df["Salary"], bins=5)
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.title("Distribution of Salaries")
plt.show()