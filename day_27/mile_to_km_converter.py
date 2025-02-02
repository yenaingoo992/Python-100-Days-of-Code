import tkinter
from tkinter import Entry, Label, Button

window = tkinter.Tk()
window.title("Mile To KM Converter")
window.minsize(width=400, height=200)
window.maxsize(width=400, height=200)
window.config(padx=60, pady=50)

font = ("Roboto", 12)

# mile entry
mile_entry = Entry(width=15)
mile_entry.grid(column=1, row=0)

mile_label = Label(text="Miles", font=font)
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=font)
equal_label.grid(column=0, row=1)
equal_label.config(pady=16, padx=10)

km_value = Label(text="0", font=font)
km_value.grid(column=1, row=1)

km_label = Label(text="Km", font=font)
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate")
calculate_button.grid(column=1, row=2)

def mile_to_km_converter():
    mile = float(mile_entry.get())
    km = mile * 1.60934
    km_value.config(text=f"{round(km, 2)}")

calculate_button.config(command=mile_to_km_converter)

window.mainloop()