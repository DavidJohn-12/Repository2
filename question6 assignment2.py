import pandas as pd

# Load the dataset
data= pd.read_csv("crime.csv")

# Create the risk column
def assign_risk(crime_rate):
    if crime_rate >= 0.50:
        return "HighCrime"
    else:
        return "LowCrime"

data["risk"] = data["ViolentCrimesPerPop"].apply(assign_risk)

# Group by risk level
grouped = data.groupby("risk")

# Calculate average unemployment rate
average_unemployment = grouped["PctUnemployed"].mean()

# Print the results
for risk_level, avg in average_unemployment.items():
    print(f"{risk_level}: Average unemployment rate = {avg:.2f}")
