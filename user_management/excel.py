import pandas as pd

# Define the data for the students
data = {
    'Roll No': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Maths Marks': [85, 90, 75, 88],
    'Science Marks': [92, 80, 79, 85],
    'English Marks': [88, 78, 83, 90],
    'Address': ['wangoi', 'wabagai', 'imphal', 'moreh'],
    'DOB' : ['10-02-2003','23-03-2003','13-09-2001','2-07-2002'],
    'email' :['veloangom@gmail.com','khbelona@gmail.com','khdamayenti@gmail.com','xywz@gmail.com'],
    
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Define the Excel file name
excel_file = 'students.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(excel_file, index=False)

print(f'Student details have been saved to {excel_file}')
