from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

def converter():
    miles_input_value = float(miles_input.get())
    kilometer_result_label['text'] = str(miles_input_value * 1.609)

button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)






window.mainloop()