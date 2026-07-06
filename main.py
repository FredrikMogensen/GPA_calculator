from pypdf import PdfReader
import re


filepath = input(
    "Enter the full path to the transcript file (without quotes):\n")
reader = PdfReader(filepath)

text = ""
for page in reader.pages:
    text += page.extract_text()

grades = re.findall(
    r'[A-Ö]{4}\d\d\s.+\d\.\d\shp\s[3-5]\s\d{4}\-\d\d\-\d\d\s1', text)

total_points = 0
points_x_grades = 0

for g in grades:
    grade = int(g.split(' ')[-3])
    points = float(g.split(' ')[-5])
    total_points += points
    points_x_grades += points * grade

print(f"Grade Average: {points_x_grades / total_points}")
