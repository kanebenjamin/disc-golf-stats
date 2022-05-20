from tkinter import *

from matplotlib.pyplot import title
from dg_util import *
import os
"""
window = Tk()       
window.title('Track Ya Stats')
window.geometry("1200x900+10+20")

#Find data file:
filename = 'course_data.json' 
if '_MEIPASS2' in os.environ:
    filename = os.path.join(os.environ['_MEIPASS2'], filename)

#Create a Course GUI Elements
course_label = Label(window, text="Add a Course! Number of Holes: ", fg='black')
hole_number = Entry(window)
create_course_button = Button(window, text="Create Course", command= lambda: create_course(18))
course_label.grid(column=0,row=1)
hole_number.grid(column=1,row=1)
create_course_button.grid(column=2, row=1)

#Current Courses GUI
current_course_label = Label(window, text="Current courses saved: ", fg='black')
current_course_label.grid(column=0,row=3)
current_course_view_label = Label(window, text="LIST OF CURRENT COURSES PULLED FROM JSON FILE", fg='black')
current_course_view_label.grid(column=1,row=3)

#Refresh button:
create_course_button = Button(window, text="Refresh", command=refresh)
create_course_button.grid(column=0, row=10)

#See course stats:
course_stats_label = Label(window, text="Course Stats: ", fg='black')
course_stats_label.grid(column=0, row=4)
course_entry = Entry(window)
course_entry.grid(column=1, row=4)
course_stats_button = Button(window, text="See Stats", command= lambda: course_stats(course_entry.get()))
course_stats_button.grid(column=2,row=4)

#Add Course Data GUI Elements 
create_course_data_button = Button(window, text="Add Course Data", command= lambda: to_course_data_window(window))
create_course_data_button.grid(column=0,row=5)
####Course Data entry window


window.mainloop() """

###################################################################################

#Find data file:
filename = 'course_data.json' 
if '_MEIPASS2' in os.environ:
    filename = os.path.join(os.environ['_MEIPASS2'], filename)

LARGEFONT =("Verdana", 35)

class tkinterApp(Tk):
	
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        
        # __init__ function for class Tk
        Tk.__init__(self, *args, **kwargs)
        
        
        # creating a container
        container = Frame(self)
        self.geometry("1000x1000")
        self.title = "Disc Golf Tracker"
        container.pack(side = "top", fill = "both", expand = True)

        #container.grid_rowconfigure(0, weight = 1)
        #container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, CourseData, AddCourse):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startpage

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # label of frame Layout 2
        label = Label(self, text ="Disc Golf Stats", font = LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        button1 = Button(self, text ="Add Course",
        command = lambda : controller.show_frame(AddCourse))

        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 2, padx = 10, pady = 10)

        ## button to show frame 2 with text layout2
        button2 = Button(self, text ="See Course Data/Add Course Data",
        command = lambda : controller.show_frame(CourseData))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        #Create a Course GUI Elements
        course_label = Label(self, text="Add a Course! Number of Holes: ", fg='black')
        hole_number = Entry(self)
        course_label.grid(column=0,row=1)
        hole_number.grid(column=1,row=1)

        #Current Courses GUI
        current_course_label = Label(self, text="Current courses saved: ", fg='black')
        current_course_label.grid(column=0,row=3)
        current_course_view_label = Label(self, text="LIST OF CURRENT COURSES PULLED FROM JSON FILE", fg='black')
        current_course_view_label.grid(column=1,row=3)

		


# second window frame page1
class AddCourse(Frame):
	
    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)
        label = Label(self, text ="Add Course", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = Button(self, text ="Course Data Page",
                            command = lambda : controller.show_frame(CourseData))

        # putting the button in its place
        # by using grid
        button1.grid(row = 13, column = 1, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button2 = Button(self, text ="Back",
                            command = lambda : controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row = 14, column = 1, padx = 10, pady = 10)




# third window frame page2
class CourseData(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text ="Course Data", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = Button(self, text ="Add Course Page",
                            command = lambda : controller.show_frame(AddCourse))

        # putting the button in its place by
        # using grid
        button1.grid(row = 29, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text
        # layout3
        button2 = Button(self, text ="Back",
                            command = lambda : controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row =30, column = 1, padx = 10, pady = 10)

        label = Label(self, text="Select course: ")
        label.grid(column=0, row=2)
        
        courses_group = StringVar()
        #Open up the data
        with open(filename, "r") as file_:
            course_data = json.loads(file_.read())
        #Add courses to a list
        courses = []
        for course in course_data:
            courses.append(course["course"])
        #Make radio buttons for courses
        row = 2
        for i in range(len(courses)):
            if i > 3:
                row += 1
            Radiobutton(self, 
                text=courses[i],
                variable=courses_group, 
                value=courses[i]).grid(row=row,column=i+1)
        #Add Course Data
        entry_label = Label(self, text="Add Data: < 3,5,6,3,4 >JUST LIKE THAT (without < >). Put an 'X' for a hole not played.")
        entry_label.grid(column=0, row=5)
        entry_data = Entry(self)
        entry_data.grid(row=5,column=2)
        add_data = Button(self, text ="Add Data to Course",
                            command = lambda : create_course_entry(self, courses_group.get(), course_data, entry_data.get()))
        add_data.grid(row=5,column=3)

        #View the data
        view_data = Button(self, text="View Data for Course", command= lambda: view_score(courses_group.get()))
        view_data.grid(row=6, column=2)
        #TODO work on view_scores function with pandas library


# Driver Code
app = tkinterApp()
app.mainloop()
