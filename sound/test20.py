import tkinter as tk,random

# Create a window
window = tk.Tk()

# Create a label
label = tk.Label(text="No", font=("Helvetica", 200), fg="red")
label.pack()

# Bind the left mouse button to the label
label.bind("<Button-1>", lambda event: label.place(x=random.randint(0, window.winfo_width() - label.winfo_width()), y=random.randint(0, window.winfo_height() - label.winfo_height())))

# Start the main loop
window.mainloop()
