print("To check you results follow the prompts below:")
print(" please enter your marks in each subject below between 0 to 10 :")
science = int(input("Enter marks in science:"))
economics = int(input("Enter marks in economics:"))
maths= int(input("Enter marks in maths:"))
language = int(input("Enter marks in language:"))
final = science + economics + maths + language
avg = (science + economics + maths + language)/4

if avg > 3:
    if max(science, economics, maths, language) > 10:
        print("Error, please retype.")
    elif avg >= 8 :
        print("Your final marks are:", final, "Grade: A")
    elif avg >= 6:
        print("Your final marks are:", final, "Grade: B")
    elif avg > 3:
        print("Your final marks are:", final, "Grade: C")
else:
    print("Your final marks are:", final, "Grade: F")

