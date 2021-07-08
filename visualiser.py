from tkinter import *
from tkinter import ttk
import random
from algorithms import bubble_sort, merge_sort, heap_sort
from colours import *

# Set colours for background + text
background = dark_grey
text_colour = white
# if you prefer lighter background uncomment the following two lines
# background = white
# text_colour = black

# Set up initial window
window = Tk()
window.title("Sorting Algorithms Visualisation")
window.maxsize(1000, 700)
window.config(bg=background)

algorithm_name = StringVar()
algo_list = ["Bubble Sort", "Merge Sort", "Heap Sort"]

speed_name = StringVar()
speed_list = ["Fast", "Medium", "Slow"]

data_range = IntVar()
data_range.set(10)

sort_data = []


def draw_data(data, colour_array):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    offset = 4
    x_width = (canvas_width - offset) / (len(data))
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + (offset / 2)
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colour_array[i])

    window.update_idletasks()


# Generate list of nums to sort
def generate_sort_nums():
    global sort_data

    sort_data = list(range(1, data_range.get() + 1))

    for i in range(0, len(sort_data) - 2):
        j = random.randint(i, len(sort_data)-1)
        sort_data[i], sort_data[j] = sort_data[j], sort_data[i]

    draw_data(sort_data, [blue] * len(sort_data))


# Set the sorting speed
def set_speed():
    if speed_menu.get() == "Slow":
        return 0.3
    elif speed_menu.get() == "Medium":
        return 0.1
    else:
        return 0.001


# Perform the sort on the list of nums to be sorted
def sort():
    global sort_data
    time_tick = set_speed()

    if algo_menu.get() == "Bubble Sort":
        bubble_sort(sort_data, draw_data, time_tick)
    elif algo_menu.get() == "Merge Sort":
        merge_sort(sort_data, 0, len(sort_data) - 1, draw_data, time_tick)
    elif algo_menu.get() == "Heap Sort":
        heap_sort(sort_data, draw_data, time_tick)


UI_frame = Frame(window, width=900, height=300, bg=background)
UI_frame.grid(row=1, column=0, padx=10, pady=5)

# Field to set the number of elements to sort (defaults to 10)
data_range_label = Label(UI_frame, text="Number of elements to sort: ", bg=background, fg=text_colour)
data_range_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
data_range_entry = ttk.Entry(UI_frame, textvariable=data_range)
data_range_entry.grid(row=0, column=1, padx=5, pady=5)

# Set up the dropdown to select the sorting algorithm
algo_list_label = Label(UI_frame, text="Algorithm: ", bg=background, fg=text_colour)
algo_list_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=3, padx=5, pady=5)
algo_menu.current(0)

# Set up the dropdown to select the sorting speed
speed_list_label = Label(UI_frame, text="Sorting Speed: ", bg=background, fg=text_colour)
speed_list_label.grid(row=0, column=4, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=0, column=5, padx=5, pady=5)
speed_menu.current(0)

# Button to generate array
generate_button = Button(UI_frame, text="Generate Array", command=generate_sort_nums, bg=light_gray)
generate_button.grid(row=1, column=2, padx=5, pady=5)

# Button to start sorting
sort_button = Button(UI_frame, text="Sort", command=sort, bg=light_gray)
sort_button.grid(row=1, column=3, padx=5, pady=5)

# Canvas to draw the array on
canvas = Canvas(window, width=800, height=400, bg=background)
canvas.grid(row=0, column=0, padx=10, pady=5)


window.mainloop()
