#!/usr/bin/env python3

import tkinter
from tkinter import ttk
from tkinter import messagebox
import csv

class DiecastEntryForm(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.pack()

        # Defining Variables for Entry Fields
        # Driver Info
        self.firstName = tkinter.StringVar()
        self.lastName = tkinter.StringVar()
        self.teamName = tkinter.StringVar()

        # Car Info
        # Spinbox
        self.carYear = tkinter.StringVar()
        # Combobox
        self.carMake = tkinter.StringVar()

        self.carModel = tkinter.StringVar()
        self.carNumber = tkinter.StringVar()
        self.carSponsor = tkinter.StringVar()
        # Event Info
        # Checkbox
        self.racedDiecast = tkinter.StringVar()

        self.raceTrack = tkinter.StringVar()
        # Checkbox
        self.driverWin = tkinter.StringVar()


        # Window Icon Photo
        icon = tkinter.PhotoImage(file="nascar_icon.png")
        window.iconphoto(False, icon)

        # Background image
        bg = tkinter.PhotoImage(file = "daytona_background.png")
        self.label1 = tkinter.Label(self, image = bg)
        self.label1.place(x=0,y=0)

        # Saving Driver Info
        driver_info_frame = tkinter.LabelFrame(self, text="Driver Information")
        driver_info_frame.grid(row=1, column=0, padx=20, pady=10)

        # Driver and Team Name Labels
        first_name_label = tkinter.Label(driver_info_frame, text="First Name")
        first_name_label.grid(row=0, column=0)
        last_name_label = tkinter.Label(driver_info_frame, text="Last Name")
        last_name_label.grid(row=0, column=1)
        team_name_label = tkinter.Label(driver_info_frame, text="Team Name")
        team_name_label.grid(row=0, column=2)

        # Driver and Team Name Entry boxes
        first_name_entry = tkinter.Entry(driver_info_frame, textvariable=self.firstName)
        last_name_entry = tkinter.Entry(driver_info_frame, textvariable=self.lastName)
        team_name_entry = tkinter.Entry(driver_info_frame, textvariable=self.teamName)
        first_name_entry.grid(row=1, column=0)
        last_name_entry.grid(row=1, column=1)
        team_name_entry.grid(row=1, column=2)

        # Universal Padding for Driver Information Widget
        for widget in driver_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Saving Car Info
        car_info_frame = tkinter.LabelFrame(self, text="Car Information")
        car_info_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        # Car Year
        car_year_label = tkinter.Label(car_info_frame, text="Year")
        car_year_spinbox = tkinter.Spinbox(car_info_frame, from_=1947, to=2050, textvariable=self.carYear)
        car_year_label.grid(row=0,column=0)
        car_year_spinbox.grid(row=1,column=0)

        # Car Make
        car_make_label = tkinter.Label(car_info_frame, text="Make")
        car_make_combobox = ttk.Combobox(car_info_frame, values=["Buick", "Chevrolet", "Chrysler", "Dodge", "Ford", "Mercury","Oldsmobile", "Plymouth", "Pontiac", "Toyota"], textvariable=self.carMake)
        car_make_label.grid(row=0,column=1)
        car_make_combobox.grid(row=1,column=1)

        # Car Model 
        car_model_label = tkinter.Label(car_info_frame, text="Model")
        car_model_entry = tkinter.Entry(car_info_frame, textvariable=self.carModel)
        car_model_label.grid(row=0,column=2)
        car_model_entry.grid(row=1,column=2)

        # Car Number
        car_number_label = tkinter.Label(car_info_frame, text="Number: ", justify=tkinter.RIGHT)
        car_number_entry = tkinter.Entry(car_info_frame, textvariable=self.carNumber)
        car_number_label.grid(row=2,column=0, sticky="e")
        car_number_entry.grid(row=2,column=1, sticky="w")

        # Primary Sponsor
        car_sponsor_label = tkinter.Label(car_info_frame, text="Primary Sponsor:", justify=tkinter.RIGHT)
        car_sponsor_entry = tkinter.Entry(car_info_frame, textvariable=self.carSponsor)
        car_sponsor_label.grid(row=3,column=0, sticky="e")
        car_sponsor_entry.grid(row=3,column=1, sticky="w")

        # Universal Padding for Car Information Widget
        for widget in car_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Saving Event Info
        event_info_frame = tkinter.LabelFrame(self, text="Event Info")
        event_info_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

        # Raced Diecast Checkbox
        raced_var = tkinter.StringVar(value="Not Raced")
        raced_diecast_check = tkinter.Checkbutton(event_info_frame, text="Is this a raced diecast?", variable=raced_var, onvalue="Raced", offvalue="Not Raced")
        raced_diecast_check.grid(row=1,column=0)

        # Race Track Information
        racetrack_info_label = tkinter.Label(event_info_frame, text="Race Track")
        racetrack_info_entry = tkinter.Entry(event_info_frame, textvariable=self.raceTrack)
        racetrack_info_label.grid(row=0,column=1)
        racetrack_info_entry.grid(row=1,column=1)
        # Driver Win Checkbox
        win_var = tkinter.StringVar(value="Did not win")
        win_check = tkinter.Checkbutton(event_info_frame, text="Did the driver win?", variable=win_var, onvalue="Won race!", offvalue="Did not win race.")
        win_check.grid(row=1,column=2)

        # Universal Padding for Event Info Widget
        for widget in event_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Frame for Buttons to allow them to share Column 0
        buttons_frame = tkinter.LabelFrame(self)
        buttons_frame.grid(row=4,column=0, padx=20, pady=10)

        # Add Diecast Button
        add_button = tkinter.Button(buttons_frame, text="   Add Diecast   ", command=self.write_data)
        add_button.grid(row=4,column=0)

        # View Diecast Button
        view_button = tkinter.Button(buttons_frame, text="   View Diecasts   ")
        view_button.grid(row=4,column=1)

        # Universal Padding for Buttons
        for widget in buttons_frame.winfo_children():
            widget.grid_configure(padx=20, pady=5)

# ---------------------------------------- #

    file = "diecast_information.csv"

    # Check for field completion
    def check_complete(self):
        if self.firstName.get() == "" or self.lastName.get() =="" or self.teamName.get() =="" or self.carYear.get() =="" or self.carMake.get()=="" or self.carModel.get()=="" or self.carNumber.get()=="" or self.carSponsor.get():
            messagebox.showerror("Error", "Please complete required entries")
            return
        # 

    def write_data(self):
        diecasts = [
        self.firstName.get(),
        self.lastName.get(),
        self.teamName.get(),
        self.carYear.get(),
        self.carMake.get(),
        self.carModel.get(),
        self.carNumber.get(),
        self.carSponsor.get(),
        self.racedDiecast.get(),
        self.raceTrack.get(),
        self.driverWin.get(),
        ]
        try:
            with open('diecast_information.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(diecasts)
        
            messagebox.showinfo("Success", "Data submitted successfully")

            # Clear Text Entry Boxes
            self.firstName.set("")
            self.lastName.set("")
            self.teamName.set("")
            self.carYear.set("")
            self.carMake.set("")
            self.carModel.set("")
            self.carNumber.set("")
            self.carSponsor.set("")
            self.racedDiecast.set("")
            self.raceTrack.set("")
            self.driverWin.set("")

        except Exception as e:
            messagebox.showerror("Error", f"Unable to submit data: {e}")

if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("McGee Diecast Data Form")
    window.geometry("525x435")
    DiecastEntryForm(window)
    window.mainloop()