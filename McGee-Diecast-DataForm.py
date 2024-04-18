#!/usr/bin/env python3

import tkinter
from tkinter import ttk
import csv
import os

FILENAME = "diecast_information.csv"

def read_data():
    diecasts = []
    with open(FILENAME, newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            first_name_entry.insert(0, row[0])
            last_name_entry.insert(0, row[1])
            team_name_entry.insert(0, row[2])



def write_data():
    firstName = first_name_entry.get()
    lastName = last_name_entry.get()
    teamName = team_name_entry.get()
    carYear = car_year_spinbox.get()
    carMake = car_make_combobox.get()
    carModel = car_model_entry.get()
    carNumber = car_number_entry.get()
    carSponsor = car_sponsor_entry.get()
    racedDiecast = raced_diecast_check.get()
    raceTrack = racetrack_info_entry.get()
    driverWin = win_check.get()

    with open('diecast_information.csv', 'r') as file:
        writer = csv.writer(file)
        writer.writerow(firstName, lastName, teamName, carYear, carMake, carModel, carNumber, carSponsor, racedDiecast, raceTrack, driverWin)

#TODO: Set this to a function.

window = tkinter.Tk()
window.title("McGee Diecast Data Form")

frame = tkinter.Frame(window)
frame.pack()

# Setting Initial Window Size
window.geometry("525x435")

# Window Icon Photo
icon = tkinter.PhotoImage(file="nascar_icon.png")
window.iconphoto(False, icon)

# Background image
bg = tkinter.PhotoImage(file = "daytona_background.png")
label1 = tkinter.Label(frame, image = bg)
label1.place(x=0,y=0)

# Saving Driver Info
driver_info_frame = tkinter.LabelFrame(frame, text="Driver Information")
driver_info_frame.grid(row=1, column=0, padx=20, pady=10)

# Driver and Team Name Labels
first_name_label = tkinter.Label(driver_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(driver_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
team_name_label = tkinter.Label(driver_info_frame, text="Team Name")
team_name_label.grid(row=0, column=2)

# Driver and Team Name Entry boxes
first_name_entry = tkinter.Entry(driver_info_frame)
last_name_entry = tkinter.Entry(driver_info_frame)
team_name_entry = tkinter.Entry(driver_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
team_name_entry.grid(row=1, column=2)

# Universal Padding for Driver Information Widget
for widget in driver_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Car Info
car_info_frame = tkinter.LabelFrame(frame, text="Car Information")
car_info_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# Car Year
car_year_label = tkinter.Label(car_info_frame, text="Year")
car_year_spinbox = tkinter.Spinbox(car_info_frame, from_=1947, to=2050)
car_year_label.grid(row=0,column=0)
car_year_spinbox.grid(row=1,column=0)

# Car Make
car_make_label = tkinter.Label(car_info_frame, text="Make")
car_make_combobox = ttk.Combobox(car_info_frame, values=["Buick", "Chevrolet", "Chrysler", "Dodge", "Ford", "Mercury","Oldsmobile", "Plymouth", "Pontiac", "Toyota"])
car_make_label.grid(row=0,column=1)
car_make_combobox.grid(row=1,column=1)

# Car Model 
car_model_label = tkinter.Label(car_info_frame, text="Model")
car_model_entry = tkinter.Entry(car_info_frame)
car_model_label.grid(row=0,column=2)
car_model_entry.grid(row=1,column=2)

# Car Number
car_number_label = tkinter.Label(car_info_frame, text="Number: ", justify=tkinter.RIGHT)
car_number_entry = tkinter.Entry(car_info_frame)
car_number_label.grid(row=2,column=0, sticky="e")
car_number_entry.grid(row=2,column=1, sticky="w")

# Primary Sponsor
car_sponsor_label = tkinter.Label(car_info_frame, text="Primary Sponsor:", justify=tkinter.RIGHT)
car_sponsor_entry = tkinter.Entry(car_info_frame)
car_sponsor_label.grid(row=3,column=0, sticky="e")
car_sponsor_entry.grid(row=3,column=1, sticky="w")

# Universal Padding for Car Information Widget
for widget in car_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Event Info
event_info_frame = tkinter.LabelFrame(frame, text="Event Info")
event_info_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Raced Diecast Checkbox
raced_diecast_check = tkinter.Checkbutton(event_info_frame, text="Is this a raced diecast?")
raced_diecast_check.grid(row=1,column=0)

# Race Track Information
racetrack_info_label = tkinter.Label(event_info_frame, text="Race Track")
racetrack_info_entry = tkinter.Entry(event_info_frame)
racetrack_info_label.grid(row=0,column=1)
racetrack_info_entry.grid(row=1,column=1)
# Driver Win Checkbox
win_check = tkinter.Checkbutton(event_info_frame, text="Did the driver win?")
win_check.grid(row=1,column=2)

# Universal Padding for Event Info Widget
for widget in event_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Frame for Buttons to allow them to share Column 0
buttons_frame = tkinter.LabelFrame(frame)
buttons_frame.grid(row=4,column=0, padx=20, pady=10)

# Add Diecast Button
add_button = tkinter.Button(buttons_frame, text="   Add Diecast   ")
add_button.grid(row=4,column=0)

# View Diecast Button
view_button = tkinter.Button(buttons_frame, text="   View Diecasts   ")
view_button.grid(row=4,column=1)

# Universal Padding for Buttons
for widget in buttons_frame.winfo_children():
    widget.grid_configure(padx=20, pady=5)

#if __name__ == "__main__":
#    window = tkinter.Tk()
#    window.title("McGee Diecast Data Form")
    # Setting Initial Window Size
    #TODO: Initialize the function
#    window.geometry("525x435")

window.mainloop()