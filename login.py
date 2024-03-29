import tkinter as tk
from tkinter import messagebox
import cv2
from pyzbar.pyzbar import decode
import csv



def capture_frames():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Failed to open camera!")
        return
    
    # Prompt user to position the barcode
    messagebox.showinfo("Scan Barcode", "Please position the barcode in front of the camera and press 'q' to scan.")
    
    while True:
        ret, frame = cap.read()
        cv2.imshow("Scan Barcode", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    # Print out captured frame
    print("Captured Frame:", frame)
    
    # Decode barcodes from the captured frame
    decoded_objects = decode(frame)
    barcode_data = {obj.data.decode("utf-8") for obj in decoded_objects}
    
    print("Scanned Barcodes:", barcode_data)
    
    # Get user input
    user_name = name_entry.get()
    
    # Check if user access is allowed
    access_allowed = False
    with open('barcodes.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                csv_user_name, csv_barcode = map(str.strip, row)
                print("CSV Data:", csv_user_name, csv_barcode)  # Debug print
                if csv_user_name == user_name and csv_barcode in barcode_data:
                    access_allowed = True
                    break
    
    if access_allowed:
        messagebox.showinfo("Access Granted", "User access allowed!")
    else:
        messagebox.showerror("Access Denied", "Access denied!")


# Create main window
root = tk.Tk()
root.title("User Access Control")

# Create name entry
name_label = tk.Label(root, text="Enter Your Name:")
name_label.pack(padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.pack(padx=10, pady=5)

# Create access button
access_button = tk.Button(root, text="Check Access", command=capture_frames)
access_button.pack(padx=10, pady=5)

# Run the application
root.mainloop()
