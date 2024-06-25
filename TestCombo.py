from tkinter import *
from tkinter import ttk
# Replace 'data' with your actual data list
data = ["Pomme", "Orange", "Banane", "Citron", "Kiwi", "Fraise", "Pêche", "Abricot", "Poire", "Raisin"]
def on_change(event):
    # Get the current text from the entry widget
    new_value = entry.get()
    input_str = combobox.get()
    # Filter the data based on the input
    filtered_data = [x for x in data if x.startswith(input_str)]

    # Update the combobox values with the filtered data
    combobox['values'] = filtered_data
    print(filtered_data)

    # Clear the combobox selection if no matches
    if filtered_data:
        if(len(filtered_data)<=2):
            combobox.set(filtered_data[0])

    # Perform actions based on the new value
    print(f"Input changed to: {new_value}")
    # ... (Your specific actions here)
def update_combobox(event):
    # Get the current text from the entry widget
    input_str = entry.get()

    # Filter the data based on the input
    filtered_data = [x for x in data if x.startswith(input_str)]

    # Update the combobox values with the filtered data
    combobox['values'] = filtered_data

    # Clear the combobox selection if no matches
    if not filtered_data:
        combobox.current(-1)

# Create the main window
window =Tk()

# Create the combobox with auto-completion functionality
combobox =ttk.Combobox(window)
combobox.pack()

# Create an entry widget for user input
entry =Entry(window)
entry.pack()
combobox.bind("<KeyRelease>", on_change)
# Initialize the combobox with the initial data
combobox['values'] = data

# Start the main event loop
window.mainloop()
