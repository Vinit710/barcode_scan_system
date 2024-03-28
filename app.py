import tkinter as tk
from tkinter import messagebox

def register_barcode():
    barcode = barcode_entry.get()
    description = description_entry.get()

    # Here you can add code to save the barcode information to a database
    # For this example, we'll just print the information
    print("Barcode:", barcode)
    print("Description:", description)

    messagebox.showinfo("Success", "Barcode registered successfully!")

# Create main window
root = tk.Tk()
root.title("Barcode Registration")

# Create barcode entry
barcode_label = tk.Label(root, text="Barcode:")
barcode_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
barcode_entry = tk.Entry(root)
barcode_entry.grid(row=0, column=1, padx=10, pady=5)

# Create description entry
description_label = tk.Label(root, text="Description:")
description_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1, padx=10, pady=5)

# Create register button
register_button = tk.Button(root, text="Register Barcode", command=register_barcode)
register_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
