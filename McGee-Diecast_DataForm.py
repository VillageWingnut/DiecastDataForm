#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox

FILENAME = "diecast_information.csv"


class DiecastDataForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("McGee Diecast Data Form")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Background image
        bg = tk.PhotoImage(file="daytona_background.png")
        label1 = tk.Label(self, image=bg)
        label1.image = bg  # Keeping reference to avoid back caching
        label1.place(x=0, y=0)

        # Window Icon Photo
        icon = tk.PhotoImage(file="nascar_icon.png")
        self.master.iconphoto(False, icon)

        # Saving Driver Info
        driver_info_frame = tk.LabelFrame(self, text="Driver Information")
        driver_info_frame.grid(row=1, column=0, padx=20, pady=10)

        # Driver and Team Name Labels
        first_name_label = tk.Label(driver_info_frame, text="First Name")
        first_name_label.grid(row=0, column=0)
        last_name_label = tk.Label(driver_info_frame, text="Last Name")
        last_name_label.grid(row=0, column=1)
        team_name_label = tk.Label(driver_info_frame, text="Team Name")
        team_name_label.grid(row=0, column=2)

        # Driver and Team Name Entry boxes
        self.first_name_entry = tk.Entry(driver_info_frame)
        self.last_name_entry = tk.Entry(driver_info_frame)
        self.team_name_entry = tk.Entry(driver_info_frame)
        self.first_name_entry.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)
        self.team_name_entry.grid(row=1, column=2)

        # Universal Padding for Driver Information Widget
        for widget in driver_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Saving Car Info
        car_info_frame = tk.LabelFrame(self, text="Car Information")
        car_info_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        # Car Year
        car_year_label = tk.Label(car_info_frame, text="Year")
        self.car_year_spinbox = tk.Spinbox(car_info_frame, from_=1947, to=2050)
        car_year_label.grid(row=0, column=0)
        self.car_year_spinbox.grid(row=1, column=0)

        # Car Make
        car_make_label = tk.Label(car_info_frame, text="Make")
        self.car_make_combobox = ttk.Combobox(car_info_frame, values=["Buick", "Chevrolet", "Chrysler", "Dodge", "Ford", "Mercury","Oldsmobile", "Plymouth", "Pontiac", "Toyota"])
        car_make_label.grid(row=0, column=1)
        self.car_make_combobox.grid(row=1, column=1)

        # Car Model 
        car_model_label = tk.Label(car_info_frame, text="Model")
        self.car_model_entry = tk.Entry(car_info_frame)
        car_model_label.grid(row=0, column=2)
        self.car_model_entry.grid(row=1, column=2)

        # Car Number
        car_number_label = tk.Label(car_info_frame, text="Number: ", justify=tk.RIGHT)
        self.car_number_entry = tk.Entry(car_info_frame)
        car_number_label.grid(row=2, column=0, sticky="e")
        self.car_number_entry.grid(row=2, column=1, sticky="w")

        # Primary Sponsor
        car_sponsor_label = tk.Label(car_info_frame, text="Primary Sponsor:", justify=tk.RIGHT)
        self.car_sponsor_entry = tk.Entry(car_info_frame)
        car_sponsor_label.grid(row=3, column=0, sticky="e")
        self.car_sponsor_entry.grid(row=3, column=1, sticky="w")

        # Universal Padding for Car Information Widget
        for widget in car_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Saving Event Info
        event_info_frame = tk.LabelFrame(self, text="Event Info")
        event_info_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

        # Raced Diecast Checkbox
        self.raced_diecast_var = tk.BooleanVar()
        raced_diecast_check = tk.Checkbutton(event_info_frame, text="Is this a raced diecast?", variable=self.raced_diecast_var)
        raced_diecast_check.grid(row=1, column=0)

        # Race Track Information
        racetrack_info_label = tk.Label(event_info_frame, text="Race Track")
        self.racetrack_info_entry = tk.Entry(event_info_frame)
        racetrack_info_label.grid(row=0, column=1)
        self.racetrack_info_entry.grid(row=1, column=1)

        # Driver Win Checkbox
        self.driver_win_var = tk.BooleanVar()
        win_check = tk.Checkbutton(event_info_frame, text="Did the driver win?", variable=self.driver_win_var)
        win_check.grid(row=1, column=2)

        # Universal Padding for Event Info Widget
        for widget in event_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Frame for Buttons to allow them to share Column 0
        buttons_frame = tk.LabelFrame(self)
        buttons_frame.grid(row=4, column=0, padx=20, pady=10)

        # Add Diecast Button
        add_button = tk.Button(buttons_frame, text="   Add Diecast   ", command=self.write_data)
        add_button.grid(row=4, column=0)

        # View Diecast Button
        view_button = tk.Button(buttons_frame, text="   View Diecasts   ", command=self.read_data)
        view_button.grid(row=4, column=1)

        # Universal Padding for Buttons
        for widget in buttons_frame.winfo_children():
            widget.grid_configure(padx=20, pady=5)
            
    def clear_entry_fields(self):
        # Clear each entry field individually
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.team_name_entry.delete(0, tk.END)
        self.car_year_spinbox.delete(0, tk.END)
        self.car_make_combobox.set("")  # Clear combobox selection
        self.car_model_entry.delete(0, tk.END)
        self.car_number_entry.delete(0, tk.END)
        self.car_sponsor_entry.delete(0, tk.END)
        self.racetrack_info_entry.delete(0, tk.END)
        self.raced_diecast_var.set(False)  # Deselect the checkbox
        self.driver_win_var.set(False)  # Deselect the checkbox

    def write_data(self):
        firstName = self.first_name_entry.get()
        lastName = self.last_name_entry.get()
        teamName = self.team_name_entry.get()
        carYear = self.car_year_spinbox.get()
        carMake = self.car_make_combobox.get()
        carModel = self.car_model_entry.get()
        carNumber = self.car_number_entry.get()
        carSponsor = self.car_sponsor_entry.get()
        racedDiecast = "Yes" if self.raced_diecast_var.get() else "No"
        raceTrack = self.racetrack_info_entry.get()
        driverWin = "Yes" if self.driver_win_var.get() else "No"

        try:
            with open(FILENAME, 'a', newline="") as file:
                writer = csv.writer(file)
                writer.writerow([firstName, lastName, teamName, carYear, carMake, carModel, carNumber, carSponsor, racedDiecast, raceTrack, driverWin])
                
                messagebox.showinfo("Success", "Data submitted successfully")
                
                 # Clear Entries
                self.clear_entry_fields()  # Call a method to clear entry fields
                
        except Exception as e:
            messagebox.showerror("Error", f"Unable to submit data: {e}")
            
    def read_data(self):
        self.diecasts = []
        self.current_diecast=0
        file="diecast_information.csv"
        try:
            with open(file, mode='r', newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    self.diecasts.append(row)
                    print(','.join(row)) # Delimiter
            self.view_diecasts(self)            
        except Exception as f:
            print(f"Unable to open CSV file: {f}")

    def view_diecasts(self, diecast):
        if self.diecasts:
            diecast = self.diecasts[self.current_diecast]

            window = tk.Toplevel(self)
            window.title("Diecasts")
            window.geometry("500x350")
            
            self.topLevel = window
            
            # Window Icon Photo
            icon = tk.PhotoImage(file="nascar_icon.png")
            window.iconphoto(False, icon)
            
            # Background image for popup window
            bg2 = tk.PhotoImage(file="harvick_michigan_burnout.png")
            label2 = tk.Label(window, image=bg2)
            label2.image = bg2  # Keeping reference to avoid back caching
            label2.place(x=0, y=0)

            pop_up_frame = tk.LabelFrame(window, pady=10)
            pop_up_frame.pack()
            
            ttk.Label(pop_up_frame, text="First Name:").grid(row=0, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[0], state="readonly").grid(row=0, column=1)

            ttk.Label(pop_up_frame, text="Last Name:").grid(row=1, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[1], state="readonly").grid(row=1, column=1)

            ttk.Label(pop_up_frame, text="Team Name:").grid(row=2, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[2], state="readonly").grid(row=2, column=1)

            ttk.Label(pop_up_frame, text="Car Year:").grid(row=3, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[3], state="readonly").grid(row=3, column=1)

            ttk.Label(pop_up_frame, text="Car Make:").grid(row=4, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[4], state="readonly").grid(row=4, column=1)

            ttk.Label(pop_up_frame, text="Car Model:").grid(row=5, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[5], state="readonly").grid(row=5, column=1)

            ttk.Label(pop_up_frame, text="Car Number:").grid(row=6, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[6], state="readonly").grid(row=6, column=1)
            
            ttk.Label(pop_up_frame, text="Car Sponsor:").grid(row=7, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[7], state="readonly").grid(row=7, column=1)
            
            ttk.Label(pop_up_frame, text="Raced Diecast:").grid(row=8, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[8], state="readonly").grid(row=8, column=1)
            
            ttk.Label(pop_up_frame, text="Racetrack:").grid(row=9, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[9], state="readonly").grid(row=9, column=1)
            
            ttk.Label(pop_up_frame, text="Was it a win?").grid(row=10, column=0, sticky=tk.W)
            ttk.Label(pop_up_frame, text=diecast[10], state="readonly").grid(row=10, column=1)

            ttk.Button(pop_up_frame, text="Next", command=self.load_next).grid(row=11, column=1, pady=10)
            ttk.Button(pop_up_frame, text="Back", command=self.load_previous).grid(row=11, column=0, pady=10)
        else:
            messagebox.showinfo("No entries", "There are no entries to display")
        
    def load_next(self):
        if self.current_diecast < len(self.diecasts) - 1:
            self.current_diecast += 1
            if self.topLevel:
                self.topLevel.destroy()
            self.view_diecasts(self.diecasts[self.current_diecast])
        else:
            messagebox.showinfo("End of Data", "No more diecasts to display.")

    def load_previous(self):
        if self.current_diecast > 0:
            self.current_diecast -= 1
            if self.topLevel:
                self.topLevel.destroy()
            self.view_diecasts(self.diecasts[self.current_diecast])
        else:
            messagebox.showinfo("Beginning of Data", "Already at the first diecast.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiecastDataForm(master=root)
    app.mainloop()