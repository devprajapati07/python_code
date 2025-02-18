attend=(int(input("Number of classes attended==>")))
held=(int(input("Number of classes held==>")))

attendence=(attend/ float(held)) * 100 

if attendence>=75:
    print("the student is allow to sit in the exam.",attendence)
else:
    print("the student is not allow to sit in the exam",attendence)
