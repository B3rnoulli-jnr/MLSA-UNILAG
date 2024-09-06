score = int(input("Enter your score: "))

if score > 100 or score < 0:
    Grade = f"No Grade, invalid number score of {score}."
elif 90 <= score <= 100:
    Grade = "A"
elif 80 <= score <= 89:
    Grade = "B"
elif 70 <= score <= 79:
    Grade = "C"
elif 60 <= score <= 69:
    Grade = "D"
elif 0 <= score <= 59:
    Grade = "F"

print(Grade)