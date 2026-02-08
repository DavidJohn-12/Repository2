import pandas as pd

data = pd.read_csv('student.csv',delimiter=',') #reads csv file and creates dataframe
print(data)

#validating each line according to specification
filtered_data = data[
    (data["studytime"] >= 3) &
    (data["internet"] == 1) &
    (data["absences"] <= 5)
]
print(filtered_data)
filtered_data.to_csv("high_engagement.csv",
                   index=False) #index is false to prevent adding extra index column to new file

num_students = len(filtered_data)
print("Number of students saved:", num_students)

average_grade = filtered_data["grade"].mean()
print("Average grade:", average_grade)
