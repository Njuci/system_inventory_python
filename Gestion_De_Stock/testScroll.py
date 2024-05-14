import tkinter as tk
from tkinter import *
# Create the main window
window = tk.Tk()
window.title("Scrollable List Example")

# Define the frame to hold the list items
frame = tk.Frame(window)
frame.place(relx=0.0, rely=0.0, relheight=0.9,relwidth=1)

# Create the canvas for scrolling
canvas = tk.Canvas(frame, bg='blue')
canvas.place(relx=0.1, rely=0.1,relwidth=0.8,relheight=0.9)


# Create a scrollbar for vertical scrolling
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.place(relx=0.9, rely=0.1, relheight=0.9)

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Define the list of items to display
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10"]

# Variable to track the next item's y-position
y = 0

# Add items to the canvas
# Add items to the canvas using create_window()
t=1
for item in items:
    if t==1:
        label = Frame(canvas, bg='white',height=40,width=300)
        label.place(relx=0.02, rely=0, relwidth=0.9, relheight=0.1)
        ligne = Frame(label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=0.9)

        # Labels for article name and quantity
        title = Label(label, text="", font=('Segoe UI', 10), fg='#adabab', bg='white').place(relx=0.03, rely=0.25, relwidth=0.43)
        title = Label(label, text="", font=('Segoe UI ', 10), fg='#adabab', bg='white').place(relx=0.4, rely=0.25, relwidth=0.43)

        window_id = canvas.create_window(20, y, anchor=tk.W, window=label)  # Adjust x-position (20 here) as needed
        canvas.bind("<Button-1>", lambda event, label=label: on_click_handler(label.cget('text')))  # Bind click event
        y += label.winfo_reqheight() + 5
        label = Frame(canvas, bg='white',height=40,width=300)
        label.place(relx=0.02, rely=0, relwidth=0.9, relheight=0.1)
        ligne = Frame(label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=0.9)

        # Labels for article name and quantity
        title = Label(label, text=item, font=('Segoe UI', 10), fg='#adabab', bg='white').place(relx=0.03, rely=0.25, relwidth=0.43)
        title = Label(label, text=item, font=('Segoe UI ', 10), fg='#adabab', bg='white').place(relx=0.4, rely=0.25, relwidth=0.43)

        window_id = canvas.create_window(20, y, anchor=tk.W, window=label)  # Adjust x-position (20 here) as needed
        canvas.bind("<Button-1>", lambda event, label=label: on_click_handler(label.cget('text')))  # Bind click event
        y += label.winfo_reqheight() + 0
    else :
        label = Frame(canvas, bg='white',height=40,width=300)
        label.place(relx=0.02, rely=0, relwidth=0.9, relheight=0.1)
        ligne = Frame(label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=0.9)

        # Labels for article name and quantity
        title = Label(label, text=item, font=('Segoe UI', 10), fg='#adabab', bg='white').place(relx=0.03, rely=0.25, relwidth=0.43)
        title = Label(label, text=item, font=('Segoe UI ', 10), fg='#adabab', bg='white').place(relx=0.4, rely=0.25, relwidth=0.43)

        window_id = canvas.create_window(20, y, anchor=tk.W, window=label)  # Adjust x-position (20 here) as needed
        canvas.bind("<Button-1>", lambda event, label=label: on_click_handler(label.cget('text')))  # Bind click event
        y += label.winfo_reqheight() + 0
    t=0
    # Update the canvas's scrollable region
canvas.update_idletasks()
canvas.config(scrollregion=(0, 0, canvas.winfo_width(), canvas.winfo_height() + y))


    
# Function to handle item click (optional)
def on_click_handler(item):
    print("Clicked item:", item)

# Start the Tkinter event loop
window.mainloop()
