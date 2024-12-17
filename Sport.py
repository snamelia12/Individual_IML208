import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Global variable for keeping track of booking
bookings = []  # List to store bookings

# Function to create a new booking
def create_booking():
    name = name_var.get()
    phone = phone_var.get()
    booking_date = booking_date_var.get()
    sport = sport_var.get()
    court = court_var.get()
    time_slot = time_slot_var.get()

    # Validate that all fields are filled
    if not name or not phone or not booking_date or not sport or not court or not time_slot:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    # Add the booking to the list
    booking = {
        "name": name,
        "phone": phone,
        "booking_date": booking_date,
        "sport": sport,
        "court": f"Court {court}",
        "time": time_slot
    }
    bookings.append(booking)
    messagebox.showinfo("Success", f"Your {sport} session at {court} has been booked at {time_slot}.")

# Function to view all bookings (Read)
def view_bookings():
    if not bookings:
        messagebox.showinfo("No Bookings", "No bookings found.")
        return

    bookings_text = "Current Bookings:\n"
    for i, booking in enumerate(bookings, 1):
        bookings_text += f"{i}. {booking['sport']} - {booking['court']} at {booking['time']}\n"
        bookings_text += f"   Name: {booking['name']}, Phone: {booking['phone']}, Date: {booking['booking_date']}\n"
    
    messagebox.showinfo("Bookings", bookings_text)

# Function to update a booking
def update_booking():
    view_bookings()  # View bookings before updating
    
    booking_number = int(booking_number_var.get()) - 1
    if 0 <= booking_number < len(bookings):
        # Get the selected booking
        booking = bookings[booking_number]
        
        # Update details
        new_sport = sport_var.get()
        new_court = court_var.get()
        new_time_slot = time_slot_var.get()

        if new_sport:
            booking["sport"] = new_sport
        if new_court:
            booking["court"] = f"Court {new_court}"
        if new_time_slot:
            booking["time"] = new_time_slot
        
        messagebox.showinfo("Success", "Booking updated successfully!")
    else:
        messagebox.showerror("Error", "Invalid booking number!")

# Function to delete a booking
def delete_booking():
    view_bookings()  # View bookings before deleting
    
    booking_number = int(booking_number_var.get()) - 1
    if 0 <= booking_number < len(bookings):
        del bookings[booking_number]
        messagebox.showinfo("Success", "Booking deleted successfully!")
    else:
        messagebox.showerror("Error", "Invalid booking number!")

# GUI Setup
root = tk.Tk()
root.title("Sports Booking System")
root.geometry("400x650")

# Labels and Entry Fields for Booking Details
tk.Label(root, text="Enter Your Name").pack(pady=5)
name_var = tk.StringVar()
tk.Entry(root, textvariable=name_var).pack(pady=5)

tk.Label(root, text="Enter Phone Number").pack(pady=5)
phone_var = tk.StringVar()
tk.Entry(root, textvariable=phone_var).pack(pady=5)

tk.Label(root, text="Enter Date of Booking (YYYY-MM-DD)").pack(pady=5)
booking_date_var = tk.StringVar()
tk.Entry(root, textvariable=booking_date_var).pack(pady=5)

tk.Label(root, text="Select Sport").pack(pady=5)
sport_var = tk.StringVar()
tk.OptionMenu(root, sport_var, "Tennis", "Badminton", "Squash").pack(pady=5)

tk.Label(root, text="Select Court").pack(pady=5)
court_var = tk.StringVar()
tk.OptionMenu(root, court_var, "1", "2", "3").pack(pady=5)

tk.Label(root, text="Select Time Slot").pack(pady=5)
time_slot_var = tk.StringVar()
tk.OptionMenu(root, time_slot_var, "9:00 AM - 11:00 AM", "11:30 AM - 2:30 PM", "2:00 PM - 5:00 PM", "4:30 PM - 6:30 PM").pack(pady=5)

# Buttons for CRUD operations
tk.Button(root, text="Create Booking", command=create_booking).pack(pady=5)
tk.Button(root, text="View Bookings", command=view_bookings).pack(pady=5)

tk.Label(root, text="Enter Booking Number to Update/Delete").pack(pady=5)
booking_number_var = tk.StringVar()
tk.Entry(root, textvariable=booking_number_var).pack(pady=5)

tk.Button(root, text="Update Booking", command=update_booking).pack(pady=5)
tk.Button(root, text="Delete Booking", command=delete_booking).pack(pady=5)

# Start the GUI loop
root.mainloop()
