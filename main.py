from tkinter import *
from tkinter.ttk import *
import webbrowser
import json

# import json settings
json_file_handle = open('data.json', )
json_file = json.load(json_file_handle)
buttons = json_file

# root window
root = Tk()
root.geometry("200x400")
root.resizable(False, False)
root.title('Links')

# create scrollbar
def onFrameConfigure(window_canvas):
    '''Reset the scroll region to encompass the inner frame'''
    window_canvas.configure(scrollregion=window_canvas.bbox("all"))


# create canvas
canvas = Canvas(root, borderwidth=0)
# create frame in canvas
frame = Frame(canvas)
# create scrollbar
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4, 4), window=frame, anchor="nw")

# Resize the scrollbar if the frame size changes
frame.bind("<Configure>", lambda event, window_canvas=canvas: onFrameConfigure(canvas))


# Create buttons
i = 0

for x in buttons:
    b = Button(frame, text=x["name"], command=lambda url=x["url"]: webbrowser.open(url))
    b.pack(side=TOP,
           padx=5,
           pady=5,
           fill='x')
    i == 1


root.mainloop()
