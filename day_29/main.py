import os.path
from tkinter import *
from tkinter import messagebox
from password_generator import PasswordManager
import pandas

def save():
    website = website_input.get().strip().title()
    email = email_input.get().strip()
    password = password_input.get().strip()

    if website != "" and email != "" and password != "":
        # File path for the CSV
        file_path = "passwords.csv"

        # New data to be saved
        new_entry = {
            "website": website,
            "email": email,
            "password": password
        }

        # Load existing data if the file exists
        if os.path.exists(file_path):
            df = pandas.read_csv(file_path)
        else:
            df = pandas.DataFrame(columns=["website", "email", "password"])

        # Ensure column names match exactly
        df.columns = ["website", "email", "password"]

        # Remove existing entry if BOTH website & email match (to replace old password)
        df = df[~((df["website"] == new_entry["website"]) & (df["email"] == new_entry["email"]))]

        # Add new entry
        new_entry_df = pandas.DataFrame([new_entry])
        df = pandas.concat([df, new_entry_df], ignore_index=True)

        # Save the updated data back to the CSV
        df.to_csv(file_path, index=False)

        is_ok = messagebox.showinfo(title="Info", message="Your password saved successfully!")
        if is_ok:
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showerror(title="Error!", message="Please don't leave any box empty!")

def generate_password():
    random_password = PasswordManager().generate_password()
    password_input.delete(0, END)
    password_input.insert(0, random_password)

FONT = ("Times New Roman", 12, "normal")
BG = "#ffffff"
window = Tk()
window.title("Password Manager")
window.configure(bg=BG, padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg=BG, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT, bg=BG)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/UserName:", font=FONT, bg=BG)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=FONT, bg=BG)
password_label.grid(row=3, column=0)

website_input = Entry()
website_input.grid(row=1, column=1, columnspan=2, sticky='EW')
website_input.focus()

email_input = Entry()
email_input.grid(row=2, column=1, columnspan=2, sticky='EW')
email_input.insert(0, "yenaingoo992@gmail.com")

password_input = Entry()
password_input.grid(row=3, column=1, sticky='EW')

generate_button = Button(text="Generate Password", bg=BG, command= generate_password)
generate_button.grid(row=3, column=2)

save_button = Button(text="Save", bg=BG, command=save)
save_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()
