import tkinter
from tkinter.ttk import Label, Button, Entry

window = tkinter.Tk()
window.minsize(width=500, height=300)
window.maxsize(width=500, height=300)
window.title("Tk GUI Program")

# adding label
font = ("Times New Roman", 20, "normal")
k_label = Label(text="Hello", font=font)
k_label.grid(column=0, row=0)

click_me_button = Button(text="Click Me")
click_me_button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

k_entry = Entry(width= 15)
k_entry.grid(column=4, row=2)
#
# k_button = Button(text="Click Me")
# k_button.pack()
#
# def change_text():
#     k_label.config(text= f"Hello {k_entry.get()}, Have a nice day!")
#
# k_button.config(command=change_text)


window.mainloop()