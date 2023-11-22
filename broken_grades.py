# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

'''Shreya Sanjay
   misis no =m00975835
'''

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #inserted 'int' before 'input'

exam_three = int(input("Input exam grade three: ")) #changed 'exam_3' to 'exam_three' and changed 'str' to 'int'

grades = [exam_one,exam_two,exam_three] #inserted comma's after each element
sum = 0
for grade in grades: #corrected 'grade' to 'grades'
  sum = sum + grade

avg = int(sum / len(grades)) #corrected 'grdes' to 'grades' and added 'int' data type

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #inserted a colon
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" #replaced single quotation mark to double quotation marks
elif avg <= 69 and avg >= 60: #changed value to 'avg >=60'
    letter_grade = "D"
else:                 #replaced 'elif' to 'else'
    letter_grade = "F"

#removed the line 'for grade in grades:'
print("Exams:"+str(grades[0]),',',str(grades[1]),',',str(grades[2])) #changed the previous code to display all the grades entered

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade is "F": #corrected 'letter-grade' to 'letter_grade'
    print( "Student is failing.") #inserted parenthesis
else:
    print("Student is passing.") #inserted parenthesis
