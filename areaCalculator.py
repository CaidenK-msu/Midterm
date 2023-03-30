import tkinter as tk
import math

class AreaCalculatorGUI:
    def init (self):
        self.window = tk.Tk()
        self.window.title ("Area Calculator")

        # label for shape select tab
        shape_label = tk.Label(self.window, text = "Select a shape: ")
        shape_label.pack()

        # This is the dropdown screen for shape selection
        self.shape_options = ["Circle", "Square", "Rectangle", "Triangle"]
        self.shape_var = tk.StringVar()
        self.shape_dropdown = tk.OptionMenu(self.window, self.shape_var, *self.shape_options)
        self.shape_dropdown.pack()

        # Creates label for measurement(s) input from user
        self.measurement_label = tk.Label(self.window, text = "Enter the measurement: ")
        self.measurement_label.pack()
        self.measurement_entry = tk.Entry(self.window)
        self.measurement_entry.pack()

        #button for calculating the area
        self.calculate_button = tk.Button(self.window, text = "Calculate", command = self.calculate_area)
        self.calculate_button.pack()

        #Display for area result
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        #main
        self.window.main()

    def calculate_area(self):
        shape = self.shape_var.get()
        measurement = float(self.measurement_entry.get())

        # Calculate area for selected shape and measurement(s)
        if shape == "Circle":
            area = math.pi * (measurement ** 2)
        elif shape == "Square":
            area = measurement ** 2
        elif shape == "Rectangle":
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            area = width * height
        elif shape == "Triangle":
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            area = 0.5 * base * height

        # Display area result
        self.result_label.config(text = "The area is {:.2f}".format(area))
