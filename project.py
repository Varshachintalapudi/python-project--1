import tkinter as tk
from tkinter import messagebox, colorchooser
import matplotlib.pyplot as plt
import numpy as np

def plot_graph():
    try:
        x_min = float(x_min_entry.get())
        x_max = float(x_max_entry.get())
        function = function_entry.get()

        x = np.linspace(x_min, x_max, 1000)
        y = eval(function)

        plt.plot(x, y, label=function, color=color_var.get())
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Graph Plot")
        
        if grid_var.get():
            plt.grid(True)

        if legend_var.get():
            plt.legend()

        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Invalid input for x_min and/or x_max.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def choose_color():
    color_code = colorchooser.askcolor(title="Choose Color")
    if color_code[1]:
        color_var.set(color_code[1])

# Create the main application window
app = tk.Tk()
app.title("Graph Plotter")

# Create input labels and entries
x_min_label = tk.Label(app, text="Enter x_min:")
x_min_label.pack()

x_min_entry = tk.Entry(app)
x_min_entry.pack()

x_max_label = tk.Label(app, text="Enter x_max:")
x_max_label.pack()

x_max_entry = tk.Entry(app)
x_max_entry.pack()

function_label = tk.Label(app, text="Enter the function (e.g., 'x**2 + 3*x - 5'):")
function_label.pack()

function_entry = tk.Entry(app)
function_entry.pack()

# Color selection
color_var = tk.StringVar()
color_var.set('b')  # Default color is blue
color_button = tk.Button(app, text="Select Color", command=choose_color)
color_button.pack()

# Grid and Legend options
grid_var = tk.BooleanVar()
grid_checkbutton = tk.Checkbutton(app, text="Show Grid", variable=grid_var)
grid_checkbutton.pack()

legend_var = tk.BooleanVar()
legend_checkbutton = tk.Checkbutton(app, text="Show Legend", variable=legend_var)
legend_checkbutton.pack()

# Create the "Plot" button
plot_button = tk.Button(app, text="Plot", command=plot_graph)
plot_button.pack()

# Start the main loop
app.mainloop()
