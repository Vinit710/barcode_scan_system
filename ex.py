import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
import csv

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
        # Create a new window for updating profile details
        update_window = tk.Toplevel(app_window)
        update_window.title("Update Profile")

        # Create frame for update profile details
        update_frame = tk.Frame(update_window, bg="#ecf0f1")
        update_frame.pack(padx=20, pady=10)

        # Title label
        title_label = tk.Label(update_frame, text="UPDATE PROFILE", font=("Arial", 16, "bold"), bg="#ecf0f1")
        title_label.pack(pady=10)

        # Input fields
        tk.Label(update_frame, text="Name:", bg="#ecf0f1").pack(anchor=tk.W)
        name_entry = tk.Entry(update_frame)
        name_entry.pack(anchor=tk.W)
        tk.Label(update_frame, text="Class:", bg="#ecf0f1").pack(anchor=tk.W)
        class_entry = tk.Entry(update_frame)
        class_entry.pack(anchor=tk.W)
        tk.Label(update_frame, text="Roll No:", bg="#ecf0f1").pack(anchor=tk.W)
        roll_no_entry = tk.Entry(update_frame)
        roll_no_entry.pack(anchor=tk.W)
        tk.Label(update_frame, text="PNR No:", bg="#ecf0f1").pack(anchor=tk.W)
        pnr_no_entry = tk.Entry(update_frame)
        pnr_no_entry.pack(anchor=tk.W)
        tk.Label(update_frame, text="Phone No:", bg="#ecf0f1").pack(anchor=tk.W)
        phone_no_entry = tk.Entry(update_frame)
        phone_no_entry.pack(anchor=tk.W)

        # Save button
        def save_profile():
            name = name_entry.get()
            class_ = class_entry.get()
            roll_no = roll_no_entry.get()
            pnr_no = pnr_no_entry.get()
            phone_no = phone_no_entry.get()
            if name and class_ and roll_no and pnr_no and phone_no:
                save_to_csv(name, class_, roll_no, pnr_no, phone_no)
                update_window.destroy()
            else:
                messagebox.showwarning("Incomplete Data", "Please fill in all fields.")

        save_button = tk.Button(update_frame, text="Save", font=("Arial", 12), bg="#3498db", fg="white", command=save_profile)
        save_button.pack(pady=10)

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

    result_button = tk.Button(options_bar_frame, text="Result", font=("Arial", 12), bg="#2c3e50", fg="white", bd=0)
    result_button.pack(pady=5, padx=10, anchor=tk.W)

    att_button = tk.Button(options_bar_frame, text="Attendance", font=("Arial", 12), bg="#2c3e50", fg="white", bd=0)
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
