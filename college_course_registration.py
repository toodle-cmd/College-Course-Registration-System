#college_course_Registration

from datetime import datetime
today=datetime.now()
day=today.strftime("%d/%m/%Y")
Day= datetime.now()



print("\nwww.com xyz campus/college")
print("\nCOLLEGE REGISTRATION FORM",day,Day.strftime("%A"))
Menu=input("\nNew_Registartion(yes/no):").lower()
if Menu =="yes":
    
    print("\n Thankyou for applying to our college. please fill in the form below to complete the registration process for admission")
else:
    exit()


Student_Name=input("enter Student_Name :")
Student_Last_name=input("enter Student_Last_Name :")
Student_Father=input("enter Student_Father :")
Student_Mother=input("enter Student_Mother :")
while True:
    Student_DOB=input("enter Student_DOB(%d/%m/Y) :")
    try :
        datetime.strptime(Student_DOB,"%d/%m/%Y")
        print("verified")
        break
    except ValueError:
        print("please enter student_DOB (for example 21/07/2002) and (/) use this when enter DOB")

while True:
    email=input("enter email:")
    if email.endswith("@gmail.com"):
       print("verified")
       break
    else:
       print("not verified")


gender=["Male","Female","others"]
print("\n selcet ",gender)
select_gender=input("enter gender:")
if select_gender in gender:
    print("Gender verified")
else:
    print("not verified gender")

home_address=input("enter address:")
city=input("enter city:")
state=input("enter state:")

while True:
    Phone_Number=input("enter Phone_Number:")
    if len(Phone_Number) == 10 and Phone_Number.isdigit():
        print("verified")
        break
    else:
        print("not verified,please enter 10 digit number")
        


print("\n")
print("Now selecting course...")
course =["Btech","BCA","B.Com","BBA","Law"]
print("\n",course)
select_couse=input("enter select_couse:")
if select_couse == "Btech":
     data = {
        "Computer Science and Engineering (CSE)": "4 years",
        "Information Technology (IT)": "4 years",
        "Artificial Intelligence (AI)": "4 years",
        "Artificial Intelligence & Machine Learning (AI & ML)": "4 years",
        "Data Science": "4 years",
        "Cyber Security": "4 years",
        "Electronics and Communication Engineering (ECE)": "4 years",
        "Electrical Engineering (EE)": "4 years",
        "Electrical and Electronics Engineering (EEE)": "4 years",
        "Mechanical Engineering": "4 years",
        "Civil Engineering": "4 years",
        "Chemical Engineering": "4 years",
        "Biotechnology": "4 years",
        "Aerospace Engineering": "4 years",
        "Aeronautical Engineering": "4 years",
        "Automobile Engineering": "4 years",
        "Robotics Engineering": "4 years",
        "Mechatronics Engineering": "4 years",
        "Biomedical Engineering": "4 years",
        "Environmental Engineering": "4 years",
        "Petroleum Engineering": "4 years",
        "Agricultural Engineering": "4 years",
        "Mining Engineering": "4 years",
        "Metallurgical Engineering": "4 years",
        "Marine Engineering": "4 years",
        "Food Technology": "4 years",
        "Textile Engineering": "4 years",
        "Industrial Engineering": "4 years",
        "Production Engineering": "4 years",
        "Instrumentation Engineering": "4 years"
    }
     
     for course_name,duration in data.items():
       print(f"{course_name}:{duration}")
     select_branch=input("Enter couse :")
     if select_branch in data:
            print("verified")
     else:
            print("not found")


   
elif select_couse == "BCA":
    data1 = {
    "Programming Languages (C, C++, Java, Python)": "3 years",
    "Data Structures": "3 years",
    "Database Management System (DBMS)": "3 years",
    "Operating Systems": "3 years",
    "Computer Networks": "3 years",
    "Software Engineering": "3 years",
    "Web Development": "3 years",
    "Mobile Application Development": "3 years",
    "Artificial Intelligence": "3 years",
    "Machine Learning": "3 years",
    "Cloud Computing": "3 years",
    "Cyber Security": "3 years",
    "Data Analytics": "3 years",
    "Computer Graphics": "3 years",
    "Object-Oriented Programming (OOP)": "3 years",
    "Linux and Unix": "3 years",
    "Internet of Things (IoT)": "3 years",
    "Project Work / Internship": "3 years"
}
    
    for course_name,duration in data1.items():
        print(f"{course_name}:{duration}")
    select_branch=input("Enter Specialization :")
    if select_branch in data1:
        print("verified")
    else:
        print("not found")
    
    
