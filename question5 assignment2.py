import pandas as pd

# Load the dataset
data = pd.read_csv("student.csv")

# Create grade_band column
def assign_band(grade):
    if grade <= 9:
        return "Low"
    elif grade <= 14:
        return "Medium"
    else:
        return "High"

data["grade_band"] = data["grade"].apply(assign_band)

# Group by grade band
grouped = data.groupby("grade_band")

# Create summary statistics
summary = pd.DataFrame({
    "number_of_students": grouped.size(),
    "average_absences": grouped["absences"].mean(),
    "internet_percentage": grouped["internet"].mean() * 100
})

# Save the result
summary.to_csv("student_bands.csv")
