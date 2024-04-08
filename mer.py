import tkinter as tk
from tkinter import messagebox
import cv2
from pyzbar.pyzbar import decode
import csv

def register_user():
    # Create a new window for registration
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    
    # Name entry label and field
    name_label = tk.Label(register_window, text="Enter Your Name:")
    name_label.pack(padx=10, pady=5)
    name_entry = tk.Entry(register_window)
    name_entry.pack(padx=10, pady=5)

    # Scan button
    scan_button = tk.Button(register_window, text="Scan Barcode", command=lambda: capture_frames("register", name_entry), bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5)
    scan_button.pack(pady=5)

def login_user():
    # Create a new window for login
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    
    # Name entry label and field
    name_label = tk.Label(login_window, text="Enter Your Name:")
    name_label.pack(padx=10, pady=5)
    name_entry = tk.Entry(login_window)
    name_entry.pack(padx=10, pady=5)

    def capture_frames_login():
        user_name = name_entry.get()

        # Open the camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "Failed to open camera!")
            return

        # Prompt user to position the barcode
        messagebox.showinfo("Scan Barcode", "Please position the barcode in front of the camera and press 'q' to capture frames.")

        # Capture frames
        captured_frames = []
        while True:
            ret, frame = cap.read()
            cv2.imshow("Scan Barcode", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            captured_frames.append(frame)
        cap.release()
        cv2.destroyAllWindows()

        # Decode barcodes from the captured frames
        barcode_data = set()
        for frame in captured_frames:
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                try:
                    decoded_barcode = obj.data.decode("utf-8")
                    barcode_data.add(decoded_barcode)
                except Exception as e:
                    print("Error decoding barcode:", e)

        # Check for a match in the CSV file
        with open('barcodes.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    csv_barcode, csv_user_name = map(str.strip, row)
                    if user_name == csv_user_name and any(decoded_barcode == csv_barcode for decoded_barcode in barcode_data):
                        messagebox.showinfo("Access Granted", "Access allowed")
                        return  # Exit the function if access is granted

        messagebox.showerror("Access Denied", "Access denied")

    # Scan button (calling the new capture_frames_login function)
    scan_button = tk.Button(login_window, text="Scan Barcode", command=capture_frames_login, bg="#008CBA", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5)
    scan_button.pack(pady=5)

def capture_frames(mode, name_entry):
    user_name = name_entry.get()

    # Open the camera
    cap = cv2.VideoCapture(0) 
    if not cap.isOpened():
        messagebox.showerror("Error", "Failed to open camera!")
        return

    # Prompt user to position the barcode
    messagebox.showinfo("Scan Barcode", "Please position the barcode in front of the camera and press 'q' to capture frames.")

    # Capture frames
    captured_frames = []
    while True:
        ret, frame = cap.read()
        cv2.imshow("Scan Barcode", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        captured_frames.append(frame)
    cap.release()
    cv2.destroyAllWindows()

    # Decode barcodes from the captured frames
    barcode_data = set()
    for frame in captured_frames:
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            try:
                decoded_barcode = obj.data.decode("utf-8")
                barcode_data.add(decoded_barcode)
            except Exception as e:
                print("Error decoding barcode:", e)

    if mode == "register":
        # Save the barcode data to a CSV file
        try:
            with open('barcodes.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                # Write each decoded barcode along with the username
                for data in barcode_data:  
                    writer.writerow([data, user_name]) 
            messagebox.showinfo("Success", "User registered successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save barcode data: {e}")


# Create main window
root = tk.Tk()
root.title("Student System")

# Add title label
title_label = tk.Label(root, text="Student System", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Create buttons for registration and login (side by side with spacing)
register_button = tk.Button(root, text="Register", command=register_user, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5)
register_button.pack(side=tk.LEFT, padx=10)

login_button = tk.Button(root, text="Login", command=login_user, bg="#008CBA", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5)
login_button.pack(side=tk.LEFT)

# Run the application
root.mainloop()