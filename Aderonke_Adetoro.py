#!/usr/bin/env python
# coding: utf-8

# ### Creating a Student Grade Management System

# In[247]:


### student data function definition
def collect_student_data(): #system function creation
    students = {} # initialising a dictionary to store collected student data
    
### collecting student data using while loop and user input
    while True:
        print (f"Hello student, your Name and selected subject scores will be requested for and recorded")
        student_name = input("Enter your Surname and First name (or type completed to finish): ")
        if student_name.lower() == "completed": # initialising an exit for the input function
            break

        try: # getting subject scores with validation
            math_score = float(input("Enter your Math score: "))
            science_score = float(input("Enter your Science score: "))
            english_score = float(input("Enter your English score: "))

        except: # invalid input error handling
            print(f"Invalid input, please enter numerical values only for your subject scores")
            continue

### calculating student average score across the three subjects using mathematical operators
        total_score = (math_score + science_score + english_score)
        average_score = total_score / 3

### grade assignment based on student average score using conditional statement

        if average_score >= 85:
            grade = "A"
        elif average_score >= 75:
            grade = "B"
        elif average_score >= 65:
            grade = "C"
        elif average_score >= 55:
            grade = "D"
        else:
            grade = "F"

### creating Student Data using a Dictionary
        student_data = {"Math" : math_score,
                        "Science" : science_score, 
                        "English" : english_score,
                        "Average Score" : average_score,
                        "Final Grade": grade,
            
                       }
        students[student_name] = student_data  #updating the dictionary witha nested dictionary

    return students


# In[257]:


### displaying student data using function, and looping through student dictionary

def display_data(students):
    print ("\nDISPLAYING STUDENT DATA: ")
    for student_name, data in students.items():
        print (f"{student_name}'s grade is: ")
        for key, value in data.items():
            print (f"\n\t{key}: {value}")


# In[280]:


### Creating a Menu driven interface for data collection and retrieval based on user's input/choice

def menu_interface():  # function created
    students = {}       # initialising student dictionary
    while True:   # initialsing condition
        
        ### displaying messages to assist user's choice
        print("\n STUDENT DATA MANAGEMENT SYSTEM ")
        print ("Enter 1 to enter Student Data ")
        print ("\n Enter 2 to display Student Data ")
        print ("\n Enter 3 to exit the system ")
        user_choice = input("Enter your choice between 1-3: ")

        if user_choice == "1":
            student_data = collect_student_data()  # function call
            students.update(student_data)  # data updating in the student dictionary
        elif user_choice == "2":
            display_data(students)  # function call
        elif user_choice == "3":
            print ("Exiting the Student Data Management System, Goodbye!!") #program exit condition message
            break
        else:
            print ("Invalid choice, please enter a number between 1-3. ")
        
if __name__ == "__main__":       ### for direct script execution
    menu_interface()       ###calling the function
    


# In[ ]:




