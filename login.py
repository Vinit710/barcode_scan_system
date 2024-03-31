import tkinter as tk
from tkinter import messagebox
import cv2
from pyzbar.pyzbar import decode
import csv

def capture_frames():
    global user_name
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

    print("Captured Frames:", captured_frames)

    # Decode barcodes from the captured frames
    barcode_data = set()
    for frame in captured_frames:
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            try:
                decoded_barcode = obj.data.decode("utf-8")
                barcode_data.add(decoded_barcode)
                print("Decoded Barcode:", decoded_barcode)  # Print decoded barcode
            except Exception as e:
                print("Error decoding barcode:", e)


    
  # Check if user access is allowed
    with open('barcodes.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                csv_barcode, csv_user_name = map(str.strip, row)
                print("CSV Data:", csv_barcode, csv_user_name)  # Debug print
                if user_name == csv_user_name and any(decoded_barcode == csv_barcode for decoded_barcode in barcode_data):
                    print("Access allowed")
                    messagebox.showinfo("Access Granted", "Access allowed")
                    return

    
    print("Access denied")
    messagebox.showerror("Access Denied", "Access denied")

# Create main window
root = tk.Tk()
root.title("User Access Control")

# Create name entry
name_label = tk.Label(root, text="Enter Your Name:")
name_label.pack(padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.pack(padx=10, pady=5)

# Create scan button
scan_button = tk.Button(root, text="Scan Barcode", command=capture_frames)
scan_button.pack(padx=10, pady=5)

# Run the application
root.mainloop()
