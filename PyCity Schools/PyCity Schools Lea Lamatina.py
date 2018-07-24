import pandas as pd
import numpy as np

# paths to both files
StudentFile = 'C:/Users/leala/Documents/Data Git Repo/python-challenge/Python_Challenge/Resources/students_complete.csv'
SchoolFile = 'C:/Users/leala/Documents/Data Git Repo/python-challenge/Python_Challenge/Resources/schools_complete.csv'

# open the files
student_data_raw = pd.read_csv(StudentFile)
school_data_raw = pd.read_csv(SchoolFile)

# Add columns to I'll need before merging.  Feels like the cheaters way out but it works since it only applies to school data
school_data_raw["Spending Per Student"] = school_data_raw["budget"] / school_data_raw["size"]

# I'll use this for the spending per school later on, might as well bin them now
spending_bins = [0, 585, 615, 645, 675]
spending_labels = ["<$585", "$585-615", "$615-645", "$645-675"]
school_data_raw["Spending Classification"] = pd.cut(school_data_raw["Spending Per Student"], spending_bins, labels=spending_labels)

# And this takes care of the bins for the size portion
size_bins = [0, 1501, 3001, 5000]
size_labels = ["Small", "Mid Sized", "Large"]
school_data_raw["Size Classification"] = pd.cut(school_data_raw["size"], size_bins, labels=size_labels)

# Clean up Columns and rename them to remove underscores
school_clean = school_data_raw.rename(columns={"school_name":"School Name", "type":"Type", 
                                               "size":"Size", "budget":"Budget"})
student_clean = student_data_raw.rename(columns={"school_name":"School Name", "student_name":"Student Name", 
                                                 "gender":"Gender", "grade":"Grade", "reading_score":"Reading Score", 
                                                 "math_score":"Math Score"})

# merge the two datasets on school name commonality
complete_data = pd.merge(student_clean, school_clean, how="left", on=["School Name", "School Name"])

# I'll eventually need these bins for pass/fail classification so moving them here to clean up each ask
pass_fail= [0, 69, 101]
pass_fail_labels = ['Failed', 'Passed']

complete_data["Pass/Fail Math"] = pd.cut(complete_data["Math Score"], pass_fail, labels=pass_fail_labels)
complete_data["Pass/Fail Reading"] = pd.cut(complete_data["Reading Score"], pass_fail, labels=pass_fail_labels)

# this column is because I can't get my dataframes to put numbers that don't change inside of it
complete_data["Cheat"] = int(1)

# do the column mapping here to make my numbers show cleaner
complete_data["Budget"] = complete_data["Budget"].map("${:,}".format)
complete_data["Size"] = complete_data["Size"].map("{:,}".format)
complete_data["Spending Per Student"] = complete_data["Spending Per Student"].map("${:.2f}".format)

#total number of schools, students, budget
total_schools = len(school_data_raw["school_name"])
total_students = sum(school_data_raw["size"])
total_budget = sum(school_data_raw["budget"])

# find the averages of the math/reading scores and make them variables  -- "%.2f" --
math_average = complete_data['Math Score'].mean()
reading_average = complete_data['Reading Score'].mean()

# % passing section
    # determining % pass/fail based on created columns
math_PF = complete_data["Pass/Fail Math"].value_counts()
passing_math = math_PF[1] / total_students
reading_PF = complete_data["Pass/Fail Reading"].value_counts()
passing_reading = (reading_PF[1] / total_students)

# Overall passing rate calculations
overall_passing = (passing_math + passing_reading) / 2

# create a DataFrame for the summary calculations
district_summary = pd.DataFrame({"Total Schools": total_schools, 
                                "Total Students": '{:,}'.format(total_students),
                                "Total Budget": '${:,}'.format(total_budget), 
                                 "Average Math Score": [math_average], 
                                 "Average Reading Score": [reading_average],
                                "Percent Passing Math": '{:.2%}'.format(passing_math),
                                "Percent Passing Reading": '{:.2%}'.format(passing_reading), 
                                "Overall Passing Rate": '{:.2%}'.format(overall_passing)})
district_summary.round(2)

