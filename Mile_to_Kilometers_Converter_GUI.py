from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
# window.minsize(width=300, height=50)
window.config(padx=20, pady=20)


def convert():
    entry_miles = float(entry.get())
    calc = round(entry_miles * 1.609)
    label_convert.config(text=f"{calc}")


# Entry
entry = Entry(width=7)
entry.grid(column=1, row=0)

# Labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_convert = Label(text="0")
label_convert.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
