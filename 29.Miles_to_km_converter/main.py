from tkinter import *

# Window
window = Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)

# Label - Miles
label = Label(text="Miles")
label.grid(column=2, row=0)

# Entry
entry = Entry(width=7)
entry.grid(column=1, row=0)


def button_got_clicked():
    miles = int(entry.get())
    km = round(miles * 1.609, 2)
    label_num.config(text=km)


# Button
button = Button(text="Calculate", command=button_got_clicked)
button.grid(column=1, row=2)

# Label - km
label_km = Label(text="km")
label_km.grid(column=2, row=1)

# Label - number
label_num = Label(text="0")
label_num.grid(column=1, row=1)

# Label - equal to
label_eq = Label(text="is equal to")
label_eq.grid(column=0, row=1)

window.mainloop()
