# Question 1: Grade Calculator
# Write a Python function calculate_grade(marks) that takes a list of integer marks as input and calculates the average. Based on the average, return the corresponding grade according to the following criteria:
#
# A for average ≥ 90
# B for average ≥ 80 and < 90
# C for average ≥ 70 and < 80
# D for average ≥ 60 and < 70
# F for average < 60



maths=int(input("Enter your maths marks:"))
english=int(input("Enter your english marks:"))
hindi=int(input("Enter your Hindi marks:"))
socialScience=int(input("Enter your Social Science marks:"))
science=int(input("Enter your Science marks:"))
# for average of all the marks
average=(maths+english+hindi+socialScience+science)/5
print(average)
print("The Grade is:")
# condition for  grade checking
if(average>=90):
    print("A")
elif(average>=80 and average<90):
    print("B")
elif(average>=70 and average<80):
    print("C")
elif(average>=60 and average<70):
    print("D")
else:
    print("F")