elif select_couse == "B.Com":
    data2 = {
    "Financial Accounting": "3 years",
    "Business Economics": "3 years",
    "Business Law": "3 years",
    "Corporate Accounting": "3 years",
    "Cost Accounting": "3 years",
    "Management Accounting": "3 years",
    "Income Tax": "3 years",
    "GST (Goods and Services Tax)": "3 years",
    "Auditing": "3 years",
    "Business Statistics": "3 years",
    "Banking and Insurance": "3 years",
    "Financial Management": "3 years",
    "Human Resource Management": "3 years",
    "Marketing Management": "3 years",
    "E-Commerce": "3 years",
    "Computerized Accounting (Tally/ERP)": "3 years",
    "Entrepreneurship Development": "3 years",
    "Business Communication": "3 years"
}
    
    for course_name,duration in data2.items():
        print(f"{course_name}:{duration}")
    select_branch=input("Enter Specialization :")
    if select_branch in data2:
        print("verified")
    else:
        print("not found")
   

elif select_couse == "BBA":
    data3 = {
    "Principles of Management": "3 years",
    "Business Economics": "3 years",
    "Financial Accounting": "3 years",
    "Business Mathematics": "3 years",
    "Business Statistics": "3 years",
    "Marketing Management": "3 years",
    "Human Resource Management": "3 years",
    "Financial Management": "3 years",
    "Operations Management": "3 years",
    "Business Law": "3 years",
    "Organizational Behavior": "3 years",
    "Entrepreneurship Development": "3 years",
    "Business Communication": "3 years",
    "Digital Marketing": "3 years",
    "E-Commerce": "3 years",
    "Supply Chain Management": "3 years",
    "International Business": "3 years",
    "Project Work / Internship": "3 years"
}
    
    for course_name,duration in data3.items():
       print(f"{course_name}:{duration}")
    select_branch=input("Enter Specialization:")
    if select_branch in data3:
        print("verified")
    else:
        print("not found")



elif select_couse == "Law":
    data4 = {
    "Constitutional Law": "3 years / 5 years",
    "Criminal Law": "3 years / 5 years",
    "Contract Law": "3 years / 5 years",
    "Family Law": "3 years / 5 years",
    "Property Law": "3 years / 5 years",
    "Company Law": "3 years / 5 years",
    "Administrative Law": "3 years / 5 years",
    "Labour Law": "3 years / 5 years",
    "Environmental Law": "3 years / 5 years",
    "Intellectual Property Rights (IPR)": "3 years / 5 years",
    "Cyber Law": "3 years / 5 years",
    "Human Rights Law": "3 years / 5 years",
    "Taxation Law": "3 years / 5 years",
    "Jurisprudence": "3 years / 5 years",
    "Legal Research and Writing": "3 years / 5 years",
    "Moot Court": "3 years / 5 years",
    "Professional Ethics": "3 years / 5 years",
    "Internship": "3 years / 5 years"
}
    
    for course_name,duration in data4.items():
        print(f"{course_name}:{duration}")
    select_branch=input("Enter Specialization:")
    if select_branch in data4:
        print("verified")
    else:
        print("not found")
        


else:
    print("not found")



print("your form is filled :")
submit=input("enter submit yes or no:").lower()
if submit == "yes":
    print("your form is submitted ")
    print("\n----- Registration Summary -----")
    print("Name:", Student_Name, Student_Last_name)
    print("Course:", select_couse)
    print("Phone:", Phone_Number)
    print("Email:", email)
    print("branch_select:",select_branch)
else:
    print("not form submit")



