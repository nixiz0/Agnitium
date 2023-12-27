# Design for the simpledialog (user input)
def app_theme(root):
    root.tk_setPalette(background='#333333', foreground='#ffffff')

def center_window(root, width, height):
    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position of the upper left corner of the window to center it
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    # Set minimum and maximum size of the window
    min_width = width - 7
    min_height = height - 7
    max_width = width + 20
    max_height = height + 20
    root.minsize(min_width, min_height)
    root.maxsize(max_width, max_height) 