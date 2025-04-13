import csv

# Set your threshold here
threshold = 80

# Read CSV and analyze grades
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    print(f"📋 Students with grade above {threshold}:")
    for row in reader:
        try:
            grade = float(row['grade'])
            if grade > threshold:
                print(f"✅ {row['name']} (Grade: {grade})")
        except ValueError:
            print(f"⚠️ Skipping row with invalid grade: {row}")