import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from app1 import get_plant_data
import random

def create_circle(canvas, x, y, r, color='green'):
    """Draws a circle on the canvas at the specified position and color."""
    return canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=color)

def update_gui():
    plant_data = get_plant_data()
    for i, plant in enumerate(plant_data):
        name_labels[i].config(text=plant['plant_type'])
        moisture_labels[i].config(text=f"Moisture: {plant['moisture_level']}%")
        if plant['needs_water']:
            circle_color = 'red'
        else: 
            circle_color = 'green'
        canvas.itemconfig(circles[i], fill=circle_color, outline=circle_color)
    root.after(10000, update_gui)  # Refresh every 10 seconds

root = tk.Tk()
root.title("Plant Moisture GUI")
root.configure(bg='darkblue')  # Changed to dark blue
root.geometry('800x600')  # Width x Height

canvas = tk.Canvas(root, bg='darkblue', highlightthickness=0, width=800, height=600)  # Changed to match root
canvas.pack(fill=tk.BOTH, expand=True)

button_radius = 50
positions = [(200, 300), (400, 300), (600, 300)]
label_offset_y = 150  # Further increased offset to prevent overlap

name_labels = []
moisture_labels = []
circles = []

for i, pos in enumerate(positions):
    circle = create_circle(canvas, pos[0], pos[1], button_radius, 'green')
    circles.append(circle)
    
    name_label = tk.Label(root, bg='darkblue', fg='white', font=('Arial', 32, 'bold'))  # Increased font size
    name_label.place(x=pos[0], y=pos[1] - label_offset_y, anchor='center')
    name_labels.append(name_label)
    
    moisture_label = tk.Label(root, bg='darkblue', fg='white', font=('Arial', 24))  # Increased font size
    moisture_label.place(x=pos[0], y=pos[1] - label_offset_y + 40, anchor='center')
    moisture_labels.append(moisture_label)

update_gui()  # Initial update to set the labels and circle colors

root.mainloop()