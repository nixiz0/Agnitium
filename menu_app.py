import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, filedialog
from PIL import Image, ImageTk
import threading
import shutil
import os

from functions.reco_faces import start_reco_faces
from menu_fct import *


def reco_faces():
    cameras_in_use = {}
    root = tk.Toplevel()
    app_theme(root)
    root.withdraw()  
    
    num_cam = simpledialog.askinteger("Cam Info", "Enter the camera number")
    freq_scan = simpledialog.askinteger("Scan Frequency", "Enter the scanning recognition frequency that you want")
    fps = messagebox.askquestion("FPS", "Show FPS ?")
    if fps == 'yes':
        fps = True
    else: 
        fps = False

    # Check if user has entered essential parameters
    if num_cam is not None:
        # Check if the camera is already in use
        if num_cam in cameras_in_use:
            messagebox.showinfo("Cam Info", "The selected camera is already in use.")
        else:
            # Start the recognition faces function in a new thread
            reco_thread = threading.Thread(target=start_reco_faces, args=(num_cam, freq_scan, fps))
            reco_thread.start()
            if not reco_thread.is_alive():
                cameras_in_use = {}
    else:
        messagebox.showerror("Error", "Please enter all essential parameters.")
        
def add_faces():
    filetypes = (
        ('images', '*.png;*.jpg;*.jpeg'),
        ('All files', '*.*')
    )

    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if file_path:
        # Get file name
        filename = os.path.basename(file_path)

        # Set the path of the new folder
        new_folder = 'faces'

        # Create the folder if it doesn't exist
        os.makedirs(new_folder, exist_ok=True)

        # Set the destination path
        dest_path = os.path.join(new_folder, filename)

        # Copy the file
        shutil.copy2(file_path, dest_path)

root = tk.Tk()
root.title("Agnitium")

# Center the window and set its size
center_window(root, width=220, height=215)

# Set the background color to dark gray
root.configure(bg='#333333')

# Load the image with PIL and resize it
image = Image.open("ressources/logo_agnitium.png")
image = image.resize((100, 100), Image.LANCZOS)
image = ImageTk.PhotoImage(image)

# Create a label with the image
image_label = tk.Label(root, image=image, bg='#333333')
image_label.pack()

# Create a style for the buttons
style = ttk.Style()
style.configure('TButton', font=('Inter', 14))

# Create two modern and design buttons using ttk
button1 = ttk.Button(root, text="Faces Recognition", command=reco_faces, style='TButton')
button2 = ttk.Button(root, text="Add Faces", command=add_faces, style='TButton')

# Position the buttons in the middle of the window with a small padding
button1.pack(padx=20, pady=11)
button2.pack(padx=5, pady=5)

root.mainloop()