import tkinter as tk
from math import sqrt

def calculate_distance():
    # Get the input vectors from the entry fields
    x1 = float(entry_x1.get())
    y1 = float(entry_y1.get())
    x2 = float(entry_x2.get())
    y2 = float(entry_y2.get())

    # Calculate the distance between the two points
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Display the distance in the result label
    result_label.config(text=f"Distance: {distance}")

    # Clear the canvas
    canvas.delete("all")

    # Draw the Cartesian coordinates
    canvas.create_line(50, 0, 50, 400, width=1, arrow=tk.LAST)
    canvas.create_line(0, 350, 500, 350, width=1, arrow=tk.LAST)
    canvas.create_text(55, 20, text="Y")
    canvas.create_text(480, 360, text="X")

    # Draw the points
    canvas.create_oval(45 + x1 * 20, 355 - y1 * 20, 55 + x1 * 20, 365 - y1 * 20, fill="red")  # Point 1
    canvas.create_text(60 + x1 * 20, 370 - y1 * 20, text="P1")
    canvas.create_oval(45 + x2 * 20, 355 - y2 * 20, 55 + x2 * 20, 365 - y2 * 20, fill="blue")  # Point 2
    canvas.create_text(60 + x2 * 20, 370 - y2 * 20, text="P2")

    # Draw the vector between the points
    canvas.create_line(50 + x1 * 20, 350 - y1 * 20, 50 + x2 * 20, 350 - y2 * 20, arrow=tk.LAST)

# Create the main window
window = tk.Tk()
window.title("Vector Distance Calculator")

# Create the labels for the first vector
label_vector1 = tk.Label(window, text="Vector 1:")
label_vector1.grid(row=0, column=0, padx=5, pady=5)

label_x1 = tk.Label(window, text="X:")
label_x1.grid(row=1, column=0, padx=5, pady=5)
entry_x1 = tk.Entry(window)
entry_x1.grid(row=1, column=1, padx=5, pady=5)

label_y1 = tk.Label(window, text="Y:")
label_y1.grid(row=2, column=0, padx=5, pady=5)
entry_y1 = tk.Entry(window)
entry_y1.grid(row=2, column=1, padx=5, pady=5)

# Create the labels for the second vector
label_vector2 = tk.Label(window, text="Vector 2:")
label_vector2.grid(row=3, column=0, padx=5, pady=5)

label_x2 = tk.Label(window, text="X:")
label_x2.grid(row=4, column=0, padx=5, pady=5)
entry_x2 = tk.Entry(window)
entry_x2.grid(row=4, column=1, padx=5, pady=5)

label_y2 = tk.Label(window, text="Y:")
label_y2.grid(row=5, column=0, padx=5, pady=5)
entry_y2 = tk.Entry(window)
entry_y2.grid(row=5, column=1, padx=5, pady=5)

# Create the button to calculate the distance
calculate_button = tk.Button(window, text="Calculate Distance", command=calculate_distance)
calculate_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Create the label to display the result
result_label = tk.Label(window, text="Distance: ")
result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Create the canvas for drawing
canvas = tk.Canvas(window, width=500, height=400)
canvas.grid(row=0, column=2, rowspan=8, padx=5, pady=5)

# Start the main event loop
window.mainloop()
