import tkinter as tk
from PIL import Image, ImageTk ,ImageFilter

def create_app_window(user_name):
    app_window = tk.Tk()
    app_window.title("Student Login System")
    app_window.state('zoomed')

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
    update_profile_button = tk.Button(options_bar_frame, text="Update Profile", font=("Arial", 12), bg="#2c3e50", fg="white", bd=0)
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


    # --- Scrollable Canvas for Images ---
    canvas = tk.Canvas(right_content_frame, bg="#ffffff", bd=0, highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(right_content_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to contain the images
    images_frame = tk.Frame(canvas, bg="#ffffff")
    canvas.create_window((0, 0), window=images_frame, anchor=tk.NW)

    # Add images to the frame
    for i in range(1):  # Add 10 sample images
        image_path = f"image_{i}.jpeg"  # Replace with the path of your images
        img = Image.open(image_path)
        img.thumbnail((200, 200))  # Resize images to fit the frame
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(images_frame, image=img_tk)
        label.image = img_tk  # Keep reference to prevent garbage collection
        label.pack(pady=10)

    # Update the canvas scroll region
    images_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    return app_window   

# Example usage
create_app_window("John Doe").mainloop()