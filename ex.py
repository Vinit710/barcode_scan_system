import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
import csv
import random

def create_app_window(user_name):
    app_window = tk.Tk()
    app_window.title("Student Login System")
    app_window.state('zoomed')

    # Function to handle saving data to CSV
    def save_to_csv(name, class_, roll_no, pnr_no, phone_no):
        with open("details.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, class_, roll_no, pnr_no, phone_no])
        messagebox.showinfo("Success", "Profile Updated Successfully!")

    # Function to handle Update Profile button click
    def update_profile():
        # Clear previous profile update frame if exists
        clear_frame()
        
        # Create frame for update profile details
        update_frame = tk.Frame(main_content_frame, bg="#ecf0f1")
        update_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Title label
        title_label = tk.Label(update_frame, text="UPDATE PROFILE", font=("Arial", 16, "bold"), bg="#ecf0f1")
        title_label.grid(row=0, columnspan=2, pady=10)

        # Input fields
        tk.Label(update_frame, text="Name:", bg="#ecf0f1").grid(row=1, column=0, sticky="w")
        name_entry = tk.Entry(update_frame)
        name_entry.grid(row=1, column=1, padx=10)
        tk.Label(update_frame, text="Class:", bg="#ecf0f1").grid(row=2, column=0, sticky="w")
        class_entry = tk.Entry(update_frame)
        class_entry.grid(row=2, column=1, padx=10)
        tk.Label(update_frame, text="Roll No:", bg="#ecf0f1").grid(row=3, column=0, sticky="w")
        roll_no_entry = tk.Entry(update_frame)
        roll_no_entry.grid(row=3, column=1, padx=10)
        tk.Label(update_frame, text="PNR No:", bg="#ecf0f1").grid(row=4, column=0, sticky="w")
        pnr_no_entry = tk.Entry(update_frame)
        pnr_no_entry.grid(row=4, column=1, padx=10)
        tk.Label(update_frame, text="Phone No:", bg="#ecf0f1").grid(row=5, column=0, sticky="w")
        phone_no_entry = tk.Entry(update_frame)
        phone_no_entry.grid(row=5, column=1, padx=10)

        # Save button
        def save_profile():
            name = name_entry.get()
            class_ = class_entry.get()
            roll_no = roll_no_entry.get()
            pnr_no = pnr_no_entry.get()
            phone_no = phone_no_entry.get()
            if name and class_ and roll_no and pnr_no and phone_no:
                save_to_csv(name, class_, roll_no, pnr_no, phone_no)
                update_frame.destroy()
            else:
                messagebox.showwarning("Incomplete Data", "Please fill in all fields.")

        save_button = tk.Button(update_frame, text="Save", font=("Arial", 12), bg="#3498db", fg="white", command=save_profile)
        save_button.grid(row=6, columnspan=2, pady=10)

    # Function to generate random marks for subjects
    def generate_random_marks():
        return random.randint(50, 100)  # Assuming maximum marks for each subject is 100

    # Function to calculate grade based on marks
    def calculate_grade(marks):
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"

    # Function to handle Result button click
    def show_result():
        # Clear previous frame if exists
        clear_frame()

        # Create frame for result section
        result_frame = tk.Frame(main_content_frame, bg="#ecf0f1")
        result_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Title label
        title_label = tk.Label(result_frame, text="YOUR RESULT", font=("Arial", 16, "bold"), bg="#ecf0f1")
        title_label.grid(row=0, columnspan=5, pady=10)

        # Labels for subjects
        subjects = ["DSA", "MATH", "ENGLISH", "OOP", "Software Engineering", "Elective"]
        tk.Label(result_frame, text="Subject", font=("Arial", 12, "bold"), bg="#ecf0f1").grid(row=1, column=0)
        tk.Label(result_frame, text="Total Marks", font=("Arial", 12, "bold"), bg="#ecf0f1").grid(row=1, column=1)
        tk.Label(result_frame, text="Gained Marks", font=("Arial", 12, "bold"), bg="#ecf0f1").grid(row=1, column=2)
        tk.Label(result_frame, text="Grade", font=("Arial", 12, "bold"), bg="#ecf0f1").grid(row=1, column=3)

        total_marks = 100  # Total marks for each subject
        total_gained_marks = 0

        # Display result for each subject
        for i, subject in enumerate(subjects, start=2):
            gained_marks = generate_random_marks()
            total_gained_marks += gained_marks
            grade = calculate_grade(gained_marks)

            tk.Label(result_frame, text=subject, font=("Arial", 12), bg="#ecf0f1").grid(row=i, column=0)
            tk.Label(result_frame, text=str(total_marks), font=("Arial", 12), bg="#ecf0f1").grid(row=i, column=1)
            tk.Label(result_frame, text=str(gained_marks), font=("Arial", 12), bg="#ecf0f1").grid(row=i, column=2)
            tk.Label(result_frame, text=grade, font=("Arial", 12), bg="#ecf0f1").grid(row=i, column=3)

        # Calculate percentage
        percentage = (total_gained_marks / (len(subjects) * total_marks)) * 100

        # Display percentage
        tk.Label(result_frame, text="Percentage:", font=("Arial", 12, "bold"), bg="#ecf0f1").grid(row=i+1, column=0)
        tk.Label(result_frame, text=f"{percentage:.2f}%", font=("Arial", 12), bg="#ecf0f1").grid(row=i+1, column=1, columnspan=3)

        # Function to generate random attended lectures
    def generate_random_attendance():
        return random.randint(0, 20)  # Assuming total lectures are 20

    # Function to calculate attendance percentage
    def calculate_attendance_percentage(attended_lectures):
        total_lectures = 20  # Assuming total lectures are 20
        percentage = (attended_lectures / total_lectures) * 100
        return percentage

    # Function to handle Attendance button click
    def show_attendance():
        # Clear previous frame if exists
        clear_frame()

        # Create frame for attendance section
        att_frame = tk.Frame(main_content_frame, bg="#ecf0f1")
        att_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Title label
        title_label = tk.Label(att_frame, text="ATTENDANCE", font=("Arial", 16, "bold"), bg="#ecf0f1")
        title_label.grid(row=0, columnspan=4, pady=10)

        # Labels for subjects
        subjects = ["DSA", "MATH", "ENGLISH", "OOP", "Software Engineering", "Elective"]
        tk.Label(att_frame, text="Subject", font=("Arial", 12, "bold"), bg="#ecf0f1").grid(row=1, column=0)
        tk.Label(att_frame, text="Total Lectures", font=("Arial", 12, "bold"), bg="#ecf0f1").grid(row=1, column=1)
        tk.Label(att_frame, text="Attended Lectures", font=("Arial", 12, "bold"), bg="#ecf0f1").grid(row=1, column=2)
        tk.Label(att_frame, text="Attendance Percentage", font=("Arial", 12, "bold"), bg="#ecf0f1").grid(row=1, column=3)

        # Display attendance for each subject
        for i, subject in enumerate(subjects, start=2):
            attended_lectures = generate_random_attendance()
            attendance_percentage = calculate_attendance_percentage(attended_lectures)

            tk.Label(att_frame, text=subject, font=("Arial", 12), bg="#ecf0f1").grid(row=i, column=0)
            tk.Label(att_frame, text="20", font=("Arial", 12), bg="#ecf0f1").grid(row=i, column=1)
            tk.Label(att_frame, text=str(attended_lectures), font=("Arial", 12), bg="#ecf0f1").grid(row=i, column=2)
            tk.Label(att_frame, text=f"{attendance_percentage:.2f}%", font=("Arial", 12), bg="#ecf0f1").grid(row=i, column=3)
    # Function to clear the frame
    def clear_frame():
        for widget in main_content_frame.winfo_children():
            widget.destroy()

    # --- Header Frame ---
    header_frame = tk.Frame(app_window, bg="#3498db")  
    header_frame.pack(fill=tk.X)

    # Welcome label
    welcome_label = tk.Label(header_frame, text=f"Welcome, {user_name}", 
                        font=("Arial", 18, "bold"),  
                        bg="#3498db", fg="white",  
                        pady=10)
    welcome_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

    # --- Options Bar Frame ---
    options_bar_frame = tk.Frame(app_window, bg="#2c3e50", width=int(app_window.winfo_screenwidth() * 0.2)) 
    options_bar_frame.pack(side=tk.LEFT, fill=tk.Y)  

    # Menu title label
    menu_label = tk.Label(options_bar_frame, text="Menu", font=("Arial", 14, "bold"), bg="#2c3e50", fg="white")
    menu_label.pack(pady=10)

    # Update profile button
    update_profile_button = tk.Button(options_bar_frame, text="Update Profile", font=("Arial", 12), bg="#2c3e50", fg="white", bd=0, command=update_profile)
    update_profile_button.pack(pady=5, padx=10, anchor=tk.W)

    # Other features button
    other_features_button = tk.Button(options_bar_frame, text="Other Features", font=("Arial", 12), bg="#2c3e50", fg="white", bd=0)
    other_features_button.pack(pady=5, padx=10, anchor=tk.W)

    # Result button
    result_button = tk.Button(options_bar_frame, text="Result", font=("Arial", 12), bg="#2c3e50", fg="white", bd=0, command=show_result)
    result_button.pack(pady=5, padx=10, anchor=tk.W)

    # Attendance button
    att_button = tk.Button(options_bar_frame, text="Attendance", font=("Arial", 12), bg="#2c3e50", fg="white", bd=0, command=show_attendance)
    att_button.pack(pady=5, padx=10, anchor=tk.W)

    # Logout button
    logout_button = tk.Button(options_bar_frame, text="Logout", font=("Arial", 12), bg="#2c3e50", fg="white", bd=0)
    logout_button.pack(pady=5, padx=10, anchor=tk.W)

    # --- Main Content Frame ---
    main_content_frame = tk.Frame(app_window, bg="#ecf0f1")  # Create main_content_frame here
    main_content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # --- Right Content Frame with Background Image ---
    right_content_frame = tk.Canvas(main_content_frame, bg="white", bd=0, highlightthickness=0)
    right_content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Load and blur the background image
    background_image = Image.open("clg.jpg")  # Change "clg.jpg" to your image file path
    blurred_background = background_image.filter(ImageFilter.GaussianBlur(radius=10))
    blurred_photo = ImageTk.PhotoImage(blurred_background)
    blurred_label = tk.Label(right_content_frame, image=blurred_photo)
    blurred_label.image = blurred_photo  # Keep reference to prevent garbage collection
    blurred_label.pack(fill=tk.BOTH, expand=True)

    return app_window   

# Example usage
create_app_window("John Doe").mainloop()
