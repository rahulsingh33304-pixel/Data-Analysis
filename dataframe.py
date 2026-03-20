import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create sample data
data = {
    "Year": [2019, 2020, 2021, 2022, 2023],
    "Marks": [65, 70, 75, 80, 85],
    "Subjects": ["Math", "Science", "English", "Computer", "History"],
    "Scores": [80, 75, 70, 85, 60]
}

# create DataFrame
df = pd.DataFrame(data)

# ---------- BAR CHART ----------
plt.figure()
plt.bar(df["Year"], df["Marks"])
plt.title("Bar Chart - Marks by Year")
plt.xlabel("Year")
plt.ylabel("Marks")
plt.show()

# ---------- PIE CHART ----------
plt.figure()
plt.pie(df["Scores"], labels=df["Subjects"], autopct='%1.1f%%')
plt.title("Pie Chart - Subject Scores")
plt.show()

# ---------- SCATTER PLOT ----------
plt.figure()
plt.scatter(df["Year"], df["Marks"])
plt.title("Scatter Plot - Marks vs Year")
plt.xlabel("Year")
plt.ylabel("Marks")
plt.show()



import pandas as pd

# create employee data
data = {
    "Emp_ID": [101,102,103,104,105,106,107,108,109,110,
               111,112,113,114,115,116,117,118,119,120,
               121,122,123,124,125],
    
    "Name": ["Rahul","Amit","Sita","Riya","Karan","Neha","Arjun","Pooja","Vikas","Anjali",
             "Rohit","Simran","Deepak","Kavita","Manish","Priya","Suresh","Nisha","Vivek","Sneha",
             "Ajay","Meena","Tarun","Komal","Raj"],
    
    "Role": ["Chef","Waiter","Manager","Cashier","Cleaner","Waiter","Chef","Waiter","Manager","Cashier",
             "Cleaner","Chef","Waiter","Manager","Cashier","Cleaner","Chef","Waiter","Manager","Cashier",
             "Cleaner","Chef","Waiter","Manager","Cashier"],
    
    "Age": [25,22,30,28,35,24,27,23,32,29,
            40,26,21,33,31,38,29,22,36,27,
            34,28,23,37,30],
    
    "Salary": [20000,15000,30000,18000,12000,15000,22000,15000,32000,18000,
               12000,21000,15000,33000,19000,13000,23000,15000,34000,20000,
               14000,24000,16000,35000,21000]
}

# create DataFrame
df = pd.DataFrame(data)

# display data
print(df)