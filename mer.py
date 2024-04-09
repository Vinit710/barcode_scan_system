import tkinter as tk
from tkinter import messagebox
import cv2
from pyzbar.pyzbar import decode
import csv
from PIL import Image, ImageTk, ImageFilter

def register_user():
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.state('zoomed')

    # Load and process background image
    image = Image.open("clg.jpg")  # Replace with your image path
    image = image.filter(ImageFilter.GaussianBlur(radius=10))
    photo = ImageTk.PhotoImage(image)

    # Background image label
    background_label = tk.Label(register_window, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Central tab frame
    tab_frame = tk.Frame(register_window, bg="white", width=400, height=200)
    tab_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Title label (Register)
    title_label = tk.Label(tab_frame, text="Register", font=("Helvetica", 16, "bold"), bg="white")
    title_label.pack(pady=10)

    # Name entry
    name_label = tk.Label(tab_frame, text="Enter Your Name:")
    name_label.pack()
    name_entry = tk.Entry(tab_frame)
    name_entry.pack()

    # Scan button
    scan_button = tk.Button(tab_frame, text="Scan Barcode", command=lambda: capture_frames("register", name_entry), bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5)
    scan_button.pack(pady=10)

def login_user():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.state('zoomed')

    # Load and process background image
    image = Image.open("clg.jpg")  # Replace with your image path
    image = image.filter(ImageFilter.GaussianBlur(radius=10))
    photo = ImageTk.PhotoImage(image)

    # Background image label
    background_label = tk.Label(login_window, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Central tab frame
    tab_frame = tk.Frame(login_window, bg="white", width=400, height=200)
    tab_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Title label (Login)
    title_label = tk.Label(tab_frame, text="Login", font=("Helvetica", 16, "bold"), bg="white")
    title_label.pack(pady=10)

    # Name entry
    name_label = tk.Label(tab_frame, text="Enter Your Name:")
    name_label.pack()
    name_entry = tk.Entry(tab_frame)
    name_entry.pack()

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
                        login_window.destroy()  # Close the login window
                        open_app_window(user_name)  # Open the app window
                        
                        return  # Exit the function if access is granted

        messagebox.showerror("Access Denied", "Access denied")

   # Scan button (calling the capture_frames_login function)
    scan_button = tk.Button(tab_frame, text="Scan Barcode", command=capture_frames_login, bg="#008CBA", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5)
    scan_button.pack(pady=10)


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
    


def open_app_window(user_name):
    root.destroy()  # Close the main window
    global app_window  # Make app_window accessible outside the function 
    app_window = tk.Tk()  # Create a new instance of Tk (the main window)
    app_window.title("Student Login System")
    app_window.state('zoomed')  # Maximize the windo

    # Simple UI for the app window
    welcome_label = tk.Label(app_window, text=f"Welcome, {user_name}!", font=("Helvetica", 14, "bold"))
    welcome_label.pack(pady=20)



    
# Create main window
root = tk.Tk()
root.title("Student System")

# Load and process background image (increased blur)
image = Image.open("clg.jpg")
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=10))  # Use GaussianBlur instead of BLUR
photo = ImageTk.PhotoImage(blurred_image) 

# Create a label to display the background image
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the central tab (larger size)
tab_frame = tk.Frame(root, bg="white", width=450, height=11350)  # Increase width and height further
tab_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Welcome label
welcome_label = tk.Label(tab_frame, text="Welcome to the Website", font=("Helvetica", 14, "bold"), bg="white")
welcome_label.pack(pady=10)

# Create buttons for registration and login
register_button = tk.Button(tab_frame, text="Register", command=register_user, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5)
register_button.pack(pady=5)

login_button = tk.Button(tab_frame, text="Login", command=login_user, bg="#008CBA", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5)
login_button.pack(pady=5)

# Run the application
root.mainloop()