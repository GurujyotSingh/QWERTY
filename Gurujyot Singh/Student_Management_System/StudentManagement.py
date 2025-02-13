
import json
import os
import pandas as pd


class Student:
    def __init__(self, std_name, std_age):      # Calling Parameterized Constructor
        # Declaring variable to be accessed globally
        self.std_name = std_name
        self.std_age = std_age

    def add_student(self):  # To add Student
        sub_marks = int(input(" Enter Number of Subjects to be added : "))  # Taking Subject Number to be added
        marks = {}
        i = 1
        while i <= sub_marks:
            subname = input("Enter Subject Name : ")    # Taking Subject Name
            val = int(input(f"\tEnter Marks for Subject {i} : "))   # Taking Subject Value
            marks.update({f"{subname}": val})
            i += 1
        main_data = {                       # Data to JSON format uisng Dict
            "Student Name": self.std_name.upper(),
            "Age": int(self.std_age),
            "Marks": marks
        }
        file_data = {}
        if os.path.exists("Student_data.json"):
            with open("Student_data.json", "r") as file:        # Accesing Student File
                file_data = json.load(file)

        file_data[self.std_name.upper()] = main_data    # Putting data as the index value of Name
        with open("Student_data.json","w") as file:
            json.dump(file_data, file, indent=4)        # Dumping data in file

    @staticmethod
    def del_student():      # To delete std rec
        with open("Student_data.json", "r") as file:
            file_data = json.load(file)
        # Getting name of std to be deleted
        student_name = input("\nEnter the name of the student to delete: ").strip().upper()

        if student_name not in file_data:   #  if student doesnt exist
            print(f"\ Student '{student_name}' not found!\n")
            return

        del file_data[student_name]     # deleteing student name using index

        with open("Student_data.json", "w") as file:
            json.dump(file_data, file, indent=4)    # exprting new data in file

        print(f"\n Student '{student_name}' has been deleted successfully!\n")

    @staticmethod
    def update_student():   # To update std rec
        name = input("Please Type the Name of the Student : ").upper()  # Taking naem to update
        if os.path.exists("Student_data.json"):
            with open("Student_data.json", "r") as file:
                file_data = json.load(file)
        if name not in file_data:
            print("Student Not Found")
        else:
            # Asking user which task to perform
            print("1. Do you want to change Student Name ? ")
            print("2. Do you want to change Student Age ? ")
            print("3. Do you want to change Student Marks ? ")
            choice = input("Enter Your choice : ")
            if choice == "1":
                # To change Name
                new_name = input("Enter the new name: ").strip().upper()
                if new_name in file_data:
                    print("\n Name already exists! Choose another name.\n")
                    return
                file_data[new_name] = file_data.pop(name)   # used pop to replcae existing name to new name
                file_data[new_name]["Student Name"] = new_name
                print("\n Student name updated successfully!\n")

            elif choice == "2":
                # TO change age
                new_age = int(input("Enter new age: "))
                file_data[name]["Age"] = new_age
                print("\nAge updated successfully!\n")

            elif choice == "3":
                # To update marks
                print("\nExisting Marks:")
                for subject, mark in file_data[name]["Marks"].items():
                    print(f"{subject}: {mark}")
                subject_to_update = input("\nEnter subject name to update (e.g., AWS): ")   # getting subname

                if subject_to_update in file_data[name]["Marks"]:
                    new_marks = int(input(f"Enter new marks for {subject_to_update}: "))
                    file_data[name]["Marks"][subject_to_update] = new_marks # updating marks
                    print("\n Marks updated successfully!\n")
                else:
                    print("\n Subject not found!\n")
                    return

            with open("Student_data.json", "w") as file:
                json.dump(file_data, file, indent=4)

    @staticmethod
    def search_student():    # To search std rec

        with open("Student_data.json", "r") as file:
            file_data = json.load(file)

        student_name = input("\nEnter the name of the student to search: ").strip().upper() # getting name to be searched
        matching_students = {}
        for name, details in file_data.items():
            if student_name in name:        # Putting std data in new var
                matching_students[name] = details

        if matching_students:   # if result matches
            #printind data
            for name, student in matching_students.items():
                print("------------------------------------")
                print("Student Found!\n")
                print(f"Name: {student['Student Name']}")
                print(f"Age: {student['Age']}")
                print("Marks:")
                for subject, mark in student["Marks"].items():
                    print(f"   - {subject}: {mark}")
        else:
            print(f"\n Student '{student_name}' not found!\n")

    @staticmethod
    def view_students():    # viewing all students
        if os.path.exists("Student_data.json"):
            with open("Student_data.json", "r") as file:    #fetching data
                file_data = json.load(file)

        for student, details in file_data.items():
            # printing data
            print("-------------------------------------")
            print(f"\t\t\tRecord of {student}")
            print("-------------------------------------")
            print(f"Name : {student}")
            print(f"Age  : {details['Age']}")
            print("Marks:")
            for subject, mark in details['Marks'].items():
                print(f"  - {subject}: {mark}")

    @staticmethod
    def export_to_csv():    # Exporting data to csv
        if not os.path.exists("Student_data.json"):
            print("No student data found!")
            return

        with open("Student_data.json", "r") as file:    # fetching data
            file_data = json.load(file)

        student_list = []
        for student, details in file_data.items():
            marks_list=[]
            for subject, mark in details["Marks"].items():  # getting marks from file
                marks_list.append(f"{subject}:{mark}")
            # getting a new dict to divide the data
            student_dict = {
                "Student Name": details["Student Name"],
                "Age": details["Age"],
                "Marks": marks_list
            }
            student_list.append(student_dict)   #adding data to list

        df = pd.DataFrame(student_list)     #CALLING PANDA TO DIVIDE LIST IN COL ROW FORMAT
        file_name = input("Enter File Name(Without extension) : ")
        df.to_csv(f"{file_name}.csv", index=False)  #CALLING INBUILT FUNCTION TO EXPORT DATA
        print(f"Student data exported successfully to '{file_name}.csv'")


# FIRST USER INTERFACE
print("Select from the following options: \n"
      "1. Add Student \t \t 2. View All Students \t\t 3. Search Student \n"
      "4. Update Record  \t 5. Delete Record \t\t 6. Export to Excel")
i = int(input("\nEnter Your Choice : "))
if i == 1:
    # Taking Student Name and Age
    std_name = input(" Enter Student Name : ")
    std_age = int(input(" Enter Student Age : "))
    obj = Student(std_name, std_age)    # Passing Name and Age to Class through constructor
    obj.add_student()   # Calling function to add Student
elif i == 2:
    Student.view_students()     # Calling function to display all the students
elif i == 3:
    Student.search_student()    # Calling function to search particular student
elif i == 4:
    Student.update_student()    # Calling function to update any record available in file
elif i == 5:
    Student.del_student()       # Calling function to delete particular record
elif i == 6:
    Student.export_to_csv()   # calling function to export file data to particular csv file
