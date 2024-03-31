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
            barcode_data.add(obj.data.decode("utf-8"))

    # Save the barcode data to a CSV file
    try:
        with open('barcodes.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            for data in barcode_data:
                writer.writerow([data, user_name])
        messagebox.showinfo("Success", "User registered successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save barcode data: {e}")

# Create main window
root = tk.Tk()
root.title("Student Registration")

# Add title label
title_label = tk.Label(root, text="Student Registration", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Create name entry
name_label = tk.Label(root, text="Enter Your Name:")
name_label.pack(padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.pack(padx=10, pady=5)

# Add instruction label
instruction_label = tk.Label(root, text="Scan your college ID")
instruction_label.pack(pady=5)

# Create scan button
scan_button = tk.Button(root, text="Scan Barcode", command=capture_frames, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), padx=10, pady=5)
scan_button.pack(padx=10, pady=5)

# Run the application
root.mainloop()
