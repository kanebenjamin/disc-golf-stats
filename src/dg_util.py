from errno import ENETRESET
from tkinter import *
import json
import os
from tkinter import messagebox

#Find data file:
filename = 'course_data.json' 
if '_MEIPASS2' in os.environ:
    filename = os.path.join(os.environ['_MEIPASS2'], filename)

def create_course(hole_number):
    pass

#DO NOT TOUCH - IS FRAGILE
def create_course_entry(window, course, course_data, entry_data):
    #Need this to check against user entry
    number_of_holes = 0
    for i in range(len(course_data)):
        if course_data[i]["course"] == course:
            number_of_holes = len(course_data[i]["par"])

    entry_data = entry_data.split(",")
    #Fancy as fuck please appreciate my list comprehension
    entry_data = [int(score) for score in entry_data]
    #TELL THEM THEY PUT THE WRONG NUMBER OF FUCKING SCORES.  I D I O T S
    if len(entry_data) != number_of_holes:
        messagebox.showerror("Error", "Wrong number of holes input for course: {0}".format(course))
    else:
        #MMM WRITE THAT FUCKIN DATA MMMMMM
        with open(filename, "w") as file_:
            for i in range(len(course_data)):
                if course_data[i]["course"] == course:
                    course_data[i]["scores"].append(entry_data)
            json.dump(course_data, file_)

def view_score(course):
    pass
        



    

    
