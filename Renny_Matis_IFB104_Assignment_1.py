
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 12056081
student_name   = 'Renny Matis'
#
#  NB: All files submitted for this assessable task will be subjected
#  to automated plagiarism analysis using a tool such as the Measure
#  of Software Similarity (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the online video instructions for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts
#  and you will submit your final solution as this single Python 3
#  file only, whether or not you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
config_file = 'assignment_1_config.py'
if isfile(config_file):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print(f"\nCannot find file '{config_file}', aborting!\n")
    abort()

# Define the function for generating data sets in Task 1B,
# using the imported raw data generation function if available,
# but otherwise creating a dummy function that just returns an
# empty list
data_file = 'assignment_1_data.py'
if isfile(data_file):
    print('Data generation module found ...\n')
    from assignment_1_data import raw_data
    def data_set(new_seed = randint(0, 99999)):
        return raw_data(new_seed) # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.
#

# All of your code goes in, or is called from, this function.
# In Task 1B ensure that your code does NOT call functions data_set
# or raw_data because they're already called in the main program
# below.


def visualise_data(report_list):

    tracer(False)

    # Define necessary variables
    
    size_of_frame = 79
    leg_width = 4
    leg_size = 26

    cow_body_height = 30
    cow_body_width = 50
 
    radius_of_head = 16
    radius_of_ears = 8
    radius_of_eyes = 6

    diameter_of_head = 32

    min_blob_size = 8
    max_blob_size = 16

    # Speed up the turtle

    speed('fastest')

    # Move the turtle to the lefthand side of the screen to draw a positive cow

    def positive_cow_movement():
        left(90)
        forward(250)
        right(90)
        forward(-560)

    # Draw a positive Cow demonstration
    def positive_background(frame_size):
        pendown()
        width(1)
        pencolor('black')
        fillcolor('green')
        begin_fill()
        forward(size_of_frame)
        right(90)
        forward(size_of_frame)
        right(90)
        forward(size_of_frame)
        right(90)
        forward(size_of_frame)
        end_fill()       
        penup()
        right(180)
        forward(size_of_frame * 1.5)

    # Write the text for a positive cow demonstration
    def positive_text():
        write('Beef sales \nare high!', move = False, align = 'left', font = ('Arial', 12))

        #  Move to location and draw a positive cow

    def fix_location_positive():
        right(180)
        forward(size_of_frame - 10)
        right(90)
        forward(size_of_frame // 2)
        left(90)

        # Draw a positive Cow

    def cow_legs():
        color('white')
        width(leg_width)
        pendown()
        left(180)
        circle(leg_size, size_of_frame)
        penup()
        circle(leg_size, -size_of_frame)
        left(90)
        pendown()
        right(60)
        circle(leg_size, size_of_frame)
        penup()
        circle(leg_size, -size_of_frame)
        left(90)
        pendown()
        right(120)
        circle(leg_size, -size_of_frame)
        penup()
        circle(leg_size, size_of_frame)
        right(120)
        pendown()
        left(90)
        circle(leg_size, -size_of_frame)
        penup()
        circle(leg_size, size_of_frame)
        right(120)

        # Move to location to draw body of the cow

        pendown()
        right(120)
        forward(10)

        # Draw the body of the positive cow

    def cow_body(cow_height, cow_width):
        right(90)
        forward(leg_size)
        pendown()
        begin_fill()
        right(90)
        forward(cow_body_height)
        right(90)
        forward(cow_body_width)
        right(90)
        forward(cow_body_height)
        right(90)
        forward(cow_body_width)
        end_fill()
        penup()
        right(90)
        forward(cow_body_height // 2)
        right(90)

        # Move to location of cow head

        penup()
        left(90)
        forward(cow_body_height // 2)
        right(90)
        forward(cow_body_width)

        # Draw the head
    def cow_head(head_radius, ears_radius):
        dot(diameter_of_head, 'black')
        left(90)
        forward(radius_of_head // 2)
        left(90)
        forward(radius_of_head)
        dot(radius_of_head, 'black')
        dot(radius_of_ears, 'tan')
        right(180)
        forward(diameter_of_head)
        dot(radius_of_head, 'black')
        dot(radius_of_ears, 'tan')
        left(180)
        forward(radius_of_head)
        left(90)
        forward(radius_of_head + (radius_of_head // 5))
        dot(radius_of_ears * 1.5, 'tan')
        right(90)
        forward(radius_of_ears // 2)
        dot(radius_of_ears // 2, 'black')
        right(180)
        forward(radius_of_ears)
        dot(radius_of_ears // 2, 'black')
        left(180)
        forward(radius_of_ears // 2)
        right(90)
        forward(radius_of_head)
        right(90)
        forward(radius_of_head // 3)
        dot(radius_of_eyes, 'white')
        dot(radius_of_eyes // 2, 'black')
        right(180)
        forward(radius_of_head // 2)
        dot(radius_of_eyes, 'white')
        dot(radius_of_eyes // 2, 'black')

        # Move to the back of cow to add blobs

        left(90)
        forward(cow_body_height // 1.5)
        right(90)
        forward(cow_body_width)
        right(180)

        # Add blobs to cow body

    def cowblobs():
        for cow_blobs in range(4):
            color('black')
            forward(cow_body_width // 5)
            dot(randint(min_blob_size, max_blob_size))
        

        # Move to the next location to draw the next Cow demonstration

    def normal_cow_movement():
        left(90)
        forward((size_of_frame // 2) - 5)
        left(90)
        forward(size_of_frame * 1.5)
        left(90)

        # Draw a standard Cow demonstration

    def normal_background(frame_size):
        pendown()
        width(1)
        pencolor('black')
        fillcolor('yellow')
        begin_fill()
        forward(size_of_frame)
        right(90)
        forward(size_of_frame)
        right(90)
        forward(size_of_frame)
        right(90)
        forward(size_of_frame)
        end_fill()
        penup()
        right(180)
        forward(size_of_frame * 1.5)
        
    # Write the text for a standard cow demonstration
    def normal_text():
        write('Beef is just\nbreaking even', move = False, align = 'left', font = ('Arial', 12))

        # Move to location within standard Cow demonstration to draw a normal Cow and orientate the cow

    def fix_location_normal():
        right(180)
        forward(size_of_frame)
        right(90)
        forward((size_of_frame // 2) - 10)

    def negative_cow_movement():
        right(90)
        forward((size_of_frame // 2) + 6)
        right(90)
        forward(size_of_frame // 2)
        left(90)
        forward(size_of_frame)
        left(90)
        

    def negative_background(frame_size):
        pendown()
        width(1)
        pencolor('black')
        fillcolor('orange')
        begin_fill()
        forward(size_of_frame)
        right(90)
        forward(size_of_frame)
        right(90)
        forward(size_of_frame)
        right(90)
        forward(size_of_frame)
        end_fill()
        penup()
        right(180)
        forward((size_of_frame * 1.5) + 0.5)
        
    # Write the text for a negative cow demonstration
    def negative_text():
        write('Beef is in \na slump', move = False, align = 'left', font = ('Arial', 12))

        # move the cow back to a position where it can be drawn representing a negative model

    def fix_location_negative():
        left(180)
        forward(size_of_frame + 10)
        right(90)
        forward(size_of_frame // 2)
        right(90)


 # Call commands to create the image

    positive_cow_movement()
    positive_background(size_of_frame)
    positive_text()
    fix_location_positive()
    cow_legs()
    cow_body(cow_body_height, cow_body_width)
    cow_head(radius_of_head, radius_of_ears)
    cowblobs()
    normal_cow_movement()
    normal_background(size_of_frame)
    normal_text()
    fix_location_normal()
    cow_legs()
    cow_body(cow_body_height, cow_body_width)
    cow_head(radius_of_head, radius_of_ears)
    cowblobs()
    negative_cow_movement()
    negative_background(size_of_frame)
    negative_text()
    fix_location_negative()
    cow_legs()
    cow_body(cow_body_height, cow_body_width)
    cow_head(radius_of_head, radius_of_ears)
    cowblobs()

# Part B code begins below

# find the bottom left corner of the grid, and move the turtle vertically by four cell_size lengths (+1 is to adjust for turtle offset error) in order to reach the top left corner of initial 0 grid

    left_edge_config = grid_offset - ((grid_width * cell_size) // 2)
    bottom_edge_config = -(grid_height * cell_size) // 2
    goto(left_edge_config, bottom_edge_config)
    setheading(90)
    forward((cell_size * 4) + 1)
    setheading(0)
    
# Uncomment code below in order to use the print function to find the Y coordinate for all 12 months, and the two for loops which print the X coordinates of all 12 months

##    print(int(ycor()))
##    for Find_Month_Coordinates in range(6):
##        print(int(xcor()))
##        forward(cell_size)
    # second for loop is included to resolve error in coordinates by using forward with turtle (error reduces cell_size by 1 and offsets the month locations, +1 resolves this)
##    for Find_Month_Coordinates in range(5):
##        forward(cell_size)
##        print(int(xcor() + 1))


# Write necessary variables

    # Y coordinates for every month is 40 as that is where the top left corner of initial 0 grid starts
    Month_Ycor = 40

    # X coordinates for every month is found using the two Find_Month_Coordinates for loops
    January_Xcor = -400
    February_Xcor = -320
    March_Xcor = -240
    April_Xcor = -160
    May_Xcor = -80
    June_Xcor = 0
    July_Xcor = 80
    August_Xcor = 160
    September_Xcor = 240
    October_Xcor = 320
    November_Xcor = 400
    December_Xcor = 480

# Access list of data with a for loop  

    for monthly_report in report_list:
        Which_Month, Month_Value = monthly_report

# Create a function that decides which cow is necessary to be drawn based on the Month_Value in the report_list (dataset)
            
        def Which_Cow_To_Draw():
                #Draw a positive cow if the Month_Value is above 0 (therefore a positive number)  
                if Month_Value > 0 and Month_Value <= 3:
                    for Amount_Of_Cows_Pos in range(Month_Value + 1):
                        positive_background(size_of_frame)
                        fix_location_positive()
                        cow_legs()
                        cow_body(cow_body_height, cow_body_width)
                        cow_head(radius_of_head, radius_of_ears)
                        cowblobs()
                        # Reposition the turtle to the top left corner of the month's grid, in addition to moving up one grid everytime a positive cow is drawn
                        setheading(180)
                        forward(34)
                        setheading(90)
                        forward(size_of_frame * 1.5)
                        right(90)
                # If the Month_Value surpasses 3, do not draw any additional cows and only draw 4 (maximum capacity on the chart)
                elif Month_Value > 3:
                    for Too_Many_Positive_Cows in range(4):
                        positive_background(size_of_frame)
                        fix_location_positive()
                        cow_legs()
                        cow_body(cow_body_height, cow_body_width)
                        cow_head(radius_of_head, radius_of_ears)
                        cowblobs()
                        # Reposition the turtle to the top left corner of the month's grid, in addition to moving up one grid everytime a positive cow is drawn
                        setheading(180)
                        forward(34)
                        setheading(90)
                        forward(size_of_frame * 1.5)
                        right(90)
                # Draw a negative cow if the Month_Value is less than 0 (therefore negative number) and equal to or bigger than -3
                elif 0 > Month_Value >= -3:
                    for Amount_Of_Cows_Neg in range(abs(Month_Value - 1)):
                        negative_background(size_of_frame)
                        fix_location_negative()
                        cow_legs()
                        cow_body(cow_body_height, cow_body_width)
                        cow_head(radius_of_head, radius_of_ears)
                        cowblobs()
                        setheading(180)
                        # Reposition the turtle to the top left corner of the month's grid, in addition to moving up one grid everytime a negative cow is drawn
                        forward(44)      
                        setheading(270)  
                        forward(size_of_frame // 2)  
                        left(90)
                # If the Month_Value is smaller than negative 3, do not draw any additional cows and only draw 4 (maximum capacity on the chart)
                elif -3 > Month_Value:
                    for Amount_Of_Cows_Neg in range(4):
                        negative_background(size_of_frame)
                        fix_location_negative()
                        cow_legs()
                        cow_body(cow_body_height, cow_body_width)
                        cow_head(radius_of_head, radius_of_ears)
                        cowblobs()
                        setheading(180)
                        # Reposition the turtle to the top left corner of the month's grid, in addition to moving up one grid everytime a negative cow is drawn
                        forward(44)      
                        setheading(270)  
                        forward(size_of_frame // 2)  
                        left(90)
                # Draw a single normal cow if the value is not above 0 or below 0 (therefore it must be 0)
                else:
                    pendown()
                    normal_background(size_of_frame)
                    fix_location_normal()
                    cow_legs()
                    cow_body(cow_body_height, cow_body_width)
                    cow_head(radius_of_head, radius_of_ears)
                    cowblobs()
                
            
        # if statements to check for what month it is, then go to the X coordinate for the month, and then use the function Which_Cow_To_Draw to draw the necessary cow     
        if Which_Month == 'January':
            goto(January_Xcor, Month_Ycor)
            Which_Cow_To_Draw()       
        elif Which_Month == 'February':
            goto(February_Xcor, Month_Ycor)
            Which_Cow_To_Draw() 
        elif Which_Month == 'March':
            goto(March_Xcor, Month_Ycor)
            Which_Cow_To_Draw()  
        elif Which_Month == 'April':
            goto(April_Xcor, Month_Ycor)
            Which_Cow_To_Draw()  
        elif Which_Month == 'May':
            goto(May_Xcor, Month_Ycor)
            Which_Cow_To_Draw()  
        elif Which_Month == 'June':
            goto(June_Xcor, Month_Ycor)
            Which_Cow_To_Draw()  
        elif Which_Month == 'July':
            goto(July_Xcor, Month_Ycor)
            Which_Cow_To_Draw()  
        elif Which_Month == 'August':
            goto(August_Xcor, Month_Ycor)
            Which_Cow_To_Draw()  
        elif Which_Month == 'September':
            goto(September_Xcor, Month_Ycor)
            Which_Cow_To_Draw()  
        elif Which_Month == 'October':
            goto(October_Xcor, Month_Ycor)
            Which_Cow_To_Draw()  
        elif Which_Month == 'November':
            goto(November_Xcor, Month_Ycor)
            Which_Cow_To_Draw()
        # December is the only month remaining so if it isn't the previous 11 months; it must be December
        else:
            goto(December_Xcor, Month_Ycor)
            Which_Cow_To_Draw() 

    # For loop to calculate the profits of Beef Sales, adding each month's Month_Value together to find the Total_Profit
    Total_Profit = 0
    for monthly_report in report_list:
        Total_Profit += monthly_report[1]


    # Go to bottom left of the program and write the Total_Profit calculation's result
    goto(left_edge_config, bottom_edge_config)
    setheading(180)
    forward(size_of_frame * 3)
    write(f"Total Profit ($bn): {Total_Profit}", move = False, align = 'left', font = ('Arial', 14))
    
#--------------------------------------------------------------------#



#-----Main Program to Run Student's Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
#
# ***** You can add arguments to this function call to modify
# ***** features of the drawing canvas such as the background
# ***** and line colours, etc
create_drawing_canvas(canvas_title = 'The Australian Beef Industry', write_instructions = False)
    

# Create the data set and pass it to the student's function
#
# ***** While developing your Task 1B code you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
#
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#