# total number of schools, students, budget
sum_df = complete_data.groupby(["School Name", "Type"])
school_students = sum_df.sum()["Size"] / sum_df.sum()["Cheat"]
school_budget = sum_df.sum()["Budget"] / sum_df.sum()["Cheat"]

# find the averages of the math/reading scores and make them variables  -- "%.2f" --
school_math_average = sum_df.mean()['Math Score']
school_reading_average = sum_df.mean()['Reading Score']

# determining % pass/fail based on created columns
school_math_PF = sum_df["Pass/Fail Math"].value_counts()
school_passing_math = school_math_PF[1] / school_students
school_reading_PF = sum_df["Pass/Fail Reading"].value_counts()
school_passing_reading = school_reading_PF[1] / school_students

# Overall passing rate calculations
school_overall_passing = (school_passing_math + school_passing_reading) / 2

schools = pd.DataFrame({"Average Math Score": school_math_average, 
                       "Average Reading Score": school_reading_average, 
                       "Total Students": school_students,
                       "Budget": school_budget,
                       "Percent Passing Math": school_passing_math,
                       "Percent Passing Reading": school_passing_reading,
                       "Overall Passing Rate": school_overall_passing})             
schools.round()

sorted_summary = schools.sort_values("Overall Passing Rate")
sorted_summary.tail()

#  *****MATH SCORES BY GRADE*****
grades_list = complete_data.groupby(['School Name', 'Grade'])

math_summary = pd.DataFrame(grades_list["Math Score"].sum())
math_summary.head()

#  *****READING SCORES BY GRADE*****
reading_summary = pd.DataFrame(grades_list["Reading Score"].sum())
reading_summary.head()

#  *****SPENDING ANALYSIS*****
spending_group = complete_data.groupby(['Spending Classification'])

spending_students = spending_group.sum()["Size"] / spending_group.sum()["Cheat"]

spending_math_PF = spending_group["Pass/Fail Math"].value_counts()
spending_passing_math = spending_math_PF[1] / spending_students
spending_reading_PF = spending_group["Pass/Fail Reading"].value_counts()
spending_passing_reading = spending_reading_PF[1] / spending_students

# Overall passing rate calculations
spending_overall_passing = (spending_passing_math + spending_passing_reading) / 2

spending_summary = pd.DataFrame({"Reading Average": spending_group["Reading Score"].mean().round(2),
                                "Math Average": spending_group["Reading Score"].mean().round(2),
                                "Percent Passing Math": spending_passing_math,
                                "Percent Passing Reading": spending_passing_reading,
                                "Overall Passing Rate": spending_overall_passing})
spending_summary

# Size summary

size_group = complete_data.groupby(['Size Classification'])

size_students = size_group.sum()["Size"] / size_group.sum()["Cheat"]

size_math_PF = size_group["Pass/Fail Math"].value_counts()
size_passing_math = size_math_PF[1] / size_students
size_reading_PF = size_group["Pass/Fail Reading"].value_counts()
size_passing_reading = size_reading_PF[1] / size_students

# Overall passing rate calculations
size_overall_passing = (size_passing_math + size_passing_reading) / 2

size_summary = pd.DataFrame({"Reading Average": size_group["Reading Score"].mean().round(2),
                                "Math Average": size_group["Reading Score"].mean().round(2),
                                "Percent Passing Math": size_passing_math,
                                "Percent Passing Reading": size_passing_reading,
                                "Overall Passing Rate": size_overall_passing})
size_summary

type_group = complete_data.groupby(['Type'])

type_students = type_group.sum()["Size"] / type_group.sum()["Cheat"]

type_math_PF = type_group["Pass/Fail Math"].value_counts()
type_passing_math = type_math_PF[1] / type_students
type_reading_PF = type_group["Pass/Fail Reading"].value_counts()
type_passing_reading = type_reading_PF[1] / type_students

# Overall passing rate calculations
type_overall_passing = (type_passing_math + type_passing_reading) / 2

type_summary = pd.DataFrame({"Reading Average": type_group["Reading Score"].mean().round(2),
                                "Math Average": type_group["Reading Score"].mean().round(2),
                                "Percent Passing Math": type_passing_math,
                                "Percent Passing Reading": type_passing_reading,
                                "Overall Passing Rate": type_overall_passing})
type_summary