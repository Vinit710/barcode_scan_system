import tkinter as tk
from PIL import Image, ImageTk, ImageFilter



def create_app_window(user_name):
    app_window = tk.Tk()
    app_window.title("Student Login System")
    app_window.state('zoomed')

    # --- Options Bar Frame ---
    # ... (options bar setup)

    # --- Main Content Frame ---
    main_content_frame = tk.Frame(app_window, bg="#ecf0f1")  # Create main_content_frame here
    main_content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # --- Header Frame ---
    header_frame = tk.Frame(main_content_frame, bg="#3498db")  # Now you can reference main_content_frame
    header_frame.pack(fill=tk.X)
    welcome_label = tk.Label(header_frame, text=f"Welcome, {user_name}", 
                        font=("Arial", 18, "bold"),  
                        bg="#3498db", fg="white",  
                        pady=10)
    welcome_label.pack(side=tk.TOP)  # Place welcome label on top

    # --- Options Bar Frame (Menu Tab) ---
    menu_width = int(app_window.winfo_screenwidth() * 0.2)  # 20% of the screen width for the menu
    content_width = app_window.winfo_screenwidth() - menu_width  # Remaining width for the content

    options_bar_frame = tk.Frame(header_frame, bg="#2c3e50", width=menu_width) 
    options_bar_frame.pack(side=tk.BOTTOM, fill=tk.Y)  # Place on the bottom

    # Menu title label
    menu_label = tk.Label(options_bar_frame, text="Menu", font=("Arial", 14, "bold"), bg="#2c3e50", fg="white")
    menu_label.pack(pady=10)

    # ... (rest of the code for header, content, and footer)

    return app_window

    

    

