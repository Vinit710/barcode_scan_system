import tkinter as tk
from PIL import Image, ImageTk, ImageFilter



def create_app_window(user_name):
    app_window = tk.Tk()
    app_window.title("Student Login System")
    app_window.state('zoomed')

    # ... (Load images)

    # --- Options Bar Frame ---
    # ... (options bar setup)

    # --- Main Content Frame ---
    main_content_frame = tk.Frame(app_window, bg="#ecf0f1")  # Create main_content_frame here
    main_content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # --- Header Frame ---
    header_frame = tk.Frame(main_content_frame, bg="#3498db")  # Now you can reference main_content_frame
    header_frame.pack(fill=tk.X)
    welcome_label = tk.Label(header_frame, text=f"Welcome, {user_name}", 
                        font=("Arial", 18, "bold"),  # Larger font size and bold
                        bg="#3498db", fg="white",  # White text for contrast
                        pady=10)  # Add padding for vertical spacing
    welcome_label.pack()

    # ... (rest of the code for header, content, and footer)

    return app_window

    

    

