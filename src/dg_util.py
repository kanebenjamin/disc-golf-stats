from errno import ENETRESET
from tkinter import *
import json
import os
from tkinter import messagebox
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import os

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
        messagebox.showinfo("Info", "Data successfully added for {0}!".format(course))
        
def view_score(course):
    objects = ["Ace", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "3+"]
    object_map = {"Ace": 0, "Eagle": 0, "Birdie": 0, "Par": 0, "Bogey": 0, "Double Bogey": 0, "3+": 0}
    with open(filename, "r") as file_:
        data = json.load(file_)
        for course_ in data:
            if course == course_["course"]:
                par_list = course_["par"]
                for score_list in course_["scores"]:
                    print("in score list for")
                    index = 0
                    for score in score_list:
                        result = score - par_list[index]
                        print(result)
                        if score == 1:
                            object_map["Ace"] += 1
                        elif score == -2:
                            object_map["Eagle"] += 1
                        elif result == -1:
                            object_map["Birdie"] += 1
                        elif result == 0:
                            object_map["Par"] += 1
                        elif result == 1:
                            object_map["Bogey"] += 1
                        elif result == 2:
                            object_map["Double Bogey"] += 1
                        elif result > 2:
                            object_map["3+"] += 1
                        index += 1
    
    y_pos = np.arange(len(objects))
    stats = [object_map["Ace"], object_map["Eagle"], object_map["Birdie"], object_map["Par"], object_map["Bogey"], object_map["Double Bogey"], object_map["3+"]]

    plt.barh(y_pos, stats, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel("Course Data")
    plt.title("{0} course stats".format(course))
    plt.show()
    
        



    

    
